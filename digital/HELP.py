# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\naeem\Desktop\HELP.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HELP(object):
    def setupUi(self, HELP):
        HELP.setObjectName("HELP")
        HELP.resize(1384, 713)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/zo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        HELP.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(HELP)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(HELP)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/icon/help.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.retranslateUi(HELP)
        QtCore.QMetaObject.connectSlotsByName(HELP)

    def retranslateUi(self, HELP):
        _translate = QtCore.QCoreApplication.translate
        HELP.setWindowTitle(_translate("HELP", "Form"))

import photo_rc
