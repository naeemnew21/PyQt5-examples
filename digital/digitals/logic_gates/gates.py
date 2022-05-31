# enter combination of input to get output

class get_logic :
    def __init__(self , select_iter = 7 ,*inputs):  # select_iter to save time in iterable when use the class for particular gates
        self.inputs = inputs
        self.select_iter = select_iter

    '''generator for output of all gates'''
    def __iter__(self) :
        if self.inputs == ():
            return None
        if self.select_iter == 7 :
            for i in (self.AND_list(*self.inputs) , self.OR_list(*self.inputs) , self.NAND_list(*self.inputs) , self.NOR_list(*self.inputs) , self.XOR_list(*self.inputs) , self.XNOR_list(*self.inputs)) :
                yield i
        elif self.select_iter == 4 :
            for i in (self.AND_list(*self.inputs) , self.OR_list(*self.inputs) , self.XOR_list(*self.inputs) ) :
                yield i  
        elif self.select_iter == 3 :
            for i in (self.AND_list(*self.inputs) , self.OR_list(*self.inputs) ) :
                yield i
        else :
            for i in ( self.NAND_list(*self.inputs) , self.NOR_list(*self.inputs) ) :
                yield i
        #for i in self.inputs :
        #   yield self.NOT_list(i)

    ''' set inputs values as lists like a , b , c... : a = [0,0,1,1]... '''
    def set_inputs(self , *args) :
        self.inputs = args

    @property
    def get_inputs(self) :
        return self.inputs

    
    ''' gates' input is elements not list
         like (0,1,0,1)
         not ([0,1,0,1], [0,0,1,1])
    '''
    def NOT(self , a) :
        if a :
            return 0
        return 1
    
    def AND(self , *args) :
        if 0 in args :
            return 0
        return 1

    def OR(self , *args) :
        if 1 in args :
            return 1
        return 0

    def NAND(self , *args) :
        if 0 in args :
            return 1
        return 0

    def NOR(self , *args) :
        if 1 in args :
            return 0
        return 1

    def XOR(self , *args) :
        return  self.NAND(*args)&self.OR(*args)

    def XNOR(self , *args) :
        return  int(not(self.NAND(*args)&self.OR(*args)))
    

    ''' gates' input is list not list elements
         like ([0,1,0,1], [0,0,1,1])
         not (0,1,0,1)
    '''
    def NOT_list(self , a) :
        return [ int(not(i)) for i in a ]
    
    def AND_list(self , *args) :
        out = []
        for i in zip(*args) :
            out.append(self.AND( *i ))
        return out

    def OR_list(self , *args) :
        out = []
        for i in zip(*args) :
            out.append(self.OR( *i ))
        return out

    def NAND_list(self , *args) :
        out = []
        for i in zip(*args) :
            out.append(self.NAND( *i ))
        return out

    def NOR_list(self , *args) :
        out = []
        for i in zip(*args) :
            out.append(self.NOR( *i ))
        return out

    def XOR_list(self , *args) :
        out = []
        for i in zip(*args) :
            out.append(self.XOR( *i ))
        return out
    
    def XNOR_list(self , *args) :
        out = []
        for i in zip(*args) :
            out.append(self.XNOR( *i ))
        return out

class get_alpha(get_logic) :
    #generator
    def __iter__(self) :
        if self.inputs == ():
            return None
        if self.select_iter == 7 :
            for i in (self.A_AND(*self.inputs) , self.A_OR(*self.inputs) , self.A_NAND(*self.inputs) , self.A_NOR(*self.inputs) , self.A_XOR(*self.inputs) , self.A_XNOR(*self.inputs)) :
                yield i
        elif self.select_iter == 4 :
            for i in (self.A_AND(*self.inputs) , self.A_OR(*self.inputs) , self.A_XOR(*self.inputs) ) :
                yield i
        elif self.select_iter == 3 :
            for i in (self.A_AND(*self.inputs) , self.A_OR(*self.inputs) ) :
                yield i
        else :
            for i in ( self.A_NAND(*self.inputs) , self.A_NOR(*self.inputs) ) :
                yield i
    ''' gates' input is variables like (a,b,c,...)
         output is : a&b,....
         help you to trace the solution
    '''
    def A_NOT(self, my_input):
        return '(!{})'.format(my_input)
    
    def A_AND(self,*args):
        result = ''
        for i in args :
            result += i
        result = '(&' + result + ')'
        return result

    def A_OR(self,*args):
        result = ''
        for i in args :
            result += i
        result = '(|' + result + ')'
        return result

    def A_XOR(self,*args):
        result = ''
        for i in args :
            result += i
        result = '(+' + result + ')'
        return result

    def A_NAND(self,*args):
        result = ''
        for i in args :
            result += i
        result = '($' + result + ')'
        return result

    def A_NOR(self,*args):
        result = ''
        for i in args :
            result += i
        result = '(=' + result + ')'
        return result

    def A_XNOR(self,*args):
        result = ''
        for i in args :
            result += i
        result = '(#' + result + ')'
        return result
