#convert from number system to another
import string
from digitals.number_systems import Dec

class convert:
    def __init__(self , num = None , From = None, To = None , end_point = 7) :# num : int or string
        self.num = str(num)
        self.From = From  # from any system
        self.To = To            # to another system
        self.end_point = end_point
        self.checked = self.check_base(self.From)
        for i in self.num :
            if i not in self.checked :
                raise TypeError("'{}' Base Error".format(i))
        if (self.From == 1) or (self.To == 1) :
            raise TypeError("SystemBase Error")

    def __iter__(self) :
        start = Dec.num_dec(self.num , self.From).n2d()
        for i in range(int(start)+1) :
            yield Dec.dec_num(i , self.To , self.end_point).d2n()

    def calc(self) :
        '''
           first : convert number to decimal system
           then convert result from decimal system to another system
        '''
        start = Dec.num_dec(self.num , self.From).n2d()  # number not string
        return  Dec.dec_num(start , self.To , self.end_point).d2n() # string
        

    def check_base(self , base) :
        sympols = '0123456789'+string.ascii_uppercase+string.ascii_lowercase
        return '.'+sympols[:base]
