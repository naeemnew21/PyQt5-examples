# tree
# version = 1.5

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import sys
import os

import tree_gui

import WandR
import Inheritance
from Inheritance import human
import HelpS

import MyStyle
import draw_tree
import relations
import interface

            
class myTree(QWidget , tree_gui.Ui_Form) :
    '''
        this class make relations between parents and childs as a tree
        we used it to make a family tree as a special case
    '''
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        
        'change directory'
        WandR.init_loc('family tree')
        
        self.Tree = Inheritance.create_tree() # eval '[human() ,human() , ...]'
        self.btns = Inheritance.create_btns(self.Tree , self.fam_frame , self.info) # create list of btns
        self.current_branch = 0
        self.shown_btns = [[] for i in range(8)]
        self.tree_path = [] # for one member in the tree >> ahmed mohammed ...
        self.search_result = []
        self.search_result_index = 0
        self.layout = 0 # direction from right to left (arabic)
        self.status_text = interface.arabic_status
        
        self.init_tree()

        self.edit_btn.clicked.connect(self.change_name)
        self.add_btn.clicked.connect(self.add_child)
        self.del_btn.clicked.connect(self.del_child)
        self.child_list.clicked.connect(self.child_list_click)
        self.save_btn.clicked.connect(self.save_data)
        self.black_btn.clicked.connect(self.black_style )
        self.green_btn.clicked.connect(self.green_style )
        self.classic_btn.clicked.connect(self.custom_style)
        self.export_btn.clicked.connect(self.drw_tree)
        self.search_btn.clicked.connect(self.name_search)
        self.search_next_btn.clicked.connect(self.next_result)
        self.search_back_btn.clicked.connect(self.back_result)
        self.lang_btn.clicked.connect(self.change_interface)

    def init_tree(self) :
        'interface'
        n = WandR.get_data('def_interface')
        if n == '0' :
            self.layout = 1
            self.change_interface()
        elif n == '1' :
            self.layout = 0
            self.change_interface()
        else :
            pass
        
        'create family parent if None'
        if len(self.Tree) == 0 :
            name = self.status_text[20]
            n = 0
            gender = True
            parent = None
            parent_x = None
            gen = Inheritance.add_root(name , n , gender , parent , parent_x , self.fam_frame , self.info)
            self.Tree.append(gen[0])
            self.btns.append(gen[1])

        'show family button'
        xy = HelpS.get_positions(1 , 0 , 705)
        HelpS.create_order_btns(self.btns[:1] , xy) # show family button
        self.shown_btns[0].append(self.btns[0])# add the button to shown buttons
        self.name_LE.setText(self.Tree[0].name[-1])
        'show children'
        self.child_list.clear()
        children_list = list(self.Tree[0].son.values())
        self.child_list.addItems(children_list)
        'show data'
        data = WandR.get_data(str(self.current_branch))
        self.data_list.setText(data)

        'theme'
        r = WandR.get_data('def_style')
        try :
            if r == 'black' :
                self.black_style()
            elif r == 'green' :
                self.green_style()
            elif r == 'custom' :
                self.custom_style()
        except :
            pass
        

    def info(self):
        'executed when button clicked'
        self.current_branch = int(self.sender().objectName())
        x = self.Tree[self.current_branch]
        'profile'
        self.name_LE.setText(x.name[-1])
        self.full_name.setText(x.get_full_name() +'(' + str(x.order + 1) + ')')
        if x.gender :
            self.gender_label.setText(self.status_text[18])
        else :
            self.gender_label.setText(self.status_text[19])
        son_count = 0
        for i in relations.pick_son(self.Tree , self.Tree[self.current_branch]) :
            son_count += 1
        self.profile_count.setText(str(son_count))
        'children'
        self.child_list.clear()
        children_list = list(x.son.values())
        self.child_list.addItems(children_list)
        'data'
        data = WandR.get_data(str(self.current_branch))
        self.data_list.setText(data)
        'status'
        self.status_show.setText('')
        'draw tree'
        self.show_btns(x.order)
        'paint path'
        both = HelpS.new_path(self.tree_path , x)
        self.tree_path = both[1]
        HelpS.paint_path(self.btns , both[0] , both[1] , MyStyle.btn_style  )
        

    def change_name(self) :
        try :
            index = self.current_branch
            nname = self.name_LE.text()
            
            'change name in x_list'
            WandR.change_name(self.Tree[index].name[-1] ,nname , index)
            
            'change name in self.Tree'
            self.Tree = Inheritance.create_tree()
            
            'change btn name'
            self.btns[index].setText(nname)
            self.status_show.setText(self.status_text[0])
        except :
            self.status_show.setText(self.status_text[1])

    def add_child(self) :
        try :
            index = self.current_branch
            name = self.child_name.text()
            n = len(self.Tree)
            'if gender female'
            if not(self.Tree[index].gender) :
                self.child_list.addItem(self.status_text[2])
                self.status_show.setText(self.status_text[3])
                return
            'if name repeated'
            rep = 0
            parent_sons = list(self.Tree[index].son.values())
            if name in  parent_sons :
                rep = 1
            'if len of branch more than 8'
            if  self.Tree[index].order > 6 :
                self.status_show.setText(self.status_text[4])
                return
            "if len of parent's sons more than 16"
            if len(parent_sons) > 15 :
                self.status_show.setText(self.status_text[5])
                return
            'add child'
            gender = not(bool(self.gender_cb.currentIndex()))
            parent = self.Tree[index]
            parent_x = index
            gen = Inheritance.add_root(name , n ,gender , parent , parent_x , self.fam_frame , self.info)
            self.Tree.append(gen[0])
            self.btns.append(gen[1])
            'click btn to refresh'
            self.btns[index].click()
            if rep == 1 :
                self.status_show.setText(self.status_text[6])
            else :
                self.status_show.setText(self.status_text[7])
                
        except :
            self.status_show.setText(self.status_text[8])


    def del_child(self) :
        try :
            index = self.current_branch
            name = self.child_name.text()
            'if name not exist in parent sons'
            parent_sons = list(self.Tree[index].son.values())
            if name not in  parent_sons :
                self.status_show.setText(self.status_text[9])
                return
            'if son has children'
            child_index = self.Tree[index].get_child_index(name)
            children = self.Tree[child_index].son
            if len(children) > 0 :
                self.status_show.setText(self.status_text[10])
                return
            'delete child'
            self.Tree[child_index] = None  # del the child
            self.Tree[index].son.pop(child_index , False)  #del from parent
            WandR.del_child(child_index) # del from x_list
            self.btns[index].click()  # disappear button
            self.status_show.setText(self.status_text[11])
        except :
            self.status_show.setText(self.status_text[12])

    
    def save_data(self) :
        try :
            data = self.data_list.toPlainText()
            name = self.current_branch
            WandR.save_data(str(name)  , data)
            self.status_show.setText(self.status_text[13])
        except :
            self.status_show.setText(self.status_text[14])


    def show_btns(self , order) :
        '''
            first disappear shown buttons with order less than the clicked button
            then show the sons of the clicked parent
            order : int
        '''
        if order > 7 :
            return
        self.shown_btns = HelpS.disappear(self.shown_btns , order )
        names = self.Tree[self.current_branch].son
        btns = [self.btns[i] for i in names]
        n_btns = len(names)
        if n_btns == 0 :
            return
        xy = HelpS.get_positions(n_btns , order+1 , self.fam_frame.width())
        HelpS.create_order_btns(btns , xy)
        self.shown_btns[order+1].extend(btns)

    def resizeEvent(self, event):
        width = self.fam_frame.width()
        pos = HelpS.get_positions(1,0,width)
        self.btns[0].setGeometry(*pos[0])
        for i in self.tree_path :
            self.btns[i].click()

    def child_list_click(self ):
        item = self.child_list.currentItem()
        name = item.text()
        self.child_name.setText(name)

    def black_style(self ):
        self.setStyleSheet('')
        self.setStyleSheet(MyStyle.black_style)
        WandR.save_data('def_style' , 'black')
            
    def green_style(self):
        self.setStyleSheet('')
        self.setStyleSheet(MyStyle.green_style)
        WandR.save_data('def_style' , 'green')

    def custom_style(self ):
        style = WandR.get_data('style')
        try :
            self.setStyleSheet(style)
            WandR.save_data('def_style' , 'custom')
        except :
            self.status_show.setText(self.status_text[15])

    def drw_tree(self) :
        path = QFileDialog.getSaveFileName(self, "Save Image",
                                       r"C://Users/{}/Desktop/Untitled.png".format(os.getlogin()),
                                       "Images (*.png)")
        direct = path[0]
        ext = path[1]
        if direct == '' :
            self.status_show.setText(self.status_text[17])
            return
        if self.search_LE.text() == 'ahmednaeem1996' :
            trick = self.child_name.text()
        else :
            trick = ''
        x = draw_tree.Draw_Tree( Inheritance.create_tree() ,  direct , trick)
        if self.layout == 0 :
            x.draw_blocks_rtl()
        else :
            x.draw_blocks_ltr()
        self.status_show.setText(self.status_text[16])
        
        
    def name_search(self) :
        self.search_result_index = 0
        name = self.search_LE.text()
        x = relations.scan(self.Tree , self.Tree[self.current_branch])
        self.search_result = x.pick(name)
        n = len(self.search_result)
        self.search_res.setText(str(n))
        'show the first result'
        if n > 0 :
            for i in self.search_result[0] :
                self.btns[i].click()

    def next_result(self) :
        n = len(self.search_result)
        if n == 0 :
            return
        if self.search_result_index == (n-1) :
            return
        self.search_result_index += 1
        for i in self.search_result[self.search_result_index] :
            self.btns[i].click()
    
    def back_result(self) :
        n = len(self.search_result)
        if n == 0 :
            return
        if self.search_result_index == 0 :
            return
        self.search_result_index -= 1
        for i in self.search_result[self.search_result_index] :
            self.btns[i].click()


    def change_interface(self) :
            n = self.layout
            if n == 1 :  #current arabic so translate english
                interface.arabic_interface(self)
                self.status_text = interface.arabic_status
                self.layout = 0
            else :    #current english so translate  arabic
                interface.english_interface(self)
                self.status_text = interface.english_status
                self.layout = 1
            interface.reverse_layout(self , n)
            WandR.save_data('def_interface' , str(self.layout))
            for i in self.tree_path :
                self.btns[i].click()

        
        
                
        
if __name__ == '__main__' :
    app = QApplication(sys.argv)
    window = myTree()
    window.show()
    app.exec_()


