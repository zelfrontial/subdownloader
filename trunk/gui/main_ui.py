# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Wed Jun 18 13:13:53 2008
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(780, 593)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setGeometry(QtCore.QRect(0, 24, 780, 545))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.vboxlayout = QtGui.QVBoxLayout()

        self.tabs = QtGui.QTabWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabs.sizePolicy().hasHeightForWidth())
        self.tabs.setSizePolicy(sizePolicy)
        self.tabs.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabs.setObjectName("tabs")
        self.tab = QtGui.QWidget()
        self.tab.setGeometry(QtCore.QRect(0, 0, 756, 496))
        self.tab.setObjectName("tab")
        self.vboxlayout1 = QtGui.QVBoxLayout(self.tab)
        self.vboxlayout1.setObjectName("vboxlayout1")
        self.hboxlayout = QtGui.QHBoxLayout()

        self.buttonPlay = QtGui.QPushButton(self.tab)
        self.buttonPlay.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonPlay.sizePolicy().hasHeightForWidth())
        self.buttonPlay.setSizePolicy(sizePolicy)
        self.buttonPlay.setObjectName("buttonPlay")
        self.hboxlayout.addWidget(self.buttonPlay)
        self.buttonDownload = QtGui.QPushButton(self.tab)
        self.buttonDownload.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonDownload.sizePolicy().hasHeightForWidth())
        self.buttonDownload.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.buttonDownload.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/download.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonDownload.setIcon(icon)
        self.buttonDownload.setObjectName("buttonDownload")
        self.hboxlayout.addWidget(self.buttonDownload)
        self.buttonIMDB = QtGui.QPushButton(self.tab)
        self.buttonIMDB.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonIMDB.sizePolicy().hasHeightForWidth())
        self.buttonIMDB.setSizePolicy(sizePolicy)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/imdb.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonIMDB.setIcon(icon1)
        self.buttonIMDB.setIconSize(QtCore.QSize(32, 16))
        self.buttonIMDB.setObjectName("buttonIMDB")
        self.hboxlayout.addWidget(self.buttonIMDB)
        spacerItem = QtGui.QSpacerItem(231, 27, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)
        self.label_9 = QtGui.QLabel(self.tab)
        self.label_9.setObjectName("label_9")
        self.hboxlayout.addWidget(self.label_9)
        self.filterLanguageForVideo = QtGui.QComboBox(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filterLanguageForVideo.sizePolicy().hasHeightForWidth())
        self.filterLanguageForVideo.setSizePolicy(sizePolicy)
        self.filterLanguageForVideo.setMinimumSize(QtCore.QSize(100, 0))
        self.filterLanguageForVideo.setObjectName("filterLanguageForVideo")
        self.hboxlayout.addWidget(self.filterLanguageForVideo)
        self.vboxlayout1.addLayout(self.hboxlayout)
        self.splitter = QtGui.QSplitter(self.tab)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.groupBox_folderselect = QtGui.QGroupBox(self.splitter)
        self.groupBox_folderselect.setObjectName("groupBox_folderselect")
        self.vboxlayout2 = QtGui.QVBoxLayout(self.groupBox_folderselect)
        self.vboxlayout2.setObjectName("vboxlayout2")
        self.folderView = QtGui.QTreeView(self.groupBox_folderselect)
        self.folderView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.folderView.setObjectName("folderView")
        self.vboxlayout2.addWidget(self.folderView)
        self.groupBox_videosFound = QtGui.QGroupBox(self.splitter)
        self.groupBox_videosFound.setObjectName("groupBox_videosFound")
        self.hboxlayout1 = QtGui.QHBoxLayout(self.groupBox_videosFound)
        self.hboxlayout1.setObjectName("hboxlayout1")
        self.videoView = QtGui.QTreeView(self.groupBox_videosFound)
        self.videoView.setObjectName("videoView")
        self.hboxlayout1.addWidget(self.videoView)
        self.vboxlayout1.addWidget(self.splitter)
        self.tabs.addTab(self.tab, "")
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setGeometry(QtCore.QRect(0, 0, 756, 496))
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.movieNameText = QtGui.QLineEdit(self.tab_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.movieNameText.sizePolicy().hasHeightForWidth())
        self.movieNameText.setSizePolicy(sizePolicy)
        self.movieNameText.setObjectName("movieNameText")
        self.horizontalLayout.addWidget(self.movieNameText)
        self.buttonSearchByName = QtGui.QPushButton(self.tab_3)
        self.buttonSearchByName.setObjectName("buttonSearchByName")
        self.horizontalLayout.addWidget(self.buttonSearchByName)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        spacerItem1 = QtGui.QSpacerItem(26, 26, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.label_3 = QtGui.QLabel(self.tab_3)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.searchSitesCombo = QtGui.QComboBox(self.tab_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchSitesCombo.sizePolicy().hasHeightForWidth())
        self.searchSitesCombo.setSizePolicy(sizePolicy)
        self.searchSitesCombo.setObjectName("searchSitesCombo")
        self.horizontalLayout_2.addWidget(self.searchSitesCombo)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.hboxlayout2 = QtGui.QHBoxLayout()
        self.hboxlayout2.setObjectName("hboxlayout2")
        spacerItem2 = QtGui.QSpacerItem(581, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout2.addItem(spacerItem2)
        self.label_10 = QtGui.QLabel(self.tab_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setObjectName("label_10")
        self.hboxlayout2.addWidget(self.label_10)
        self.filterLanguageForTitle = QtGui.QComboBox(self.tab_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filterLanguageForTitle.sizePolicy().hasHeightForWidth())
        self.filterLanguageForTitle.setSizePolicy(sizePolicy)
        self.filterLanguageForTitle.setMinimumSize(QtCore.QSize(100, 0))
        self.filterLanguageForTitle.setObjectName("filterLanguageForTitle")
        self.hboxlayout2.addWidget(self.filterLanguageForTitle)
        self.verticalLayout_2.addLayout(self.hboxlayout2)
        self.vboxlayout3 = QtGui.QVBoxLayout()
        self.vboxlayout3.setObjectName("vboxlayout3")
        self.groupBox_4 = QtGui.QGroupBox(self.tab_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setObjectName("groupBox_4")
        self.hboxlayout3 = QtGui.QHBoxLayout(self.groupBox_4)
        self.hboxlayout3.setObjectName("hboxlayout3")
        self.moviesView = QtGui.QTreeView(self.groupBox_4)
        self.moviesView.setObjectName("moviesView")
        self.hboxlayout3.addWidget(self.moviesView)
        self.vboxlayout3.addWidget(self.groupBox_4)
        self.verticalLayout_2.addLayout(self.vboxlayout3)
        self.tabs.addTab(self.tab_3, "")
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setGeometry(QtCore.QRect(0, 0, 756, 496))
        self.tab_4.setObjectName("tab_4")
        self.vboxlayout4 = QtGui.QVBoxLayout(self.tab_4)
        self.vboxlayout4.setObjectName("vboxlayout4")
        self.vboxlayout5 = QtGui.QVBoxLayout()
        self.vboxlayout5.setObjectName("vboxlayout5")
        self.groupBox_2 = QtGui.QGroupBox(self.tab_4)
        self.groupBox_2.setObjectName("groupBox_2")
        self.vboxlayout6 = QtGui.QVBoxLayout(self.groupBox_2)
        self.vboxlayout6.setObjectName("vboxlayout6")
        self.vboxlayout7 = QtGui.QVBoxLayout()
        self.vboxlayout7.setObjectName("vboxlayout7")
        self.hboxlayout4 = QtGui.QHBoxLayout()
        self.hboxlayout4.setObjectName("hboxlayout4")
        self.buttonUploadBrowseFolder = QtGui.QToolButton(self.groupBox_2)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/openfolder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonUploadBrowseFolder.setIcon(icon2)
        self.buttonUploadBrowseFolder.setIconSize(QtCore.QSize(24, 24))
        self.buttonUploadBrowseFolder.setObjectName("buttonUploadBrowseFolder")
        self.hboxlayout4.addWidget(self.buttonUploadBrowseFolder)
        self.line_3 = QtGui.QFrame(self.groupBox_2)
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.hboxlayout4.addWidget(self.line_3)
        self.buttonUploadPlusRow = QtGui.QToolButton(self.groupBox_2)
        self.buttonUploadPlusRow.setEnabled(True)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonUploadPlusRow.setIcon(icon3)
        self.buttonUploadPlusRow.setIconSize(QtCore.QSize(24, 24))
        self.buttonUploadPlusRow.setObjectName("buttonUploadPlusRow")
        self.hboxlayout4.addWidget(self.buttonUploadPlusRow)
        self.buttonUploadMinusRow = QtGui.QToolButton(self.groupBox_2)
        self.buttonUploadMinusRow.setEnabled(False)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/minus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonUploadMinusRow.setIcon(icon4)
        self.buttonUploadMinusRow.setIconSize(QtCore.QSize(24, 24))
        self.buttonUploadMinusRow.setObjectName("buttonUploadMinusRow")
        self.hboxlayout4.addWidget(self.buttonUploadMinusRow)
        self.line_2 = QtGui.QFrame(self.groupBox_2)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.hboxlayout4.addWidget(self.line_2)
        self.buttonUploadUpRow = QtGui.QToolButton(self.groupBox_2)
        self.buttonUploadUpRow.setEnabled(False)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonUploadUpRow.setIcon(icon5)
        self.buttonUploadUpRow.setIconSize(QtCore.QSize(24, 24))
        self.buttonUploadUpRow.setObjectName("buttonUploadUpRow")
        self.hboxlayout4.addWidget(self.buttonUploadUpRow)
        self.buttonUploadDownRow = QtGui.QToolButton(self.groupBox_2)
        self.buttonUploadDownRow.setEnabled(False)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/images/down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonUploadDownRow.setIcon(icon6)
        self.buttonUploadDownRow.setIconSize(QtCore.QSize(24, 24))
        self.buttonUploadDownRow.setObjectName("buttonUploadDownRow")
        self.hboxlayout4.addWidget(self.buttonUploadDownRow)
        spacerItem3 = QtGui.QSpacerItem(401, 33, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout4.addItem(spacerItem3)
        self.buttonUpload = QtGui.QPushButton(self.groupBox_2)
        self.buttonUpload.setEnabled(True)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.buttonUpload.setFont(font)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/images/upload.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonUpload.setIcon(icon7)
        self.buttonUpload.setObjectName("buttonUpload")
        self.hboxlayout4.addWidget(self.buttonUpload)
        self.vboxlayout7.addLayout(self.hboxlayout4)
        self.uploadView = UploadListView(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uploadView.sizePolicy().hasHeightForWidth())
        self.uploadView.setSizePolicy(sizePolicy)
        self.uploadView.setAcceptDrops(True)
        self.uploadView.setDragEnabled(True)
        self.uploadView.setDragDropMode(QtGui.QAbstractItemView.DropOnly)
        self.uploadView.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.uploadView.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.uploadView.setGridStyle(QtCore.Qt.DotLine)
        self.uploadView.setObjectName("uploadView")
        self.vboxlayout7.addWidget(self.uploadView)
        self.vboxlayout6.addLayout(self.vboxlayout7)
        self.line = QtGui.QFrame(self.groupBox_2)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.vboxlayout6.addWidget(self.line)
        self.vboxlayout5.addWidget(self.groupBox_2)
        self.groupBox = QtGui.QGroupBox(self.tab_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(300, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox.setObjectName("groupBox")
        self.gridlayout = QtGui.QGridLayout(self.groupBox)
        self.gridlayout.setObjectName("gridlayout")
        self.label_4 = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMaximumSize(QtCore.QSize(10, 16777215))
        self.label_4.setObjectName("label_4")
        self.gridlayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.label = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridlayout.addWidget(self.label, 0, 1, 1, 1)
        self.uploadIMDB = QtGui.QComboBox(self.groupBox)
        self.uploadIMDB.setObjectName("uploadIMDB")
        self.gridlayout.addWidget(self.uploadIMDB, 0, 2, 1, 1)
        self.buttonUploadFindIMDB = QtGui.QPushButton(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonUploadFindIMDB.sizePolicy().hasHeightForWidth())
        self.buttonUploadFindIMDB.setSizePolicy(sizePolicy)
        self.buttonUploadFindIMDB.setMinimumSize(QtCore.QSize(0, 0))
        self.buttonUploadFindIMDB.setMaximumSize(QtCore.QSize(50, 16777215))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/images/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonUploadFindIMDB.setIcon(icon8)
        self.buttonUploadFindIMDB.setObjectName("buttonUploadFindIMDB")
        self.gridlayout.addWidget(self.buttonUploadFindIMDB, 0, 3, 1, 1)
        self.label_8 = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMaximumSize(QtCore.QSize(10, 16777215))
        self.label_8.setObjectName("label_8")
        self.gridlayout.addWidget(self.label_8, 1, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.gridlayout.addWidget(self.label_5, 1, 1, 1, 1)
        self.uploadLanguages = QtGui.QComboBox(self.groupBox)
        self.uploadLanguages.setObjectName("uploadLanguages")
        self.gridlayout.addWidget(self.uploadLanguages, 1, 2, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.gridlayout.addWidget(self.label_6, 2, 1, 1, 1)
        self.uploadReleaseText = QtGui.QLineEdit(self.groupBox)
        self.uploadReleaseText.setObjectName("uploadReleaseText")
        self.gridlayout.addWidget(self.uploadReleaseText, 2, 2, 1, 1)
        self.label_7 = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName("label_7")
        self.gridlayout.addWidget(self.label_7, 3, 1, 1, 1)
        self.uploadComments = QtGui.QTextEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uploadComments.sizePolicy().hasHeightForWidth())
        self.uploadComments.setSizePolicy(sizePolicy)
        self.uploadComments.setMaximumSize(QtCore.QSize(16777215, 100))
        self.uploadComments.setObjectName("uploadComments")
        self.gridlayout.addWidget(self.uploadComments, 3, 2, 1, 1)
        self.vboxlayout5.addWidget(self.groupBox)
        self.vboxlayout4.addLayout(self.vboxlayout5)
        self.tabs.addTab(self.tab_4, "")
        self.vboxlayout.addWidget(self.tabs)
        self.verticalLayout.addLayout(self.vboxlayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setGeometry(QtCore.QRect(0, 569, 780, 24))
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 780, 24))
        self.menuBar.setObjectName("menuBar")
        self.menuMain = QtGui.QMenu(self.menuBar)
        self.menuMain.setObjectName("menuMain")
        self.menuOptions = QtGui.QMenu(self.menuBar)
        self.menuOptions.setObjectName("menuOptions")
        self.menu_Help = QtGui.QMenu(self.menuBar)
        self.menu_Help.setObjectName("menu_Help")
        MainWindow.setMenuBar(self.menuBar)
        self.action_Quit = QtGui.QAction(MainWindow)
        self.action_Quit.setObjectName("action_Quit")
        self.action_HelpHomepage = QtGui.QAction(MainWindow)
        self.action_HelpHomepage.setObjectName("action_HelpHomepage")
        self.action_HelpAbout = QtGui.QAction(MainWindow)
        self.action_HelpAbout.setObjectName("action_HelpAbout")
        self.action_HelpBug = QtGui.QAction(MainWindow)
        self.action_HelpBug.setObjectName("action_HelpBug")
        self.action_HelpDonation = QtGui.QAction(MainWindow)
        self.action_HelpDonation.setObjectName("action_HelpDonation")
        self.action_ShowPreferences = QtGui.QAction(MainWindow)
        self.action_ShowPreferences.setObjectName("action_ShowPreferences")
        self.menuMain.addAction(self.action_Quit)
        self.menuOptions.addAction(self.action_ShowPreferences)
        self.menu_Help.addAction(self.action_HelpHomepage)
        self.menu_Help.addAction(self.action_HelpDonation)
        self.menu_Help.addAction(self.action_HelpBug)
        self.menu_Help.addSeparator()
        self.menu_Help.addAction(self.action_HelpAbout)
        self.menuBar.addAction(self.menuMain.menuAction())
        self.menuBar.addAction(self.menuOptions.menuAction())
        self.menuBar.addAction(self.menu_Help.menuAction())

        self.retranslateUi(MainWindow)
        self.tabs.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "SubDownloader", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonPlay.setText(QtGui.QApplication.translate("MainWindow", "Play", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonDownload.setText(QtGui.QApplication.translate("MainWindow", "Download", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonIMDB.setText(QtGui.QApplication.translate("MainWindow", "Movie Info", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("MainWindow", "Show :", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_folderselect.setTitle(QtGui.QApplication.translate("MainWindow", "Select Folder:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_videosFound.setTitle(QtGui.QApplication.translate("MainWindow", "Videos found:", None, QtGui.QApplication.UnicodeUTF8))
        self.tabs.setTabText(self.tabs.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Search from Video file(s)", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonSearchByName.setText(QtGui.QApplication.translate("MainWindow", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Search in: ", None, QtGui.QApplication.UnicodeUTF8))
        self.searchSitesCombo.addItem(QtGui.QApplication.translate("MainWindow", "OpenSubtitles.org", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("MainWindow", "Show :", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("MainWindow", "Subtitles found:", None, QtGui.QApplication.UnicodeUTF8))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_3), QtGui.QApplication.translate("MainWindow", "Search by Movie Name", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("MainWindow", "Select Folder with Videos / Subtitles: ", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonUploadBrowseFolder.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonUploadPlusRow.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonUploadMinusRow.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonUploadUpRow.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonUploadDownRow.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonUpload.setText(QtGui.QApplication.translate("MainWindow", "Upload", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Details", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#ff0000;\">*</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "IMDB: ", None, QtGui.QApplication.UnicodeUTF8))
        self.uploadIMDB.addItem(QtGui.QApplication.translate("MainWindow", "Click on FIND button to choose the IMDB link", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonUploadFindIMDB.setText(QtGui.QApplication.translate("MainWindow", "Find", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#ff0000;\">*</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Language:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Release:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "Comments:", None, QtGui.QApplication.UnicodeUTF8))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_4), QtGui.QApplication.translate("MainWindow", "Upload subtitles", None, QtGui.QApplication.UnicodeUTF8))
        self.menuMain.setTitle(QtGui.QApplication.translate("MainWindow", "&Main", None, QtGui.QApplication.UnicodeUTF8))
        self.menuOptions.setTitle(QtGui.QApplication.translate("MainWindow", "&Tools", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Help.setTitle(QtGui.QApplication.translate("MainWindow", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Quit.setText(QtGui.QApplication.translate("MainWindow", "&Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.action_HelpHomepage.setText(QtGui.QApplication.translate("MainWindow", "Visit our &Site", None, QtGui.QApplication.UnicodeUTF8))
        self.action_HelpAbout.setText(QtGui.QApplication.translate("MainWindow", "&About Subdownloader", None, QtGui.QApplication.UnicodeUTF8))
        self.action_HelpBug.setText(QtGui.QApplication.translate("MainWindow", "I found a &bug/error", None, QtGui.QApplication.UnicodeUTF8))
        self.action_HelpDonation.setText(QtGui.QApplication.translate("MainWindow", "Make a &Donation", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ShowPreferences.setText(QtGui.QApplication.translate("MainWindow", "&Preferences", None, QtGui.QApplication.UnicodeUTF8))

from uploadlistview import UploadListView
import images_rc
