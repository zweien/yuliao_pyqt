# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\work\yuliao_pyqt\yuliao_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(950, 703)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_gen = QtWidgets.QHBoxLayout()
        self.horizontalLayout_gen.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_gen.setSpacing(0)
        self.horizontalLayout_gen.setObjectName("horizontalLayout_gen")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_gen.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_gen.addWidget(self.lineEdit)
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout_gen.addWidget(self.toolButton)
        spacerItem = QtWidgets.QSpacerItem(50, 0, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_gen.addItem(spacerItem)
        self.pushButton_read = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_read.setObjectName("pushButton_read")
        self.horizontalLayout_gen.addWidget(self.pushButton_read)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_gen.addItem(spacerItem1)
        self.pushButton_add = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_add.setObjectName("pushButton_add")
        self.horizontalLayout_gen.addWidget(self.pushButton_add)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_gen.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_gen)
        spacerItem3 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout_search = QtWidgets.QHBoxLayout()
        self.horizontalLayout_search.setObjectName("horizontalLayout_search")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_search.addWidget(self.label_2)
        self.lineEdit_search = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_search.setObjectName("lineEdit_search")
        self.horizontalLayout_search.addWidget(self.lineEdit_search)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_search.addWidget(self.label_3)
        self.lineEdit_include = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_include.setText("")
        self.lineEdit_include.setObjectName("lineEdit_include")
        self.horizontalLayout_search.addWidget(self.lineEdit_include)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_search.addWidget(self.label_4)
        self.lineEdit_exclude = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_exclude.setText("")
        self.lineEdit_exclude.setObjectName("lineEdit_exclude")
        self.horizontalLayout_search.addWidget(self.lineEdit_exclude)
        self.pushButton_search = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_search.setObjectName("pushButton_search")
        self.horizontalLayout_search.addWidget(self.pushButton_search)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_search.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_search)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.pushButton_delete = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.horizontalLayout_2.addWidget(self.pushButton_delete)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.pushButton_saveDialog = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_saveDialog.setObjectName("pushButton_saveDialog")
        self.horizontalLayout_2.addWidget(self.pushButton_saveDialog)
        self.label_save_dialog = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_save_dialog.sizePolicy().hasHeightForWidth())
        self.label_save_dialog.setSizePolicy(sizePolicy)
        self.label_save_dialog.setMinimumSize(QtCore.QSize(30, 0))
        self.label_save_dialog.setText("")
        self.label_save_dialog.setObjectName("label_save_dialog")
        self.horizontalLayout_2.addWidget(self.label_save_dialog)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tableWidget.setFont(font)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.verticalHeader().setDefaultSectionSize(60)
        self.horizontalLayout.addWidget(self.tableWidget)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout.addWidget(self.textEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 950, 26))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar1 = QtWidgets.QStatusBar(MainWindow)
        self.statusBar1.setObjectName("statusBar1")
        MainWindow.setStatusBar(self.statusBar1)
        self.actionBbbb = QtWidgets.QAction(MainWindow)
        self.actionBbbb.setObjectName("actionBbbb")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionLoad = QtWidgets.QAction(MainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.actionExcel = QtWidgets.QAction(MainWindow)
        self.actionExcel.setObjectName("actionExcel")
        self.actionStat = QtWidgets.QAction(MainWindow)
        self.actionStat.setObjectName("actionStat")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menu.addAction(self.actionLoad)
        self.menu.addAction(self.actionSave)
        self.menu.addAction(self.actionExcel)
        self.menu.addAction(self.actionStat)
        self.menu.addAction(self.actionAbout)
        self.menu.addSeparator()
        self.menu.addAction(self.actionQuit)
        self.menuBar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "语料库"))
        self.label.setText(_translate("MainWindow", "语料目录"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "语料目录"))
        self.toolButton.setText(_translate("MainWindow", "浏览"))
        self.pushButton_read.setText(_translate("MainWindow", "读取语料"))
        self.pushButton_add.setText(_translate("MainWindow", "追加"))
        self.label_2.setText(_translate("MainWindow", "搜索内容"))
        self.lineEdit_search.setText(_translate("MainWindow", "所以"))
        self.lineEdit_search.setPlaceholderText(_translate("MainWindow", "搜索内容"))
        self.label_3.setText(_translate("MainWindow", "包括国家"))
        self.label_4.setText(_translate("MainWindow", "去除国家"))
        self.pushButton_search.setText(_translate("MainWindow", "搜索"))
        self.pushButton_delete.setText(_translate("MainWindow", "删除(D)"))
        self.pushButton_saveDialog.setText(_translate("MainWindow", "保存修改"))
        self.pushButton.setText(_translate("MainWindow", "退出"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "国家/地区"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "姓名"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "文件名"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "内容"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">对话详细内容</p></body></html>"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.actionBbbb.setText(_translate("MainWindow", "bbbb"))
        self.actionSave.setText(_translate("MainWindow", "保存"))
        self.actionQuit.setText(_translate("MainWindow", "退出"))
        self.actionLoad.setText(_translate("MainWindow", "打开"))
        self.actionExcel.setText(_translate("MainWindow", "搜索结果导出excel"))
        self.actionStat.setText(_translate("MainWindow", "统计"))
        self.actionAbout.setText(_translate("MainWindow", "关于"))
