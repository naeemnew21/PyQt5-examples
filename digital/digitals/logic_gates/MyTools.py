# help tools for logic gate, comparison and filtering

import math
import string  # to create inputs from string.ascci_letters

''' enter input like [0,0,0,0] then get output like [[0,1,0,1],[0,0,1,1]] ...'''
class fill_tools :
    def __init__(self , len_out = 0 ):
        self.len_out = len_out
        try :
            self.ins = int(math.log(self.len_out , 2)) # number of inputs
        except ValueError :
            self.ins = 0
        
        self.inputs = [[] for i in range(self.ins)] # create list of empty inputs [] [] [] ...
        self.alpha_ins = list() # create list of inputs sympols [a,b,c....]
        self.ins_dic = dict()   # connect inputs with alpha
        
        self.fill_inputs()
        self. alpha_inputs()
        self.connect_ins()

        
    ''' fill inputs like [0,1,0,1] , [0,0,1,1] '''
    def fill_inputs(self) :
        for i in range(1 , self.ins+1) :         # fill inputs one by one a,b,c,....
            for j in range(self.len_out//(2**i)) :  #cycle of (0,1) >>> [0,1] , [0,0,1,1] ....
                for k in range(2**(i-1)) :
                   self.inputs[i-1].append(0)
                for L in range(2**(i-1)) :     
                    self.inputs[i-1].append(1)

    ''' fill inputs like [a , b , c ,.... ] '''
    def alpha_inputs(self) :
        for i,a in zip(range(self.ins) , string.ascii_letters):
            self.alpha_ins.append(a)

    ''' connect inputs like {''a':[0,1,0,1] , 'b':[0,0,1,1] , .......} '''
    def connect_ins(self) :
        for i , j in zip(self.alpha_ins , self.inputs) :
            self.ins_dic[i] = j

    # help you to fill output
    def fill_out(self ) :
        out = []
        print("enter 1 or 0 then '-' then number of addition, 'q' for quit : ")
        while True :
            x = input("len(out) = {}  : ".format(len(out)))
            if x == 'q' :
                return out
            y = x.split('-')
            for i in range(int(y[1])) :
                out.append(int(y[0]))


    # draw truth table
    def truth_table(self , len_out , out = []):
        ttable = ''
        if not(check_tools().check_log(len_out)) :
            raise TypeError("'{}' domain error".format(len_out))
        self.__init__(len_out)
        ''' this loop to print first line : a  b  c .... out'''
        for i in self.ins_dic :
            ttable += i+'       '
        ttable += 'out\n'
        ''' this loop to print remain of truth table'''
        for i in range(len_out) :
            for j in self.ins_dic :
                ttable += str(self.ins_dic[j][i]) +'       '
            if len(out) > 0 :
                ttable += '  '+str(out[i])+'\n'
            else : ttable += '\n'
        return ttable 



class filter_tools :
    def __init__(self , out , inputs , alpha ):
        self.output = out
        self.inputs = inputs
        self.alpha = alpha

    ''' compare inputs with output'''
    def compare_filter(self) :
        if self.output in self.inputs :
            return self.alpha[self.inputs.index(self.output)]  # return letter like a,b,c,...
        return None

    ''' XOR and XNOR filter '''
    def X_filter(self) :
        if 0 in self.output :
            if 1 in self.output :
                return None
            return 'XOR(x,x) : x is one of {}'.format(self.alpha)
        return 'XNOR(x,x) : x is one of {}'.format(self.alpha)
        
        
    ''' get inputs and output then try NOT gate and compare then return result '''
    def NOT_filter(self) :
        out = [ int(not(i)) for i in self.output ]
        if out in self.inputs :
                return 'NOT({})'.format(self.alpha[self.inputs.index(out)]) # c = a,b,c,...
        return None

class check_tools :
    def __init__(self) :
        pass
    
    ''' check if all inputs equal in lenght '''
    def check_len(self , *inputs) :
        if len(inputs) == 0 :
            return True
        lens = []   # [ len(input[0]) , len(input[1]) , ....]
        for i in inputs :
            lens.append(len(i))
        for i in lens :
            if i != lens[0] :
                return False
        return True

    ''' check log for base 2 : log(number , 2)'''
    def check_log(self , n) :
        try :
            LOG = math.log(n , 2)
            if int(LOG) == LOG :
                return True
            return False
        except ValueError:
            return False


    # check particular solution
    ''' to select particular gates or particular numbers of solutions ...etc
        solutons : list of solutions
        particular_solution : particular solution
        exact : if you want to check if 'a&b' in answers as a block not each letter alone
    '''
    def check_particular(self , particular_solution , solutons  , exact = False) :
        for i in solutons :
                if particular_solution in i :
                    return True
                if exact :  
                    continue
                for j in particular_solution : 
                    if j not in i :
                        break
                else :
                    return True

    
