# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Wed Jun 17 16:30:20 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(651, 741)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.ranged_Label = QtGui.QLabel(self.centralwidget)
        self.ranged_Label.setObjectName(_fromUtf8("ranged_Label"))
        self.verticalLayout_2.addWidget(self.ranged_Label)
        self.rangedFrame = QtGui.QFrame(self.centralwidget)
        self.rangedFrame.setObjectName(_fromUtf8("rangedFrame"))
        self.verticalLayout_2.addWidget(self.rangedFrame)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.applyButton = QtGui.QPushButton(self.centralwidget)
        self.applyButton.setObjectName(_fromUtf8("applyButton"))
        self.verticalLayout.addWidget(self.applyButton)
        self.zoomtoButton = QtGui.QPushButton(self.centralwidget)
        self.zoomtoButton.setObjectName(_fromUtf8("zoomtoButton"))
        self.verticalLayout.addWidget(self.zoomtoButton)
        self.onButton = QtGui.QPushButton(self.centralwidget)
        self.onButton.setObjectName(_fromUtf8("onButton"))
        self.verticalLayout.addWidget(self.onButton)
        self.deleteButton = QtGui.QPushButton(self.centralwidget)
        self.deleteButton.setObjectName(_fromUtf8("deleteButton"))
        self.verticalLayout.addWidget(self.deleteButton)
        self.removeButton = QtGui.QPushButton(self.centralwidget)
        self.removeButton.setObjectName(_fromUtf8("removeButton"))
        self.verticalLayout.addWidget(self.removeButton)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(4)
        self.horizontalLayout.addWidget(self.tableWidget)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.tab_Tab = QtGui.QTabWidget(self.centralwidget)
        self.tab_Tab.setObjectName(_fromUtf8("tab_Tab"))
        self.peakID_Tab = QtGui.QWidget()
        self.peakID_Tab.setObjectName(_fromUtf8("peakID_Tab"))
        self.runpeakdetectButton = QtGui.QPushButton(self.peakID_Tab)
        self.runpeakdetectButton.setGeometry(QtCore.QRect(400, 30, 151, 61))
        self.runpeakdetectButton.setObjectName(_fromUtf8("runpeakdetectButton"))
        self.layoutWidget = QtGui.QWidget(self.peakID_Tab)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 259, 115))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_5.setMargin(0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_5.addWidget(self.label_3)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.knownelementsLabel = QtGui.QLabel(self.layoutWidget)
        self.knownelementsLabel.setObjectName(_fromUtf8("knownelementsLabel"))
        self.gridLayout_2.addWidget(self.knownelementsLabel, 0, 0, 1, 1)
        self.knownelementsLineEdit = QtGui.QLineEdit(self.layoutWidget)
        self.knownelementsLineEdit.setText(_fromUtf8(""))
        self.knownelementsLineEdit.setObjectName(_fromUtf8("knownelementsLineEdit"))
        self.gridLayout_2.addWidget(self.knownelementsLineEdit, 0, 1, 1, 1)
        self.maxchargestateLabel = QtGui.QLabel(self.layoutWidget)
        self.maxchargestateLabel.setObjectName(_fromUtf8("maxchargestateLabel"))
        self.gridLayout_2.addWidget(self.maxchargestateLabel, 1, 0, 1, 1)
        self.maxchargestateLineEdit = QtGui.QLineEdit(self.layoutWidget)
        self.maxchargestateLineEdit.setObjectName(_fromUtf8("maxchargestateLineEdit"))
        self.gridLayout_2.addWidget(self.maxchargestateLineEdit, 1, 1, 1, 1)
        self.suggestButton = QtGui.QPushButton(self.layoutWidget)
        self.suggestButton.setObjectName(_fromUtf8("suggestButton"))
        self.gridLayout_2.addWidget(self.suggestButton, 2, 1, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout_2)
        self.layoutWidget1 = QtGui.QWidget(self.peakID_Tab)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 170, 388, 91))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.gridLayout_3 = QtGui.QGridLayout(self.layoutWidget1)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.listView = QtGui.QListView(self.layoutWidget1)
        self.listView.setObjectName(_fromUtf8("listView"))
        self.gridLayout_3.addWidget(self.listView, 0, 0, 2, 1)
        self.addionsButton = QtGui.QPushButton(self.layoutWidget1)
        self.addionsButton.setObjectName(_fromUtf8("addionsButton"))
        self.gridLayout_3.addWidget(self.addionsButton, 0, 1, 1, 1)
        self.removeionsButton = QtGui.QPushButton(self.layoutWidget1)
        self.removeionsButton.setObjectName(_fromUtf8("removeionsButton"))
        self.gridLayout_3.addWidget(self.removeionsButton, 1, 1, 1, 1)
        self.tab_Tab.addTab(self.peakID_Tab, _fromUtf8(""))
        self.plots_Tab = QtGui.QWidget()
        self.plots_Tab.setObjectName(_fromUtf8("plots_Tab"))
        self.tab_Tab.addTab(self.plots_Tab, _fromUtf8(""))
        self.advanced_Tab = QtGui.QWidget()
        self.advanced_Tab.setObjectName(_fromUtf8("advanced_Tab"))
        self.manualBox = QtGui.QCheckBox(self.advanced_Tab)
        self.manualBox.setGeometry(QtCore.QRect(20, 30, 131, 18))
        self.manualBox.setObjectName(_fromUtf8("manualBox"))
        self.tab_Tab.addTab(self.advanced_Tab, _fromUtf8(""))
        self.verticalLayout_4.addWidget(self.tab_Tab)
        self.gridLayout.addLayout(self.verticalLayout_4, 0, 1, 2, 1)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.working_Label = QtGui.QLabel(self.centralwidget)
        self.working_Label.setObjectName(_fromUtf8("working_Label"))
        self.verticalLayout_3.addWidget(self.working_Label)
        self.workingFrame = QtGui.QFrame(self.centralwidget)
        self.workingFrame.setObjectName(_fromUtf8("workingFrame"))
        self.verticalLayout_3.addWidget(self.workingFrame)
        self.gridLayout.addLayout(self.verticalLayout_3, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 651, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionNew = QtGui.QAction(MainWindow)
        self.actionNew.setObjectName(_fromUtf8("actionNew"))
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionOpen_Recent = QtGui.QAction(MainWindow)
        self.actionOpen_Recent.setObjectName(_fromUtf8("actionOpen_Recent"))
        self.actionLoad = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../.designer/backup/document_add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLoad.setIcon(icon)
        self.actionLoad.setObjectName(_fromUtf8("actionLoad"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionSave_As = QtGui.QAction(MainWindow)
        self.actionSave_As.setObjectName(_fromUtf8("actionSave_As"))
        self.actionUndo = QtGui.QAction(MainWindow)
        self.actionUndo.setObjectName(_fromUtf8("actionUndo"))
        self.actionREdo = QtGui.QAction(MainWindow)
        self.actionREdo.setObjectName(_fromUtf8("actionREdo"))
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionOpen_Recent)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuHelp.addAction(self.actionAbout)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionREdo)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionLoad)

        self.retranslateUi(MainWindow)
        self.tab_Tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.ranged_Label.setText(_translate("MainWindow", "Ranged", None))
        self.applyButton.setText(_translate("MainWindow", "Apply", None))
        self.applyButton.setShortcut(_translate("MainWindow", "Ctrl+A", None))
        self.zoomtoButton.setText(_translate("MainWindow", "Zoom To", None))
        self.onButton.setText(_translate("MainWindow", "On", None))
        self.deleteButton.setText(_translate("MainWindow", "Delete", None))
        self.removeButton.setText(_translate("MainWindow", "Remove", None))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.runpeakdetectButton.setText(_translate("MainWindow", "Run Peak Detect", None))
        self.label_3.setText(_translate("MainWindow", "Suggest Ions", None))
        self.knownelementsLabel.setText(_translate("MainWindow", "Known Elements", None))
        self.maxchargestateLabel.setText(_translate("MainWindow", "Max Charge State", None))
        self.suggestButton.setText(_translate("MainWindow", "Suggest", None))
        self.addionsButton.setText(_translate("MainWindow", "Add Ions", None))
        self.removeionsButton.setText(_translate("MainWindow", "Remove Ions", None))
        self.tab_Tab.setTabText(self.tab_Tab.indexOf(self.peakID_Tab), _translate("MainWindow", "Peak ID", None))
        self.tab_Tab.setTabText(self.tab_Tab.indexOf(self.plots_Tab), _translate("MainWindow", "Plots", None))
        self.manualBox.setText(_translate("MainWindow", "Manual Override", None))
        self.tab_Tab.setTabText(self.tab_Tab.indexOf(self.advanced_Tab), _translate("MainWindow", "Advanced", None))
        self.working_Label.setText(_translate("MainWindow", "Working", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionNew.setText(_translate("MainWindow", "New...", None))
        self.actionNew.setToolTip(_translate("MainWindow", "Click to create a new project", None))
        self.actionNew.setStatusTip(_translate("MainWindow", "Create a new project", None))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N", None))
        self.actionOpen.setText(_translate("MainWindow", "Open...", None))
        self.actionOpen_Recent.setText(_translate("MainWindow", "Open Recent", None))
        self.actionLoad.setText(_translate("MainWindow", "Load...", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.actionSave.setText(_translate("MainWindow", "Save", None))
        self.actionSave_As.setText(_translate("MainWindow", "Save As...", None))
        self.actionUndo.setText(_translate("MainWindow", "Undo", None))
        self.actionREdo.setText(_translate("MainWindow", "Redo", None))

