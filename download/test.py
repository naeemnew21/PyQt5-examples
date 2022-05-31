
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
import os
from os import  path
import pafy
import time
import threading

from PyQt5 import uic

class PopUp_Window(QWidget):
    def __init__(self, parent = None):
        super(PopUp_Window, self).__init__(parent)
        self.parent = parent
        self.accepted = False
        self.accept_button = QPushButton(self , text = 'accept')
        self.accept_button.setGeometry(20,20,100,100)
        self.accept_button.clicked.connect(self.on_accept)

    def on_accept(self):
        self.accepted = True
        self.close()

    def closeEvent(self, event):
        if self.accepted:
            event.accept()
        else:
            event.ignore()


def main():
    app  = QApplication(sys.argv)
    window = PopUp_Window()
    window.show()
    app.exec_()
    #sys.exit(app.exec_())

if __name__ == "__main__":
    main()
