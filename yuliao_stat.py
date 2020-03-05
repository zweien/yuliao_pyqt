# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\work\yuliao_pyqt\yuliao_stat.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(864, 732)
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(120, 70, 471, 621))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(280, 0, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(600, 100, 201, 80))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_1.setObjectName("label_1")
        self.gridLayout.addWidget(self.label_1, 0, 0, 1, 1)
        self.label_total = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_total.setObjectName("label_total")
        self.gridLayout.addWidget(self.label_total, 0, 1, 1, 1)
        self.label_china = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_china.setObjectName("label_china")
        self.gridLayout.addWidget(self.label_china, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_foreign = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_foreign.setObjectName("label_foreign")
        self.gridLayout.addWidget(self.label_foreign, 2, 1, 1, 1)
        self.pushButtonBar = QtWidgets.QPushButton(Dialog)
        self.pushButtonBar.setGeometry(QtCore.QRect(640, 300, 112, 34))
        self.pushButtonBar.setObjectName("pushButtonBar")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "统计结果"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "国家/地区"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "人数"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "对话字数"))
        self.label.setText(_translate("Dialog", "统计结果"))
        self.label_2.setText(_translate("Dialog", "中国："))
        self.label_1.setText(_translate("Dialog", "总字数："))
        self.label_total.setText(_translate("Dialog", "0"))
        self.label_china.setText(_translate("Dialog", "0"))
        self.label_3.setText(_translate("Dialog", "其它："))
        self.label_foreign.setText(_translate("Dialog", "0"))
        self.pushButtonBar.setText(_translate("Dialog", "柱状图"))
