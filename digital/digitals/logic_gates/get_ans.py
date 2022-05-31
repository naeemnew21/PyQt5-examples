# enter output to get the required logic gates for circuit design
import time
import math
import threading
from itertools import combinations
from digitals.logic_gates.gates import get_logic , get_alpha
from digitals.logic_gates.MyTools import fill_tools , filter_tools , check_tools

class get_gate :
    def __init__(self, *out ):
        if check_tools().check_len(*out) :
            self.out = out
        else :
            raise TypeError('inputs have not the same length')
        
        if len(self.out) == 0 :
            self.len_out = 0 # mean no inputs
        else :
            self.len_out = len(self.out[0]) # length of only one output 
            
        self.pins = [2] # maximum inputs of gate
        self.init_tools =  fill_tools(self.len_out) 
        self.alpha_inputs = self.init_tools.alpha_ins #list of inputs[a,b,c,..]
        self.zo_inputs = self.init_tools.inputs #list of zeros and ones inputs [[0,1],[0,0],.]
        self.ans = [[] for i in out] # solutions , support multi outputs

        self.counter = 0 # to calc percentage in self.calc_percent()
        self.search_finished = False # for signal and slots in pyqt
        self.cycle_len = self.comb_len
        self.cancel = False # for signal and slots in pyqt
        self.cycle_finished = False 
        
        self.first_start()
        



    def __str__(self) :
        return str(self.get_ans)

    def __iter__(self) :
        for i in self.ans :
            yield i

    def set_out(self , *out) :
        self.__init__(*out)
        
    # set number of pins
    def set_pins(self, pins) : # pins = []
        for pin in pins :
            if (len(self.alpha_inputs) ==1) and (pin == 2 ) :
                continue
            if len(self.alpha_inputs) < pin :
                raise TypeError('N of pins must be <= N of inputs but {} > {}'.format(pins , len(self.alpha_inputs)))
        self.pins = pins

    @property
    def get_ans(self) :
        return [len(i) for i in self.ans]
    
    @property
    def get_inputs(self) :
        return (len(self.alpha_inputs) , self.alpha_inputs , self.zo_inputs )
    
    @property
    def get_out(self) :
        return self.out
    
    @property
    def get_solutions(self) :
        return self.ans
    
    @property
    def get_info(self) :
        print('@info; \nfor len of answers : self.get_ans\nfor solutions : self.get_solutions')
        print('for out : self.get_out')
        print('for inputs : self.get_inputs **self.get_inputs[0 or 1 or 2]')
        print('\t0 : len(inputs)\n\t1 : alpha_inputs\n\t2 : zo_inputs''')
        print('to start searching : self.start(wait = 0, num_gates = 7, num_sol = 0, par_sol = None , exact = False)')
        print('number of current inputs : {}'.format(self.get_inputs[0]))
        if self.get_inputs[0] == 0 :
            nc = 0  # number of combinations
        elif self.get_inputs[0] < self.pins :
            return
        else :
            nc = self.comp(self.get_inputs[0], self.pins) + self.get_inputs[0] 
        print('number of combinations for one gate : {}'.format(nc))
    
    
    ''' first filter :
        * add not inputs to main inputs
        * compare all inputs with outputs
        *check if XOR,XNOR gates is used for one input like XOR(a,a)..
    '''
    def first_start(self) :
        for i,c in zip( self.zo_inputs[:] , self.alpha_inputs[:] ) :
            Z = get_logic().NOT_list(i)
            A = get_alpha().A_NOT(c)
            self.zo_inputs.append(Z)
            self.alpha_inputs.append(A)
        for i,c in zip(self.out  , range(len(self.out))):
            filters = filter_tools(i , self.zo_inputs , self.alpha_inputs)
            compare = filters.compare_filter()
            if compare :    # compare inputs with outputs
                self.ans[c].append(compare)
                self.search_finished = True
            X = filters.X_filter( )  # check if xor , xnor gate used
            if X :
                self.ans[c].append(X)
                self.search_finished = True
    
    # main
    '''
       wait :
           *type : int
           *value : in minutes
           *task : if there's no answer in (wait) minutes stop process
        num_gates : shown in self.cycle()
        num_sol : number of solutions
        par_sol : particular solution
    '''
    def start(self , wait = 0 , num_gates = 7 , num_sol = 0, par_sol = None , exact = False ,one_ans =True ) :
        try :
            start_time = time.time()
            answer = threading.Thread(target = self.cycle , args = (num_gates,one_ans)).start()
            while True :
                if (num_gates == 3) or (num_gates == 4):
                    self.not_filter()
                if wait != 0 :
                    if (time.time() - start_time) >= (wait * 60 ) :  # check time out
                        self.search_finished = True
                        break
                if num_sol != 0 :
                    if (num_sol-1) not in self.get_ans : # check len of answers
                        break
                if par_sol != None : # check particular solution
                    if self.particular_sol(par_sol , exact) :
                        break
                if self.cycle_finished :
                    self.cycle_finished = False
                    break       
                if self.cancel : # for signal and slots in pyqt
                    break   
                time.sleep(1)
                
            return self.get_ans
        except :
            raise TypeError("self.start(wait = 0, num_gates = 7, num_sol = 0, par_sol = None , exact = False)#par_sol = 'a&b' , exact : as par_sol")


    # main combinatian function
    ''' input = inputs like (a,b,c...)
        output = new inputs
        out is one solution
        num_gates >> int :
                7:all gates
                4:[NOT,AND,OR ,XOR]
                3:[NOT,AND,OR]
                2:[NAND,NOR]
    '''
    
    def cycle(self , num_gates , one_ans = True) :#for  num_gates look up, one_answer
        self.counter = 0 # to calc self.calc_percent()
        self.cycle_len = self.comb_len
        #print('..........cycle len : ',self.cycle_len)
        #print('...........counter : ',self.counter)
        zo = []
        alpha = []
        for i in self.pins  : # self.pins = [2,3,...]
            for j,k in zip(combinations(self.zo_inputs , i) , combinations(self.alpha_inputs , i) ):
                self.counter += 1
                if self.cancel :
                    return
                for L,c in zip(get_logic(num_gates ,*j) , get_alpha(num_gates ,*k)) :
                    if self.zo_inputs.count(L) == 1 :
                       continue
                    zo.append(L)
                    alpha.append(c)
                    if  L in self.out :
                        self.ans[self.out.index(L)].append(c)                     
                        if one_ans :
                            self.search_finished = True
                            return
                        ''' to stop process if find one solution'''
                        #if 0 not in self.get_ans : # if there's at least one solution return True
                            #return True
            #print('...........counter : ',self.counter)
        self.zo_inputs += zo
        self.alpha_inputs += alpha
        self.cycle_finished = True
                       
    
    ''' NOT filter for multi outputs''' # outputs is inputs for filter
    # used in case of num_gates = 3 or 4  in  : self.solve(num_gates)
    def not_filter(self) :
        for i,c in zip(self.out  , range(len(self.out))):
            filters = filter_tools(i , self.zo_inputs , self.alpha_inputs)
            NO = filters.NOT_filter()
            if NO :
                self.ans[c].append(NO)
                self.search_finished = True

                    
    # combinations calculations
    def comp(self , n  , r  ) :
        if n < r :
            raise TypeError('Expected (n) must be >= r but {} > {}'.format(r,n))
        fact = math.factorial(n) / ( math.factorial(r) *  math.factorial(n-r))
        return int(fact)

    #combinations sum from 1 to (r) for n
    def taw(self, n, r) :
        x = 0
        for i in range(2 , r+1) :
            x += self.comp(n , i)
        return x

    # particular solution
    def particular_sol(self , par_sol , exact) :
        for i in self.ans : # check solutions one by one
            if not(check_tools().check_particular(par_sol , i , exact)) : # if check == True : continue
                ''' this break to go out of for loop beacause one of solutions
                    doesn't  satisfy particular solution
                '''
                break
        else :  # if all solutions satisfy particular solutions
            return True

    # calculate time of cycle
    def calc_time(self,n,r) :
        x = 0
        for i in self.pins :
            x += self.compself.get_inputs[0] , i()   # number of combinations 
        avg = 0.00022016756815469626 # average value from experiments
        time_sec = int(x*avg) # time in seconds
        seconds = time_sec%60
        time_min = time_sec//60 # time in minutes
        minutes = time_min%60
        time_hr = time_min // 60 # time in hours
        hours = time_hr  % 24
        time_dy = time_hr // 24 # time in days
        days = time_dy % 30
        time_mth = time_dy // 30 # time in months
        months = time_mth % 12
        years = time_mth // 12 # time in years
        return seconds,minutes,hours,days,months,years

    #calc time of one process
    def process_time(self) :
        pass

    # calc percentage %, number of operations from all combinations
    @property
    def comb_len(self):
        x = 0
        if self.get_inputs[0] == 1 :
            return 1
        for i in self.pins :
            x += self.comp(self.get_inputs[0] , i)
        return x

    @property
    def get_percent(self) :
        return round((self.counter/self.cycle_len)*100 , 3)

    def repeat_start(self , wait = 0 , num_gates = 7) :
        start_time = time.time()
        timeout = wait
        while True :
            self.start(timeout , num_gates)
            if wait != 0 :
                if (time.time() - start_time ) >= (wait*60) :
                    self.search_finished = True
                    break
                timeout = ((wait*60) - (time.time() - start_time ))//60+1
            if self.search_finished :
                break
            if self.cancel :
                break
            
            
            
        
        
        
        
        
        

    
            



