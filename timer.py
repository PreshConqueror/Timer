# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'timer.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(391, 300)
        self.set_time = QtWidgets.QPushButton(Dialog)
        self.set_time.setGeometry(QtCore.QRect(120, 50, 131, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.set_time.setFont(font)
        self.set_time.setObjectName("set_time")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 180, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.start = QtWidgets.QPushButton(Dialog)
        self.start.setGeometry(QtCore.QRect(40, 180, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.start.setFont(font)
        self.start.setObjectName("start")
        self.reset = QtWidgets.QPushButton(Dialog)
        self.reset.setGeometry(QtCore.QRect(250, 180, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reset.setFont(font)
        self.reset.setObjectName("reset")
        self.timer = QtWidgets.QLabel(Dialog)
        self.timer.setGeometry(QtCore.QRect(110, 90, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.timer.setFont(font)
        self.timer.setFrameShape(QtWidgets.QFrame.Box)
        self.timer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.timer.setLineWidth(5)
        self.timer.setTextFormat(QtCore.Qt.RichText)
        self.timer.setObjectName("timer")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(0, -5, 391, 311))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../../../../Pictures/Camera Roll/funsplash.jpg"))
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.set_time.raise_()
        self.pushButton_2.raise_()
        self.start.raise_()
        self.reset.raise_()
        self.timer.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.set_time.setText(_translate("Dialog", "set time"))
        self.pushButton_2.setText(_translate("Dialog", "Pause"))
        self.start.setText(_translate("Dialog", "Start"))
        self.reset.setText(_translate("Dialog", "Reset"))
        self.timer.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; color:#ff0000;\">TIMER</span></p></body></html>"))

