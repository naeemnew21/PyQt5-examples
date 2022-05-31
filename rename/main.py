
#Created by : Ahmed Naeem
#Email : naeemnew21@gmail.com
#whatsapp : 01091659454

import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import Rename

class MyWidget(QWidget , Rename.Ui_rename):
    '''
    Rename files and folders :

    firset : select path to rename files existed in that path
    second : write the word you want to delete or be replaced
    third : write the alternate word to replace the old or leave it empty to delete
    finally : press rename button to apply changes
    *Note : if you check the box of extension the changes will include the extension
                 like .exe,mp4,....
    '''
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        self.setupUi(self)

        '''default path '''
        self.path = r'C:\Users\{}\Desktop'.format(os.getlogin())
        self.location.setText(self.path)

        '''set normal mode as default '''
        self.label_from.hide()
        self.label_to.hide()
        self.LE_from.hide()
        self.LE_to.hide()

        '''set Model for listView '''
        self.fileModel = QFileSystemModel()
        self.fileModel.setFilter(QDir.NoDotAndDotDot |  QDir.AllEntries )
        self.listView.setModel(self.fileModel)
        self.listView.setRootIndex(self.fileModel.setRootPath(self.path))

        '''assign to selected file in list view '''
        self.selected_file = ''

        '''connect browse button '''
        self.browse.clicked.connect(self.on_browse)
        '''connect rename button '''
        self.rename_btn.clicked.connect(self.on_rename)
        '''connect radio buttons click '''
        self.rb_normal.clicked.connect(self.normal_advanced)
        self.rb_advanced.clicked.connect(self.normal_advanced)

        '''connect click on listView '''
        #self.listView.clicked.connect(self.show_click_select)
        self.listView.selectionModel().selectionChanged.connect(self.show_click_select)
            
        
    '''click on browse button '''
    def on_browse(self, index):
        '''select path '''
        path = str(QFileDialog.getExistingDirectory(self))
        self.path = path
        self.location.setText(path)
        '''show path files on the listView '''
        self.listView.setRootIndex(self.fileModel.setRootPath(path))

    '''click on rename button '''
    def on_rename(self) :
        direct = self.path
        if self.rb_normal.isChecked() :
            if self.All_check.isChecked() : # apply changes to all files
                self.click_normal(direct)
            else :              # apply changes to one file
                self.rename_one(direct)
        else :
            self.click_advanced(direct)
            
    '''click for normal mode
       collect information from :
       *word line edit : x
       *replace line edit : y
       *location line edit : directory
    '''
    def click_normal(self , direct) :
        x = self.word.text()
        y = self.replace.text()
        extension = bool(self.checkBox.checkState())
        try :
            self.rename_list(direct, x, y, extension)
        except :
            pass
        
    '''click for normal mode
       collect information from :
       *from line edit : x
       *to line edit : y
       *replace line edit : z
       *location line edit : directory
       **Note : if x is empty the function will append the replace word
                      after the index of y
    '''
    def click_advanced(self , direct) :
        x = self.LE_from.text()
        try : 
            if x == '' :
                x = None
            else :
                x = int(x) - 1
            y = int(self.LE_to.text()) - 1
            z = self.replace.text()
            self.rename_list_extra(direct , z , y , x)
        except :
            pass
        
        
    '''show and hide objects for particular mode of editting '''
    def normal_advanced(self , n) :
        if self.rb_normal.isChecked() :
            self.label_from.hide()
            self.label_to.hide()
            self.LE_from.hide()
            self.LE_to.hide()
            
            self.label_word.show()
            self.word.show()
            self.checkBox.show()
        
        if self.rb_advanced.isChecked() :
            self.label_word.hide()
            self.word.hide()
            self.checkBox.hide()

            self.label_from.show()
            self.label_to.show()
            self.LE_from.show()
            self.LE_to.show()


    '''adjust the fileName '''
    def new_name(self, filename, x , y , extension) :
        file_name = filename
        '''neglect extension '''
        if (extension == False) and (os.path.isdir(file_name) == False):
            fileEXT = os.path.splitext(file_name)  # (fileName , ext)
            file_name = fileEXT[0].replace(x , y)+fileEXT[1]
        else :
            file_name = file_name.replace(x , y)
            
        return file_name

    '''adjust all filenames in the path '''
    def rename_list(self, direct , x , y , extension = False):
        os.chdir(direct)
        for filename in os.listdir():
            new_filename = self.new_name(filename, x , y , extension)
            os.rename(filename, new_filename)

    '''adjust the name of the selected file in listview '''
    def rename_one(self , direct) :
        os.chdir(direct)
        x = self.word.text()
        y = self.replace.text()
        extension = bool(self.checkBox.checkState())
        new_filename = self.new_name(self.selected_file, x , y , extension)
        try :
            os.rename(self.selected_file, new_filename)
        except :
            pass

    '''adjust the fileName for advanced mode '''    
    def new_name_extra(self , filename , z , y , x ) : # x : start , y:end, z:word , if append : x = None
        file_name = filename
        if x != None:
            file_name = file_name.replace(file_name[ x : y ] , z)
        if x == None :
            file_name = file_name[:y] + z + file_name[y :]
        return file_name
    
    '''adjust all filenames in the path for advanced mode '''
    def rename_list_extra(self , direct , z , y , x = None):
        os.chdir(direct)
        for filename in os.listdir():
            new_filename = self.new_name_extra(filename, z , y , x)
            os.rename(filename, new_filename)

    '''show the name of the file from listView in the word text linwe if clicked '''
    def show_click_select(self , index) :
        '''change directory to file or folder location '''
        os.chdir(self.path)
        extension = bool(self.checkBox.checkState())
        #file_name = self.listView.model().itemData(index)[0] # signal from click
        try : 
            file_name =  index.indexes()[0].data()  # signal from selection
        except :
            file_name = ''
        '''assign to selected fille '''
        self.selected_file = file_name
        '''neglect extension if folders'''
        if (extension == False) and (os.path.isdir(file_name) == False) :
            file_name = os.path.splitext(file_name)[0]
        '''fill word ext line edit '''
        self.word.setText(file_name)
        

        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWidget()
    w.show()
    sys.exit(app.exec_())
