
from PIL import Image, ImageDraw , ImageFont

from arabic_reshaper import arabic_reshaper  # to write arabic letters right
from bidi.algorithm import get_display  # to display arabic letters from right to left
import time

class Draw_Tree :
    def __init__(self, tree , path  , trick = '' ,block_width = 85 , block_height = 50 , rect_width = 75 , rect_height = 20) :
        self.Tree = tree
        self.path = path
        self.block_width = block_width
        self.block_height = block_height
        self.rect_width = rect_width
        self.rect_height = rect_height
        self.tree_width = self.tree_wave()
        self.class_width = self.width_for_class_mode()[0]
        self.class_height = self.get_height()[0] + 2
        self.up_height = self.get_height()[1] + 1

        self.trick = trick

    def init_img(self) :
        copy_right = 22
        width = self.class_width * self.block_width + self.block_width
        height = self.class_height * self.block_height 

        blank_image = Image.new('RGBA', (width, height + copy_right ), '#aaaaff')
        img_draw = ImageDraw.Draw(blank_image)
        for i,color in zip(range(1, self.class_height , 2) , ['#a2a2f3']*self.class_height) :
            img_draw.rectangle((0 , i*self.block_height , width , i*self.block_height+self.block_height), fill=color)

        'copy right'
        if self.trick == '' :
            right = '   +2001091659454  -{}-'.format(time.asctime())
        else :
            right = self.trick
        
        w,h = img_draw.textsize(right)
        for i in range(0,height + copy_right , h ) :
            for j in range(0 , width , w) :
                img_draw.text((j , i ) , right , fill='#aaaaff')

        font = ImageFont.truetype(r'C://Windows/Fonts/mvboli.ttf', 14)
        sign = '+2001091659454 | {}'.format(time.asctime())
        img_draw.text((5 , height+1 ) , sign , fill='blue' , font=font)
            
        return blank_image , width
        
    def draw_blocks_rtl(self ) :
        try :
            blank_image = self.init_img()[0]
            img_draw = ImageDraw.Draw(blank_image)

            Wth = self.init_img()[1]
            
            for i in self.Tree :
                if i == None :
                    continue
                x , y = self.final_geometry(i)
                img_draw.rectangle((Wth -(x + self.rect_width) , y , Wth - x , y + self.rect_height), fill='#004800')  #550000

                font = ImageFont.truetype(r'C://Windows/Fonts/arialbd.ttf', 16)
                solo_name =  i.name[-1]
                siz = 16
                while img_draw.textsize(solo_name , font=font)[0] > self.rect_width :
                    siz -= 1
                    if siz == 0 :
                        break
                    font = ImageFont.truetype(r'C://Windows/Fonts/arialbd.ttf', siz)
                x_align = (self.rect_width - img_draw.textsize(solo_name , font=font)[0]) / 2
                reshaped_name = arabic_reshaper.reshape( solo_name)
                bidi_name = get_display(reshaped_name)

                img_draw.text((Wth -(x + self.rect_width)+x_align+5 , y) , bidi_name, fill='white' , font = font)
                
                if len(i.son) == 0 :
                    continue
                y0,y1,y2,x0,son_x  = self.line_geometry(i , x , y)
                x0 = Wth - x0

                img_draw.line((x0, y0 , x0 , y1) , fill = 'black' , width = 2)
                img_draw.line((Wth - max(son_x), y1 , Wth - min(son_x) , y1) , fill = 'black' , width = 2)

                for j in son_x :      
                    img_draw.line((Wth - j , y1 , Wth - j , y2) , fill = 'black' , width = 2)
             
                if (i.order == 0) and (len(i.son) > 1):
                    y3 ,y4 , x_terminal , son_x_2 = self.get_xy_for_root()
                    x_terminal = Wth - x_terminal
                    img_draw.line((x_terminal , y1+1 , x0+1  , y1+1) , fill = 'black' , width = 2)
                    img_draw.line((x_terminal , y1 , x_terminal , y3) , fill = 'black' , width = 2)
                    full_low_x = son_x_2[:]
                    full_low_x.append(x_terminal)
                    img_draw.line((Wth - max(full_low_x)  , y3 , Wth - min(full_low_x) , y3) , fill = 'black' , width = 2)
                    
                    for k  in son_x_2:
                        img_draw.line( (Wth - k , y3 ,Wth - k , y4) , fill = 'black' , width = 2)
                    
            blank_image.save(self.path)
            return True
        except :
            return False

    def draw_blocks_ltr(self ) :
        try :
            blank_image = self.init_img()[0]
            img_draw = ImageDraw.Draw(blank_image)
            
            for i in self.Tree :
                if i == None :
                    continue
                x , y = self.final_geometry(i)
                img_draw.rectangle((x , y , x + self.rect_width , y + self.rect_height), fill='#004800')  #550000

                font = ImageFont.truetype(r'C://Windows/Fonts/arialbd.ttf', 16)
                solo_name =  i.name[-1]
                siz = 16
                while img_draw.textsize(solo_name , font=font)[0] > self.rect_width :
                    siz -= 1
                    if siz == 0 :
                        break
                    font = ImageFont.truetype(r'C://Windows/Fonts/arialbd.ttf', siz)
                x_align = (self.rect_width - img_draw.textsize(solo_name , font=font)[0]) / 2
                reshaped_name = arabic_reshaper.reshape( solo_name)
                bidi_name = get_display(reshaped_name)

                img_draw.text((x+x_align+5 , y) , bidi_name, fill='white' , font = font)
                
                if len(i.son) == 0 :
                    continue
                y0,y1,y2,x0,son_x  = self.line_geometry(i , x , y)

                img_draw.line((x0, y0 , x0 , y1) , fill = 'black' , width = 2)
                img_draw.line((min(son_x), y1 , max(son_x) , y1) , fill = 'black' , width = 2)

                for j in son_x :      
                    img_draw.line((j , y1 , j , y2) , fill = 'black' , width = 2)
             
                if (i.order == 0) and (len(i.son) > 1):
                    y3 ,y4 , x_terminal , son_x_2 = self.get_xy_for_root()
                    img_draw.line((x0+1 , y1+1 , x_terminal , y1+1) , fill = 'black' , width = 2)
                    img_draw.line((x_terminal , y1 , x_terminal , y3) , fill = 'black' , width = 2)
                    full_low_x = son_x_2[:]
                    full_low_x.append(x_terminal)
                    img_draw.line((min(full_low_x) , y3 , max(full_low_x) , y3) , fill = 'black' , width = 2)
                    
                    for k  in son_x_2:
                        img_draw.line( (k , y3 , k , y4) , fill = 'black' , width = 2)
                    
            blank_image.save(self.path)
            return True
        except :
            return False


    def tree_wave(self):
        for i in self.Tree[::-1] :
            if i == None :
                continue
            i.throw_width()
        return self.Tree[0].get_width #  int

    def final_geometry(self , branch) :
        y_center = (self.block_height - self.rect_height) // 2
        y = self.get_y_geometry(branch) * self.block_height  + y_center
        x_center = self.get_center(branch)
        x = self.get_x_geometry(branch) * self.block_width + x_center
        return x , y


    def get_x_geometry(self , branch) :
        '''
            branch : object of human
        '''
        c = 0
        path = branch.full_self_name
        for i in path :
            order , index = self.get_brother(i)
            x = self.get_x_geometry_to_parent(order , index )
            c += x
        return c
            
    def get_x_geometry_to_parent(self , order , index):
        '''
            order : list() of indexes
            index : int
        '''
        c = 0
        for i in order[:index]:
            c += self.Tree[i].get_width
        return c

    def get_y_geometry(self , branch) :
        'upper height + height of brnach'
        if  branch.order == 0 :
            return 0
        index = branch.full_self_name[1]
        if index in self.width_for_class_mode()[1] :
            return branch.order
        return self.up_height + branch.order 
    
    def get_center(self , branch) :
        if branch.order == 0 :
            return self.class_width * self.block_width// 2
        av = branch.get_width * self.block_width
        return av//2

    def line_geometry(self , branch , x , y) :
        '''
                     [|||||||||]  _ << y0
                                   -- << y1
                                   _ << y2 
                     [||||||||||]  
        '''
        if branch.order == 0 :
            pass
        y_center = (self.block_height - self.rect_height) // 2
        y0 = y + self.rect_height
        y1 = y0 + y_center
        y2 = y1 + y_center
        'Xs geometry'
        x0 = x + self.rect_width / 2
        'son Xs'
        son = list(branch.son)
        son.sort()
        son_x = []
        if branch.order == 0 :
            son = son[::2]
        for i in son :
            x = self.final_geometry(self.Tree[i])[0]
            son_x.append(x + self.rect_width / 2 )
        return  y0,y1,y2,x0,son_x

    def get_xy_for_root(self) : 
        y3 = (self.up_height+0.5)*self.block_height
        y_center = (self.block_height - self.rect_height) // 2
        y4 = y3 + self.block_height/2 + y_center
        'x for lower class'
        son = list(self.Tree[0].son)
        son.sort()
        'x_terminal'
        x_terminal = (self.block_width - self.rect_width) * 3/4
        'Xs'
        son_x = []
        for i in son[1::2]:
            x = self.final_geometry(self.Tree[i])[0]+ self.rect_width/2
            son_x.append(x)
        return y3 ,y4 , x_terminal , son_x


        
    def width_for_class_mode(self) :
        sons = self.Tree[0].get_son_order()  # sorted
        upper_width = [self.Tree[i].get_width for i in sons[::2]]
        lower_width =  [self.Tree[i].get_width for i in sons[1::2]]
        up = sum( upper_width )
        low = sum( lower_width )
        return max(up , low) , sons[::2] ,  sons[1::2]  # max , upeer , lower

    def get_height(self) :
        up  = self.width_for_class_mode()[1]
        low = self.width_for_class_mode()[2]
        up_order = [max(self.get_grandchild_order(i)) for i in up]
        low_order = [max(self.get_grandchild_order(i)) for i in low]
        if len(up_order) == 0 :
            up_order = [0]
        if len(low_order) == 0 :
            low_order = [0]
        return (max(up_order) + max(low_order)) , max(up_order)


    def get_grandchild_order(self , index) :
        branch = self.Tree[index]
        yield branch.order
        for i in branch.son :
            yield from self.get_grandchild_order(i)

    def get_brother(self, i) :
        up = self.width_for_class_mode()[1]  # sorted
        low = self.width_for_class_mode()[2] # sorted
        if i in up :
            return up , up.index(i)
        if i in low :
            return low, low.index(i)
        order = self.Tree[i].get_brother_order()[0]
        index = self.Tree[i].get_brother_order()[1]
        return order , index
        
        
        
        


        
        






















