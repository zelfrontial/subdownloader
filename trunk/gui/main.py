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
sys.path.append(os.path.dirname(os.path.dirname(os.getcwd())))

from PyQt4 import QtCore, QtGui,Qt
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
from subdownloader.gui.widgets import LibraryBooksModel, DeviceBooksModel, \
                                  DeviceModel
from subdownloader.gui.main_ui import Ui_MainWindow
import subdownloader.FileManagement.FileScan as FileScan
import subdownloader.videofile as videofile
import subdownloader.subtitlefile as subtitlefile
import subdownloader.languages.Languages as languages

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
    

    
    def __init__(self, window, log_packets):
        QObject.__init__(self)
        Ui_MainWindow.__init__(self)
        
        self.key = '-1'
        self.log_packets = log_packets

        self.setupUi(window)
        self.card = None
        self.window = window
        window.closeEvent = self.close_event
        self.read_settings()
        
    	#self.treeView.reset()
        window.show()
	model = QDirModel(window)
	
    	model.setFilter(QDir.AllDirs|QDir.NoDotAndDotDot)
    	self.folderView.setModel(model)
	index = model.index(QDir.rootPath())
	self.folderView.setRootIndex(index)
	#print model.removeColumns(2,2,index)
	
	self.folderView.header().hide()
	self.folderView.hideColumn(3)
	self.folderView.hideColumn(2)
	self.folderView.hideColumn(1)
	
	QObject.connect(self.folderView, SIGNAL("activated(QModelIndex)"), \
                        self.folderView_clicked)
        QObject.connect(self.folderView, SIGNAL("clicked(QModelIndex)"), \
                        self.folderView_clicked)        
	
	QObject.connect(self.tree_videos, SIGNAL("customContextMenuRequested(const QPoint &)"), self.tree_videos_clicked)
	
	
	#self.tree_videos.setColumnCount(1)
	self.tree_videos.setColumnWidth(0,3)
	self.tree_subs.setColumnWidth(0,3)

	self.folderView.show()
	
	self.status_progress = QtGui.QProgressBar(self.statusBar)
	self.status_progress.setProperty("value",QVariant(0))
	
        self.status_progress.setOrientation(QtCore.Qt.Horizontal)
	self.status_label = QtGui.QLabel("v"+ APP_VERSION,self.statusBar)
	
	
	self.statusBar.insertWidget(0,self.status_label)
	self.statusBar.addPermanentWidget(self.status_progress,2)
	
	self.establish_connection()
        
        QCoreApplication.processEvents(QEventLoop.ExcludeUserInputEvents)

    
    """What to do when a Folder in the tree is clicked"""
    def folderView_clicked(self, index):
        if index.isValid():
            data = self.folderView.model().filePath(index)
            folder_path = unicode(data, 'utf-8')
	    ###print folder_path
	    self.tree_videos.clear()
	    self.tree_subs.clear()
	    #Scan recursively the selected directory finding subtitles and videos
	    videos_found,subs_found = FileScan.ScanFolder(folder_path,recursively = True,report_progress = self.progress)
	    
	    #We need to save a tablelink between hashes and TreeWidgetItems bcs we will need that items after searching
	    self.videohashes_treeitems = {}
	    self.subhashes_treeitems = {}
	    
	    #Populating the items in the treewidgets
	    for video in videos_found:
		item = QtGui.QTreeWidgetItem(self.tree_videos)
		item.setText(1,os.path.basename(video.getFilePath()))

		self.videohashes_treeitems[video.getHash()] = item
		
	    sub_hashes = []
	    
	    
    
	    for sub in subs_found:
		item = QtGui.QTreeWidgetItem(self.tree_subs)
		sub_hashes.append(sub.getHash())
		self.subhashes_treeitems[sub.getHash()] = item
		item.setCheckState(0,Qt.Unchecked)
		item.setText(1,os.path.basename(sub.getFilePath()))
		
		

	    
	    #Searching our videohashes in the OSDB database
	    QCoreApplication.processEvents(QEventLoop.ExcludeUserInputEvents)
	    self.status("Asking Database...")
	    #This effect causes the progress bar turn all sides
	    #self.status_progress.setMinimum(0)
	    #self.status_progress.setMaximum(0)
	    
	    self.window.setCursor(Qt.WaitCursor)
	    try:
		videos_result = self.OSDBServer.SearchSubtitles("",videos_found)
	    except Exception, e: 
		traceback.print_exc(e)
		qFatal("Unable to connect to server. Please try later")
	    
	
	    
	    root_subs = self.tree_subs.invisibleRootItem()
	    for video in videos_result:
		if video.hasSubtitles():
		    item = self.videohashes_treeitems[video.getHash()]
		    for sub in video.getSubtitles():
			
			item_sub = QtGui.QTreeWidgetItem(item)
			#item_sub.setText(0,sub['SubLanguageID'])
			#item_sub.setText(0,sub['SubFileName'])
			lang_xx= languages.xxx2xx(sub['SubLanguageID'])
			lang_name = languages.xxx2name(sub['SubLanguageID'])
			
			image_file = lang_xx + '.gif'
			icon = QtGui.QIcon(":/images/flags/" + image_file)
			item_sub.setIcon(0,icon)
			item_sub.setText(1,sub['SubFileName'])
			item_sub.setText(0,lang_name)
			
			
			if self.subhashes_treeitems.has_key(sub['SubHash']):
			    item_sub.setTextColor(0,QtGui.QColor("red"))
			    item_sub.setCheckState(0,Qt.Checked)
			    delete_item = self.subhashes_treeitems[sub['SubHash']]
			    root_subs.takeChild(root_subs.indexOfChild(delete_item))
			    del self.subhashes_treeitems[sub['SubHash']]
			else:
			    item_sub.setCheckState(0,Qt.Unchecked)
	
	    #We romove from subs_found the subtitles found indexed online
	    temp = []
	    temp.extend(subs_found) 
	    for mysub in subs_found:
		if not self.subhashes_treeitems.has_key(mysub.getHash()):
		    temp.remove(mysub)
	    
	    subs_found = temp
	    
	    #Trying to autodetect the language
	    percentage = 100 / len(subs_found)
	    count = 0
	    for sub in subs_found:
		detected_lang = languages.AutoDetectLang(sub.getFilePath())
		if detected_lang != None:
		    lang_xx = languages.name2xx(detected_lang)
		    image_file = lang_xx + '.gif'
		    icon = QtGui.QIcon(":/images/flags/" + image_file)
		    item = self.subhashes_treeitems[sub.getHash()]
		    item.setIcon(0,icon)
		    item.setText(0,detected_lang)
		    count += percentage
		    self.progress(count,"Autodetecting Language: " + os.path.basename(sub.getFilePath()))
	    self.tree_subs.resizeColumnToContents(0)
	    self.tree_subs.setColumnWidth(0,self.tree_subs.columnWidth(0)+20)
	    self.tree_videos.resizeColumnToContents(0)
	    self.tree_videos.setColumnWidth(0,self.tree_videos.columnWidth(0)+50)
	    self.tree_videos.expandAll()
	    self.progress(100)
	    self.status_progress.setFormat("Results returned.")
	
	    self.window.setCursor(Qt.ArrowCursor)
	    
	    #self.OSDBServer.CheckSubHash(sub_hashes)
    
    """Control the STATUS BAR PROGRESS"""
    def tree_videos_clicked(self, point):
	item = self.tree_videos.itemAt(point)
	print item.text(0)
	menu = QtGui.QMenu(self.tree_videos)
	menu.addAction(self.actionUpload_Subtitle)
	menu.exec_(self.tree_videos.mapToGlobal(point))
	
    """Control the STATUS BAR PROGRESS"""
    def progress(self, val,msg = None):
        if val < 0:
            self.status_progress.setMaximum(0)
        else: self.status_progress.setValue(val)
	if msg != None:
	    self.status_progress.setFormat(msg + ": %p%")
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
            self.OSDBServer = OSDBServer()       
        except Exception, e: 
            traceback.print_exc(e)
            qFatal("Unable to connect to server. Please try later")
        self.progress(100)
        self.status_progress.setFormat("Connected")
	
        self.window.setCursor(Qt.ArrowCursor)
    

def main():
    
    from PyQt4.Qt import QApplication, QMainWindow
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setWindowTitle(APP_TITLE)
    window.setWindowIcon(QIcon(":/icon"))
    installErrorHandler(QErrorMessage(window))
    QCoreApplication.setOrganizationName("IvanGarcia")
    QCoreApplication.setApplicationName(APP_TITLE)
    Main(window,"")    
    
    return app.exec_()

if __name__ == "__main__": 
    sys.exit(main())
