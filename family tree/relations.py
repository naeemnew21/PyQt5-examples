# relations
'''
    this script has tools that help you search in the tree
    anf get relationships of elements and coustomize search
'''


def pick_son(tree , node) :
        if node.son == {} :
            return 
        for i in node.son :
            yield i
        for i in node.son :
            yield from pick_son(tree , tree[i])

class scan :
    def __init__(self , tree  , branch ) :
        '''
            tree : list() of human
            branch : object of human
        '''
        self.Tree = tree
        self.node = branch

    def pick(self , name) :
        'name : str'
        name = name.split(' ')
        n = len(name)
        c = []
        for i in self.pick_son(self.node) :
            if  name[::-1] == self.Tree[i].name[-n:] :
                c.append(self.Tree[i].full_self_name)
        return c

    def info(self) :
        order = self.node.order
        index = self.node.self_name
        gender = self.node.self_name
        return order , index , gender
    
    def pick_son(self , node) :
        yield node.self_name
        if node.son == {} :
            return 
        for i in node.son :
            yield from self.pick_son(self.Tree[i])

