# codes ex: ones' and twos' complement , gray and bcd codes
from digitals.number_systems.NumberSystems import convert
from digitals.number_systems.operations import operate

class code :
    # all inputs and outputs are string
    def __init__(self , num = '') : # num : string , in ones or twos complement , or in bcd or gray
        if type(num) == int :
            raise TypeError("input must be str not int")
        self.n = num
        

    def ones_comp(self) :
        self.err_bin()
        ones = ''
        rever = {'1':'0' , '0':'1'}
        for i in self.n :   # this loop reverse elements in number if 1,0 replace 0,1
            ones += rever[i]
        return ones  # string

    def twos_comp(self) :
        self.err_bin()
        ones = self.ones_comp()
        twos = operate(ones , 1 , '+' , 2).solve()  # add 1 to ones complement to convert into twos
        return twos.split('.')[0][-len(self.n):]  # string

    def ones_dec(self) :
        self.err_bin()
        return '-'+convert(self.ones_comp() , 2 , 10).calc()

    def twos_dec(self) :
        self.err_bin()
        return '-'+convert(self.twos_comp() , 2 , 10).calc()

    def bin2gray(self):
        '''
           1 >+> 0 >+> 1 >+> 1
           |          |           |          |
           1         1          1         0
        '''
        self.err_bin()
        gray_code = self.n[0]
        for i,c in zip(self.n[1:] , range(1,len(self.n))) :
            op = operate(self.n[c-1] , i , '+' , 2).solve()
            gray_code += op.split('.')[0][-1]
        return gray_code

    def gray2bin(self):   # reverse self.bin2gray()
        self.err_bin()
        bin_code = self.n[0]
        for i,c in zip(self.n[1:] , range(1,len(self.n))) :
            op = operate(bin_code[c-1] , i , '+' , 2).solve()
            bin_code += op.split('.')[0][-1]
        return bin_code  # str

    def gray_dec(self) :
        self.err_bin()
        return convert(self.gray2bin() , 2 , 10).calc()   # str

    def dec2BCD(self) :
        self.err_dec()
        bcd = ''
        for i in self.n :
            bcd += str(bin(int(i)))[2:].rjust(4 , '0')
        return bcd     # str

    def BCD2dec(self) :
        self.err_bin()
        n = self.adjust(self.n)
        dec = ''
        for i in range(0,len(n),4):
            k = convert(n[i:i+4],2,10).calc()
            if int(k) > 9 :
                raise TypeError("'{}' this code not valid in BCD".format(n[i:i+4]))
            dec += k
        return dec

    def add_BCD(self,m,n) :
        self.n = m
        mm = self.BCD2dec()
        self.n = n
        nn = self.BCD2dec()
        result = int(mm)+ int(nn)
        self.n = str(result)
        return self.dec2BCD()

    def adjust(self , n) :
        if (len(n)%4) != 0 :
            adj = ((len(n) //4)*4)+4
            n = n.rjust( adj , '0')
        return n

    def reverse_str(self,n , seq) :
        v = ''
        for i in range(0,len(n) , seq) :
            v = n[i:i+seq] + v
        return v

    def err_bin(self) :
        for i in self.n :
            if i not in '01' :
                raise TypeError("'{}' not valid , only 0 or 1".format(i))
            
    def err_dec(self) :
        for i in self.n :
            if i not in '0123456789' :
                raise TypeError("'{}' not valid , only from 0 to 9".format(i))

    

     

    
