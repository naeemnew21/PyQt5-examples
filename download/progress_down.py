import os
import pafy
import humanize
from PyQt5.QtCore import *
import time
from threading import Thread
import glob



def video_info(video_link):
    try :
        v = pafy.new(video_link)
        st = v.streams
        quality_list = []
        t = v.title
        try :
            all_info = [v.title ,v.duration,'',v.author, v.viewcount , v.likes , v.dislikes
                ,'' ,v.thumb , v.bigthumb , v.bigthumbhd ,v.videoid]
        except :
            all_info = ['','','','','','','','','' ,'' ,'','']
        for s in st :
            size = humanize.naturalsize(s.get_filesize())
            data = str(s.mediatype) +"  "+ str(s.extension) +"  "+ str(s.quality) + "  "+str(size )
            quality_list.append(data)
        return (quality_list , t , all_info)
    except :
        return ()




class down_pro_thread(QThread):
    def __init__(self,parent = None,vid_add = '' , save_dir = '' , quality = 0):
        super(down_pro_thread, self).__init__(parent)
        self.my_pro = 'downloading'
        self.select = 'select'
        
        self.vid_lin = vid_add
        self.sav_director = save_dir
        self.qual = quality

        self.v = pafy.new(self.vid_lin)
        self.st = self.v.streams
        self.sav_loc = self.director(save_dir, '{}.{}'.format(self.v.title , self.st[self.qual].extension))
        self.new_title = self.sav_loc.replace(self.sav_director, '').split('.')[0].lstrip('\\')

        Thread(target=self.down , args=()).start()
        Thread(target=self.ch, args=()).start()

    trigger = pyqtSignal(tuple)
    def callback(self, *args):
        print(args)
        my_progress_bar = self.st[self.qual].my_progress #(bytesdone , speed , eta , total)

        status = ('0' , '0' , '0' , 0)

        self.trigger.emit(status)


    finish = pyqtSignal(str)
    def down(self):
            #try :
            D = self.st[self.qual].download(self.sav_loc, callback=self.callback)
            if (D.endswith('.temp')) and (self.select == 'cancel') :
                self.finish.emit('cancel')
                self.my_pro = False
            elif (D.endswith('.temp')) and (self.select == 'exit') :
                self.finish.emit('exit')
                self.my_pro = False
            else :
                self.finish.emit('done')
                self.my_pro = True
            #except :
            #self.finish.emit('failed')
            #self.my_pro = False

    def cancel_down(self , select):
        self.select = select
        self.st[self.qual]._active = False


    #to change video name if the same name exists in the directort
    def director(self , location , title , counter = 0):
        os.chdir(location)
        files = glob.glob(title) + glob.glob(title+'.temp')

        if len(files) == 0 :
            return r'{}\{}'.format(location , title)
        if len(files) > 0 :
            counter += 1
            return self.director(location, '({})'.format(counter)+title , counter)




