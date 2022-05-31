# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\family\احمد نعيم\new\python\projects\rename\python files\Rename - untitled.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_rename(object):
    def setupUi(self, rename):
        rename.setObjectName("rename")
        rename.resize(906, 288)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/ren.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        rename.setWindowIcon(icon)
        rename.setStyleSheet("QWidget {\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QLineEdit {\n"
"     border: 2px solid #3f48cc;\n"
"     background: white;\n"
"    \n"
"    font: 75 14pt \"Arial\";\n"
" }\n"
"\n"
"QLineEdit:hover {\n"
"border-color:rgb(0, 255, 0);\n"
"\n"
"}\n"
"QLabel {\n"
"font: 75 14pt \"Arial\";\n"
"}\n"
"\n"
"QRadioButton {\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton {\n"
"border-color: rgb(50, 0, 250);\n"
"   border-radius: 30px;\n"
"   color: #11FF00;\n"
"   font-family: Arial;\n"
"   font-size: 30px;\n"
"   font-weight: 200;\n"
"\n"
"   background-color: #3200FA;\n"
"\n"
"   text-decoration: none;\n"
"   display: inline-block;\n"
"   cursor: pointer;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   background: #2BAAFF;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(86, 12, 198);}")
        self.gridLayout_3 = QtWidgets.QGridLayout(rename)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame = QtWidgets.QFrame(rename)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.checkBox = QtWidgets.QCheckBox(self.frame)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_2.addWidget(self.checkBox, 2, 5, 1, 1)
        self.LE_from = QtWidgets.QLineEdit(self.frame)
        self.LE_from.setObjectName("LE_from")
        self.gridLayout_2.addWidget(self.LE_from, 3, 1, 1, 2)
        self.word = QtWidgets.QLineEdit(self.frame)
        self.word.setObjectName("word")
        self.gridLayout_2.addWidget(self.word, 2, 1, 1, 4)
        self.replace = QtWidgets.QLineEdit(self.frame)
        self.replace.setObjectName("replace")
        self.gridLayout_2.addWidget(self.replace, 4, 1, 1, 5)
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)
        self.label_word = QtWidgets.QLabel(self.frame)
        self.label_word.setObjectName("label_word")
        self.gridLayout_2.addWidget(self.label_word, 2, 0, 1, 1)
        self.rb_normal = QtWidgets.QRadioButton(self.frame)
        self.rb_normal.setChecked(True)
        self.rb_normal.setObjectName("rb_normal")
        self.gridLayout_2.addWidget(self.rb_normal, 1, 1, 1, 1)
        self.location = QtWidgets.QLineEdit(self.frame)
        self.location.setMinimumSize(QtCore.QSize(350, 0))
        self.location.setObjectName("location")
        self.gridLayout_2.addWidget(self.location, 0, 1, 1, 4)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 4, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.browse = QtWidgets.QPushButton(self.frame)
        self.browse.setMinimumSize(QtCore.QSize(75, 0))
        self.browse.setStyleSheet("font: 75 14pt \"Arial\";\n"
"border: 2px solid rgb(50, 0, 250);")
        self.browse.setObjectName("browse")
        self.gridLayout_2.addWidget(self.browse, 0, 5, 1, 1)
        self.rb_advanced = QtWidgets.QRadioButton(self.frame)
        self.rb_advanced.setObjectName("rb_advanced")
        self.gridLayout_2.addWidget(self.rb_advanced, 1, 2, 1, 1)
        self.label_from = QtWidgets.QLabel(self.frame)
        self.label_from.setObjectName("label_from")
        self.gridLayout_2.addWidget(self.label_from, 3, 0, 1, 1)
        self.LE_to = QtWidgets.QLineEdit(self.frame)
        self.LE_to.setObjectName("LE_to")
        self.gridLayout_2.addWidget(self.LE_to, 3, 4, 1, 2)
        self.label_to = QtWidgets.QLabel(self.frame)
        self.label_to.setObjectName("label_to")
        self.gridLayout_2.addWidget(self.label_to, 3, 3, 1, 1)
        self.contact = QtWidgets.QLabel(self.frame)
        self.contact.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 255);")
        self.contact.setOpenExternalLinks(True)
        self.contact.setObjectName("contact")
        self.gridLayout_2.addWidget(self.contact, 5, 0, 1, 1)
        self.rename_btn = QtWidgets.QPushButton(self.frame)
        self.rename_btn.setMinimumSize(QtCore.QSize(400, 0))
        self.rename_btn.setStyleSheet("border-radius: 10px;")
        self.rename_btn.setObjectName("rename_btn")
        self.gridLayout_2.addWidget(self.rename_btn, 5, 1, 1, 4)
        self.All_check = QtWidgets.QCheckBox(self.frame)
        self.All_check.setObjectName("All_check")
        self.gridLayout_2.addWidget(self.All_check, 5, 5, 1, 1)
        self.location.raise_()
        self.label_4.raise_()
        self.replace.raise_()
        self.label_word.raise_()
        self.browse.raise_()
        self.word.raise_()
        self.label.raise_()
        self.LE_from.raise_()
        self.LE_to.raise_()
        self.label_from.raise_()
        self.label_to.raise_()
        self.label_6.raise_()
        self.rb_normal.raise_()
        self.rename_btn.raise_()
        self.checkBox.raise_()
        self.rb_advanced.raise_()
        self.contact.raise_()
        self.All_check.raise_()
        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(rename)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setObjectName("gridLayout")
        self.listView = QtWidgets.QListView(self.frame_2)
        self.listView.setObjectName("listView")
        self.gridLayout.addWidget(self.listView, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame_2, 0, 3, 1, 1)

        self.retranslateUi(rename)
        QtCore.QMetaObject.connectSlotsByName(rename)
        rename.setTabOrder(self.location, self.browse)
        rename.setTabOrder(self.browse, self.rb_normal)
        rename.setTabOrder(self.rb_normal, self.rb_advanced)
        rename.setTabOrder(self.rb_advanced, self.word)
        rename.setTabOrder(self.word, self.checkBox)
        rename.setTabOrder(self.checkBox, self.LE_from)
        rename.setTabOrder(self.LE_from, self.LE_to)
        rename.setTabOrder(self.LE_to, self.replace)
        rename.setTabOrder(self.replace, self.rename_btn)
        rename.setTabOrder(self.rename_btn, self.listView)

    def retranslateUi(self, rename):
        _translate = QtCore.QCoreApplication.translate
        rename.setWindowTitle(_translate("rename", "Rename"))
        self.checkBox.setText(_translate("rename", "extension"))
        self.label_6.setText(_translate("rename", "Mode : "))
        self.label_word.setText(_translate("rename", "Word      :"))
        self.rb_normal.setText(_translate("rename", "normal"))
        self.label_4.setText(_translate("rename", "Replace :"))
        self.label.setText(_translate("rename", "Location :"))
        self.browse.setText(_translate("rename", "Browse"))
        self.rb_advanced.setText(_translate("rename", "advanced"))
        self.label_from.setText(_translate("rename", "From"))
        self.label_to.setText(_translate("rename", "To : "))
        self.contact.setText(_translate("rename", "<a href=\"https://www.facebook.com/ahmednaeem1996\">Contact</a>"))
        self.rename_btn.setText(_translate("rename", "Rename"))
        self.All_check.setText(_translate("rename", "All"))

import photo_rc
