# this class convert sympols to 0,1 and 0,1 to sympols
'''
encode('a') >>> '1100001'
decode('1100001') >>> 'a'
'''

class alpha_numeric_code:
    def __init__(self, code , encrypt_index) :
        self.code = code
        self.encrypt = encrypt_index  # ascii_code =7 or 8, unicode = 16 ...
        self.num_alpha = {}  # {'1100001':'a' , ...}
        self.alpha_num = {}  # {'a':'1100001' , ...}
        self.initial()

    ''' to fill alpha_decode and alpha_encode'''
    def initial(self) :
        num = (2**self.encrypt)-1
        for i in range(num) :
            ch = chr(i)
            bin_num = bin(i)[2:].rjust(self.encrypt,'0')
            self.num_alpha[bin_num] = ch
            self.alpha_num[ch] = bin_num

    def alpha2num(self) :
        bin_code = ''
        for i in self.code :
            bin_code += self.alpha_num.setdefault(i , '?')
        return bin_code

    def num2alpha(self) :
        word = ''
        for i in range(0,len(self.code), self.encrypt) :
            word += self.num_alpha.setdefault(self.code[i:i+self.encrypt] , '?')
        return word
