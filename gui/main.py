##    Copyright (C) 2007 Ivan Garcia contact@ivangarcia.org
##    This program is free software; you can redistribute it and/or modify
##    it under the terms of the GNU General Public License as published by
##    the Free Software Foundation; either version 2 of the License, or
##    (at your option) any later version.
##
##    This program is distributed in the hope that it will be useful,
##    but WITHOUT ANY WARRANTY; without even the implied warranty of
##    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##    GNU General Public License for more details.
##
##    You should have received a copy of the GNU General Public License along
##    with this program; if not, write to the Free Software Foundation, Inc.,
##    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.Warning

""" Create and launch the GUI """
import sys, re, os, traceback, tempfile
#sys.path.append(os.path.dirname(os.path.dirname(os.getcwd())))

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import Qt, SIGNAL, QObject, QCoreApplication, \
                         QSettings, QVariant, QSize, QEventLoop, QString, \
                         QBuffer, QIODevice, QModelIndex,QDir
from PyQt4.QtGui import QPixmap, QErrorMessage, QLineEdit, \
                        QMessageBox, QFileDialog, QIcon, QDialog, QInputDialog,QDirModel
from PyQt4.Qt import qDebug, qFatal, qWarning, qCritical

from subdownloader import * 
from subdownloader.OSDBServer import OSDBServer
from subdownloader.gui import installErrorHandler, Error, _Warning, \
                          extension
from subdownloader.gui.uploadlistview import UploadListModel, UploadListView
from subdownloader.gui.videolistview import VideoListModel, VideoListView
from subdownloader.gui.sublistview import SubListModel, SubListView
from subdownloader.gui.subosdblistview import SubOsdbListModel, SubOsdbListView

from subdownloader.gui.uploadlistview import UploadListModel, UploadListView

from subdownloader.gui.videotreeview import VideoTreeModel
from subdownloader.gui.subosdblistview import SubOsdbListModel, SubOsdbListView

from subdownloader.gui.main_ui import Ui_MainWindow
import subdownloader.FileManagement.FileScan as FileScan
import subdownloader.videofile as videofile
import subdownloader.subtitlefile as subtitlefile

import logging
log = logging.getLogger("subdownloader.gui.main")

class Main(QObject, Ui_MainWindow): 
    def report_error(func):
        """ 
        Decorator to ensure that unhandled exceptions are displayed 
        to users via the GUI
        """
        def function(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception, e:
                Error("There was an error calling " + func.__name__, e)
                raise
        return function
        
    
    def read_settings(self):
        settings = QSettings()
        settings.beginGroup("MainWindow")
        self.window.resize(settings.value("size", QVariant(QSize(1000, 700))).\
                            toSize())
        settings.endGroup()
        #self.database_path = settings.value("database path", QVariant(os.path\
         #                           .expanduser("~/library.db"))).toString()
    
    def write_settings(self):
        settings = QSettings()
        settings.beginGroup("MainWindow")
        settings.setValue("size", QVariant(self.window.size()))
        settings.endGroup()
    
    def close_event(self, e):
        self.write_settings()
        e.accept()
    
    def __init__(self, window, log_packets, options):
        QObject.__init__(self)
        Ui_MainWindow.__init__(self)
        
        self.key = '-1'
        self.log_packets = log_packets
        self.options = options
        self.setupUi(window)
        self.card = None
        self.window = window
        window.closeEvent = self.close_event
        window.setWindowTitle(QtGui.QApplication.translate("MainWindow", "SubDownloader "+APP_VERSION, None, QtGui.QApplication.UnicodeUTF8))
        self.read_settings()
        
        #self.treeView.reset()
        window.show()
        model = QDirModel(window)
        
        #SETTING UP FOLDERVIEW
        model.setFilter(QDir.AllDirs|QDir.NoDotAndDotDot)
        self.folderView.setModel(model)
        index = model.index(QDir.rootPath())
        self.folderView.setRootIndex(index)
        
        self.folderView.header().hide()
        self.folderView.hideColumn(3)
        self.folderView.hideColumn(2)
        self.folderView.hideColumn(1)

        QObject.connect(self.folderView, SIGNAL("activated(QModelIndex)"), \
                            self.folderView_clicked)
        QObject.connect(self.folderView, SIGNAL("clicked(QModelIndex)"), \
                            self.folderView_clicked)    
                            
        #SETTING UP VIDEOS_VIEW
        self.videoModel = VideoTreeModel(window) 
        self.videoView.setModel(self.videoModel)
        QObject.connect(self.videoModel, SIGNAL("dataChanged(QModelIndex,QModelIndex)"), self.subtitlesCheckedChanged)
        #SETTING UP SUBS_OSDB_VIEW
        #self.subs_osdb_model = SubOsdbListModel(window)  

        #SETTING UP UPLOAD_VIEW
        #self.upload_model = UploadListModel(window)    
        
        QObject.connect(self.buttonDownload, SIGNAL("clicked(bool)"), self.click_download)

        self.folderView.show()
        
        self.status_progress = QtGui.QProgressBar(self.statusbar)
        self.status_progress.setProperty("value",QVariant(0))
        
        self.status_progress.setOrientation(QtCore.Qt.Horizontal)
        self.status_label = QtGui.QLabel("v"+ APP_VERSION,self.statusbar)
        
        self.statusbar.insertWidget(0,self.status_label)
        self.statusbar.addPermanentWidget(self.status_progress,2)

        self.establish_connection()
        QCoreApplication.processEvents(QEventLoop.ExcludeUserInputEvents)
        
        #FOR TESTING
        #self.SearchVideos('/media/data/videos/downloaded/')
        
    def subtitlesCheckedChanged(self):
       subs = self.videoModel.getCheckedSubtitles()
       if subs:
           self.buttonDownload.setEnabled(True)
           self.buttonPlay.setEnabled(True)
       else:
           self.buttonDownload.setEnabled(False)
           self.buttonPlay.setEnabled(False)
           
           
    def SearchVideos(self, path):
        #Scan recursively the selected directory finding subtitles and videos
        videos_found,subs_found = FileScan.ScanFolder(path,recursively = True,report_progress = self.progress)

        #Populating the items in the VideoListView
        self.videoModel.clearTree()
        self.videoView.expandAll()
        self.videoModel.setVideos(videos_found)
        self.videoView.setModel(self.videoModel)
        
        self.videoView.expandAll() #This was a solution found to refresh the treeView
        #Searching our videohashes in the OSDB database
        QCoreApplication.processEvents(QEventLoop.ExcludeUserInputEvents)
        
        self.status("Asking Database...")
        #This effect causes the progress bar turn all sides
        self.status_progress.setMinimum(0)
        self.status_progress.setMaximum(0)
        
        self.window.setCursor(Qt.WaitCursor)
        videoSearchResults = self.OSDBServer.SearchSubtitles("",videos_found)
        self.videoModel.clearTree()
        self.videoModel.setVideos(videoSearchResults)
        self.videoView.expandAll() #This was a solution found to refresh the treeView

        self.progress(100)
        self.status_progress.setFormat("Search finished")
    
        self.window.setCursor(Qt.ArrowCursor)
        #TODO: check if the subtitle found is already in our folder.
        #self.OSDBServer.CheckSubHash(sub_hashes) 
    """What to do when a Folder in the tree is clicked"""
    def folderView_clicked(self, index):
        if index.isValid():
            data = self.folderView.model().filePath(index)
        
        folder_path = unicode(data, 'utf-8')
        self.SearchVideos(folder_path)

    def click_download(self, checked):
        #We download the subtitle in the same folder than the video
        subs = self.videoModel.getCheckedSubtitles()
        return 
        #Let's detect which subtitles the user want to download
        rows = frozenset([ index.row() for index in self.subs_osdb_view.selectedIndexes()])
        if not len(rows):
            QMessageBox.about(self.window,"Error","You need to select 1 or more subtitles to download")
        else:
            
            percentage = 100/len(rows)
            count = 0
            self.status("Connecting to download...")
            for row in rows:
                sub = self.subs_osdb_model.getSubFromRow(row)
                id_online = sub.getIdOnline()
                sub_filename = sub.getFileName()
                self.progress(count,"Downloading subtitle... "+id_online)
                count += percentage
                try:
                    #This effect causes the progress bar turn all sides
                    destinationpath = os.path.join(destinationfolder,sub_filename)
                    print destinationpath
                    videos_result = self.OSDBServer.DownloadSubtitle(id_online,destinationpath)
                except Exception, e: 
                    traceback.print_exc(e)
                    qFatal("Unable to download subtitle "+id_online)
        
            self.status("Subtitles downloaded succesfully.")
            self.progress(100)
        
    
    def videos_leftclicked(self, index):
        if index.isValid():
            subs = self.video_model.getSubsFromIndex(index.row())
        #print len(subs)
        self.subs_osdb_model.setSubs(subs)
        self.subs_osdb_view.setModel(self.subs_osdb_model)
        self.subs_osdb_view.resizeColumnsToContents()
        
    def videos_rightclicked(self, point):
        menu = QtGui.QMenu(self.video_view)
        menu.addAction(self.actionUpload_Subtitle)
        menu.exec_(self.video_view.mapToGlobal(point))
        #if index.isValid():
            #print "hello"
        
    def subs_odbc_rightclicked(self, point):
        menu = QtGui.QMenu(self.subs_osdb_view)
        menu.addAction(self.actionDownload_Subtitle)
        menu.exec_(self.subs_osdb_view.mapToGlobal(point))
        #if index.isValid():
            #print "hello"

    def subs_rightclicked(self, point):
        menu = QtGui.QMenu(self.sub_view)
        menu.addAction(self.actionUpload_Subtitle)
        menu.exec_(self.sub_view.mapToGlobal(point))
        #if index.isValid():
            #print "hello"
        
    def update_language(self,lang):
        self.label_language.setText(lang)
        
    
    """Control the STATUS BAR PROGRESS"""
    def progress(self, val,msg = None):
        self.status_progress.setMaximum(100)
        self.status_progress.reset()
        if msg != None:
            self.status_progress.setFormat(msg + ": %p%")
        if val < 0:
            self.status_progress.setMaximum(0)
        else: 
            self.status_progress.setValue(val)
        QCoreApplication.processEvents(QEventLoop.ExcludeUserInputEvents)
    
    def status(self, msg):
        self.status_progress.setMaximum(100)
        self.status_progress.reset()
        self.status_progress.setFormat(msg + ": %p%")
        self.progress(0)
        QCoreApplication.processEvents(QEventLoop.ExcludeUserInputEvents)
    
    def establish_connection(self):
        self.window.setCursor(Qt.WaitCursor)

        self.status("Connecting to server")        
        try:
            self.OSDBServer = OSDBServer(self.options)
        except Exception, e: 
            traceback.print_exc(e)
            qFatal("Unable to connect to server. Please try later")
        self.progress(100)
        self.status_progress.setFormat("Connected")
    
        self.window.setCursor(Qt.ArrowCursor)
    

def main(options):
    
    from PyQt4.Qt import QApplication, QMainWindow
    
    log.debug("Building main dialog")
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setWindowTitle(APP_TITLE)
    window.setWindowIcon(QIcon(":/icon"))
    installErrorHandler(QErrorMessage(window))
    QCoreApplication.setOrganizationName("IvanGarcia")
    QCoreApplication.setApplicationName(APP_TITLE)
    
    log.debug("Showing main dialog")
    Main(window,"", options)    
    
    return app.exec_()

#if __name__ == "__main__": 
#    sys.exit(main())
