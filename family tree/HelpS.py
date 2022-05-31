# Help tools
'''
    this script has tools that help you search in the tree
    anf get relationships of elements and coustomize search
'''
def disappear(btns_list , index):
    '''
        make btns invisible and return btns_list without invisible btns
    '''
    for order in btns_list[ index + 1 : ] :
        for btn in order :
            btn.setVisible(False)
    root = btns_list[:index+1]
    root.extend([[] for i in range(index+1 , 8)])
    return root

def get_positions(n_btns , order , width , height = 35 ,  x = 0 , y = 0):
    '''
        return positions of the buttons
        n_btns : number of buttons will be created
        x , y : geometry of the frame that contains buttons
        order : it has been standard from 0 to 8 >> represent order in the tree branches
    '''
    av_area = width // n_btns # avalible area for each button
    btn_width = 6*(av_area//8)
    space = av_area //8

    c = []
    for i in range(n_btns) :
        c.append([i*(btn_width + 2*space) + space , order*70 + 20 , btn_width , height ]) # x, y, width, height
    return c
        

def create_order_btns(btns, positions) :
    '''
        btns : list()
        positions : list() of lists() of int >>> [[int ,int ,int ,int],[],[],...]
    '''
    for i , p in zip(btns , positions) :
        i.setVisible(True)
        i.setGeometry(*p)


def convert_dic(lines , repeat = None) :
    '''
        lines : str >>> name : ahmed\nage : 22\n....'
        repeat : list() or dict()
    '''
    if len(lines) == 0:
        dic = []
    else :
        dic = lines.split('\n')
    if (repeat != None) and (dic != []) :
        for i in repeat :
            if i in dic :
                dic.remove(i)
    return dic  # list()

def new_path(path , branch ) :
    '''
        path : list() of integers
        branch : object of human()
    '''
    order = branch.order
    old = path[order:]
    new = path[: order]
    new.append(branch.self_name)
    return old , new

def paint_path(btns_list , old , new , style) :
    '''
        btns_list : list() of objects of QPushButon
        old : list() of integers
        new : list() of integers
    '''
    for i in old :
        btns_list[i].setStyleSheet('')
    for i in new :
        btns_list[i].setStyleSheet(style)




    











