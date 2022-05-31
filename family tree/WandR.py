#write and read
'''
    this script has classes and functions that save input data
    and read saved data and edit it
'''

import os
from distutils.dir_util import copy_tree

def init_loc(file_name) :
    'check if the file exist or not'
    os.chdir(r'C://Users/{}/AppData/Local'.format(os.getlogin()))
    if os.path.isdir(file_name) == False :
        os.mkdir(file_name)


def save_data(name , data) :
    '''
        name : str
        data : str
    '''
    os.chdir(r'C://Users/{}/AppData/Local/family tree'.format(os.getlogin()))
    f = open(name+'.txt' , 'w')
    f.write(data)
    f.close()

def get_data(name) :
    'name : str '
    os.chdir(r'C://Users/{}/AppData/Local/family tree'.format(os.getlogin()))
    try :
        f = open(name+'.txt' , 'r')
        r = f.read()
    except :
        f = open(name+'.txt' , 'w')
        f.write('')
        f.close()
        r = ''
    return r  # str()

def get_eval_data(name) :
    'name : str '
    os.chdir(r'C://Users/{}/AppData/Local/family tree'.format(os.getlogin()))
    f = open(name+'.txt' , 'r')
    r = f.read()
    return eval(r)  # return dict() or list()


def get_val(name , key) :
    os.chdir(r'C://Users/{}/AppData/Local/family tree'.format(os.getlogin()))
    f = open(name+'.txt' , 'r')
    r = f.read()
    dic = eval(r)
    return dic.get(key , None)


def x_list() :
    os.chdir(r'C://Users/{}/AppData/Local/family tree'.format(os.getlogin()))
    try :
        f = open('x_list.txt' , 'r')
        r = f.read()
        return eval(r)
    except :
        f = open('x_list.txt' , 'w')
        f.write('[]')
        f.close()
        return []


def add_branch(name , n , gender , parent ) :
    '''
        add branch to the tree
        name : str
        n : int - len(tree)
        parent : int
    '''
    os.chdir(r'C://Users/{}/AppData/Local/family tree'.format(os.getlogin()))
    x = get_eval_data('x_list')
    if str(parent) == 'None':
        parent = str(parent)
    else :
        parent = 'Tree[{}]'.format(str(parent))
    branch = "human('{}' , {} , {} , {} )".format(name , str(n) , str(gender) , parent )
    x.append(branch)
    save_data('x_list' , str(x))


def change_name(old , new , n):
    '''
        old : str - old name
        new : str - new name
        n : int
    '''
    os.chdir(r'C://Users/{}/AppData/Local/family tree'.format(os.getlogin()))
    x = get_eval_data('x_list') # eval(x_list) = list()
    x[n] = x[n].replace( "'{}'".format(old) , "'{}'".format(new) )
    save_data('x_list' , str(x))
    

def del_child(index) :
    ' index : int '
    x = get_eval_data('x_list') # eval(x_list) = list()
    x[index] = 'None'
    save_data('x_list' , str(x))
    

def get_str_from_dictVal(dic) :
    'dic : dict() '
    text = ''
    for i in dic.values() :
        text += i+'\n'
    return text

def take_copy(name , dist) :
    '''
        name : str
        dist : str
    '''
    os.chdir(dist)
    os.mkdir(name)
    copy_tree(r'C://Users/{}/AppData/Local/family tree'.format(os.getlogin()) , name )


def load_dir(src) :
    'src : str '
    copy_tree( src , r'C://Users/{}/AppData/Local/family tree'.format(os.getlogin()) )

    
    
    
    
