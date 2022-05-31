# convert number in any number system to decimal number
import string

class num_dec:
    def __init__(self , number , base , end_point = 7) : #number: str or int, end_point: numbers after dot(.)
        if base > 62 :
            raise TypeError('base {} not valid'.format(base))
        self.num = str(number) 
        self.base = base
        self.end_point = end_point

    def n2d(self) :
        x = self.num.split('.')
        y = self.n2d_int(x[0])
        if len(x) == 2 :
            y_float = self.n2d_float(x[1])
            y += y_float
        return y        # out : int 

    def n2d_int(self, n) :  #input string
        num = 0
        for i,e in zip(n[::-1] , range(len(n))) :
            x = self.replace_sympol(i)
            y = x*(self.base**e)
            num += y
        return num  # out int

    def n2d_float(self, n) :   #input string
        num = 0
        for i,e in zip(n, range(1 , len(n)+1)) :
            x = self.replace_sympol(i)
            y = x*(self.base**(-e))
            num += y
        return num  # out int

    def replace_sympol(self , sympol) :
        letters = '0123456789'+string.ascii_uppercase + string.ascii_lowercase
        if type(sympol) == str :
            if sympol not in letters :
                raise TypeError('{} not valid'.format(sympol))
            return letters.index(sympol)   # ex :0=0 , 1=1 , ... , A=10 , B=11
        if type(sympol) == int :
            return letters[sympol]  # ex : 0=0 , 10 = A ,...
        


# convert number in decimal to any system
class dec_num(num_dec):
    
    def d2n(self) :
        num = self.num.split('.')
        y = self.d2n_int(int(num[0]))  # calc the int part
        if len(num) == 2 :
            y += '.'+self.d2n_float(float('0.'+num[1]))
        return y  # out : str
        

    def d2n_int(self , num) :  # input: int
        result = ''
        while num > 0 :
            y = num % self.base
            z = self.replace_sympol(y)  # type(z): str
            result = z + result
            num //= self.base
        if result == '' :
            result = '0'
        return result  # output: str
            

    def d2n_float(self , num) : # input: float
        repeat = []  # ex: 0.333333... or 0.252525...
        result = ''
        for i in range(self.end_point) :
            x = num*self.base
            y = self.replace_sympol(int(x))
            result += y   
            if num in repeat :
                break
            repeat.append(num)
            num = float(str(x)[str(x).index('.'):]) # take the float part of number
            if num == 0 :
                break
        return result  # output : str

            
