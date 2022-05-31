# Inheritance

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import WandR

'''
    inheritance class and functions
'''
        
class human:
    '''
       this class is a tree
       parent > child
       name : name of person
       self_object : name of variable(child) as a string
       parent : object that inherit from
       gender : bool - True(male) or False(female)
    '''
    def __init__(self , name  , self_name , gender = True , parent = None) :
        if parent == None :
            self.parent = None
            self.name = [name]
            self.self_name = self_name
            self.full_self_name = [self_name]
            self.gender = gender
            self.order = 0
            self.son = dict()
            'draw'
            self.get_width = 1
              
        else :
            self.parent = parent
            self.parent.son[self_name] = name

            self.name = parent.name[:]
            self.name.append(name)
            self.self_name = self_name
            self.full_self_name = self.parent.full_self_name[:]
            self.full_self_name.append(self_name)

            self.gender = gender
            self.order = self.parent.order + 1

            self.son = dict()

            'draw'
            self.get_width = 1
            self.parent.get_width = 0
            
    def __str__(self) :
        return ''.join(i+' ' for i in self.name[::-1])

    def get_child_index(self , name) :
        for i in self.son :
            if self.son[i] == name :
                return i
    def get_full_name(self) :
        return ''.join(i+' ' for i in self.name[::-1])

    def throw_width(self) :
        if self.parent == None :
            return
        if len(self.son) > 1 :
            self.get_width += 1
        self.parent.get_width += self.get_width

    def get_brother_order(self) :
        if self.parent == None :
            order = [0]
        else :
            order = list(self.parent.son)
            order.sort()
        return order , order.index(self.self_name)

    def get_son_order(self) :
        if len(self.son) == 0 :
            order = [0]
        else :
            order = list(self.son)
            order.sort()
        return order
        
        
        
    
def create_tree():
    'evalute x_list to apply inheritance'
    lis = WandR.x_list()   # return list() - import WandR
    Tree = []   # [human(name , index , gender ,Tree(parent))]
    for i in lis :
        Tree.append(eval(i))
    return Tree

    
def create_btns(x , window , execute) :
    '''create buttons for everyone in the tree(x)
        x : self.Tree >>> eval(x_list)
        window : that carry the buttons
    '''
    c = []
    for i,n in zip(x, range(len(x))) :
        try :
            c.append(QPushButton(i.name[-1], window ))
            c[n].setObjectName('{}'.format(str(n)))
            c[n].released.connect(execute)
            c[n].setVisible(False)
        except :
            c.append(None)
    return c


def add_btn(name , window , objectName , execute):
    '''
        name : str
        window : GuiObject
        objectNmae : int
        execute : function()
    '''
    btn = QPushButton(name, window )
    btn.setObjectName('{}'.format(str(objectName)))
    btn.released.connect(execute)
    btn.setVisible(False)
    return btn # QObject

def add_root(name, n , gender , parent , parent_x , window , func ):
    '''
        name : str
        n : int
        gender : bool
        parent : human()
        parent_x : int
        window : QObject
        func : function
    '''
    'add new branch to the Tree '
    new_branch = human(name, n , gender , parent )

    'add new branch to x_list'
    WandR.add_branch(name , n , gender , parent_x)
        
    'add button for new_branch'
    btn = add_btn(name , window , n , func)
    return new_branch , btn







