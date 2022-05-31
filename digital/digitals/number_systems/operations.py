# do calculations on numbers in different systems
from digitals.number_systems.NumberSystems import convert

class operate :
    def __init__(self , num1 , num2 , sign  , base ) : # num1,2 : int or string
        self.num1 = str(num1)
        self.num2 = str(num2)
        self.sign = sign # sign operation ex: +, -, *, /, //, %, **
        self.base = base
        self.checked = convert().check_base(self.base)
        for i in (self.num1.replace('-','') , self.num2.replace('-','')) :
            for j in i :
                if j not in self.checked:
                    raise TypeError("'{}' Base Error".format(j))
                    

    def solve(self) :
        num1 = self.convert_2dec(self.num1)
        num2 = self.convert_2dec(self.num2)
        if self.sign == '+' :
            n = num1+num2
            return self.convert_2num(n)
        elif self.sign == '-' :
            n = num1-num2
            return self.convert_2num(n)
        elif self.sign == '*' :
            n = num1*num2
            return self.convert_2num(n)
        elif self.sign == '/' :
            if num2 == 0 :
                raise TypeError("ZeroDivisionError: division by zero")
            n = num1/num2
            return self.convert_2num(n)
        elif self.sign == '//' :
            if num2 == 0 :
                raise TypeError("ZeroDivisionError: division by zero")
            n = num1//num2
            return self.convert_2num(n)
        elif self.sign == '**' :
            n = num1**num2
            return self.convert_2num(n)
        elif self.sign == '%' :
            if num2 == 0 :
                raise TypeError("ZeroDivisionError: division by zero")
            n = num1%num2
            return self.convert_2num(n)
        else :
            raise TypeError("OperatorError: '{}' not valid".format(self.sign))

        
    def convert_2dec(self , num) : #num in any system
        sign = self.sign_filter(num)
        n = convert(str(num).replace('-','') , self.base , 10 ).calc()  #str
        return float(n)*sign  # return num in decimal system with sign

    def convert_2num(self , num) : # num in decimal system
        sign = self.sign_filter(num)
        n = convert(str(num).replace('-','') , 10 , self.base ).calc()  #str
        if sign == -1:
            n = '-'+n
        return n
    

    def sign_filter(self , num) :
        if str(num)[0] == '-' :
            return -1 # negative
        return 1 # positive
        

