from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
import os
from os import  path
from PyQt5.uic import loadUiType
import pafy
import progress_down
import urllib

FORM_CLASS,_ = loadUiType(path.join(path.dirname(__file__),"load.ui"))


class Threadclass(QThread  ) :
    def __init__(self,parent = None , vid_add = '' , save_dir = '' , quality = 1) :
        super(Threadclass,self).__init__(parent)
        self.vid_link = vid_add
        self.save_location = save_dir
        self.vid_quality = quality


    trigger = pyqtSignal(tuple)
    def run(self ):
        quality = progress_down.video_info(self.vid_link)
        self.trigger.emit(quality)





class mainApp(QWidget , FORM_CLASS) :
    def __init__(self,parent = None) :
        super(mainApp,self).__init__(parent)
        QWidget.__init__(self)
        self.setupUi(self)
        self.gui()
        self.Handle_Buttons()
        self.btn_down_1.clicked.connect(self.pave_down)
        self.btn_check_1.clicked.connect(self.pave_info)
        self.menu = QMenu()
        self.exit_event = self.menu.addAction('exit')
        self.tray_icon = QSystemTrayIcon()
        self.tray_icon.setContextMenu(self.menu)
        self.tray_icon.setIcon(QIcon('ar.png'))
        # Restore the window when the tray icon is double clicked.
        self.tray_icon.activated.connect(self.restore_window)
        self.exit_event.triggered.connect(self.close_app)


        self.check_url = ''
        self.video_title = ''
        self.file_info = ''
        self.file_size = ''
        self.cls = ''


    def gui(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        #self.groupBox.hide()
        self.LE_save_1.setPlaceholderText(r'C:\Users\{}\Desktop'.format(os.getlogin()))
        self.LE_url_1.setPlaceholderText('https://www.youtube.com/watch?v=example')
        self.LE_url_1.setToolTip('copy video link here')
        self.cb_quality_1.setToolTip('prss check to get quality')



    def Handle_Buttons(self):
        self.btn_exit.clicked.connect(self.min_tray)
        self.btn_browse_1.clicked.connect(self.save_browse_1)
        self.btn_min.clicked.connect(self.min_taskbar)
        self.btn_adv_1.clicked.connect(self.pave_resize)
        self.btn_cancel_1.clicked.connect(self.connect_cancel)





    def pave_resize(self):
        if self.height() > 600 :
            extra = -210
        else :
            extra = 210
        self.resize_win(extra)

    def resize_win(self , extra):
        self.resize(self.width() , self.height()+ extra)
        self.border_left.resize(self.border_left.width() ,self.border_left.height()+extra)
        self.border_right.resize(self.border_right.width() , self.border_right.height()+extra)
        self.frame_left.resize(self.frame_left.width() , self.frame_left.height()+extra)
        self.border_bottom.move(0,self.border_right.height())


    def save_browse_1(self):
        save_place = QFileDialog.getExistingDirectory(self , "Select download directory")
        self.LE_save_1.setText(save_place)

    def progress_1(self,val = (50,50,50,50)):
        #val=(downloaded , speed , eta , percent)
        self.pb_progress_1.setValue(val[3])
        self.lbl_size_1.setText('{}/{}'.format(val[0] , self.file_size))
        self.lbl_speed_1.setText(val[1])
        self.lbl_time_1.setText(val[2])


    def progress_2(self,val):
        self.pb_progress_2.setValue(val)

    def current_video(self , vid_title):
        if len(vid_title) > 30 :
            self.lbl_current_1.setText(vid_title[:30].ljust(34,'.'))
        else:
            self.lbl_current_1.setText(vid_title)
        self.lbl_current_1.setToolTip(vid_title)

    def connect_cancel(self):
        try :
            self.cancel_btn('cancel')
        except :
            pass

    def cancel_btn(self , selection):
        self.progress_1_thread.cancel_down(select = selection)

    def collect_info(self , info):
        #'[title ,duration,published,author, viewcount , likes , dislikes ,description ,thumb,bigthumb,bigthumbhd,id ]'
        self.adv_title.setText(info[0])
        self.adv_dur.setText(' '+info[1])
        self.adv_date.setText(info[2])
        self.adv_author.setText(info[3])
        self.adv_views.setText(str(info[4]))
        self.adv_likes.setText(str(info[5]))
        self.adv_dis.setText(str(info[6]))
        self.adv_des.setText(info[7])
        try :
            self.adv_thumb.setPixmap(self.pic(info[10]))
        except :
            try:
                self.adv_thumb.setPixmap(self.pic(info[9]))
            except :
                try :
                    self.adv_thumb.setPixmap(self.pic(info[8]))
                except :
                    print('link of image : ',info[8])
        #self.adv_profile.setPixmap(self.pic('https://i.ytimg.com/i/{}/1.jpg'.format(info[11])))



    def pic(self , url):
        data = urllib.request.urlopen(url).read()
        pixmap = QPixmap()
        pixmap.loadFromData(data)
        return pixmap

    def pave_info(self):
        self.btn_check_1.setEnabled(False)
        self.btn_down_1.setEnabled(False)
        for i in range(len(self.cb_quality_1)):
            self.cb_quality_1.removeItem(0)

        vid_link = self.LE_url_1.text()
        self.check_url = vid_link #this line to check if the the url you checked is the url you will download
        self.info_thread = Threadclass(vid_add=vid_link)
        self.info_thread.start()
        self.info_thread.trigger.connect(self.get_youtube_info)



    def get_youtube_info(self,quality = ''):
        if quality == None :
            QMessageBox.warning(self, "Download Error", "the check failed")
        elif len(quality) != 0 :
            for i in quality[0] :
                self.cb_quality_1.addItem(i)
            self.file_info = quality[0]
            self.video_title = quality[1]
            self.collect_info(quality[2])
            QMessageBox.information(self, "Download info", "the download is ready to start")
        else :
            self.file_info = ''
            self.video_info = ''
            QMessageBox.warning(self, "Download Error", "the download failed")

        self.btn_check_1.setEnabled(True)
        self.btn_down_1.setEnabled(True)



    def pave_down(self ):
        if self.LE_url_1.text() != self.check_url :
            QMessageBox.warning(self, "Download Error", "please check url again")
            return False
        try :
            self.btn_down_1.setEnabled(False)
            self.btn_check_1.setEnabled(False)
            video_link = self.LE_url_1.text()
            save_location = self.LE_save_1.text() if self.LE_save_1.text() != '' else r'C:\Users\{}\Desktop'.format(os.getlogin())
            quality = self.cb_quality_1.currentIndex()
            self.file_size = self.file_info[quality].split('  ')[3]
            self.lbl_size_1.setText('{}/{}'.format('0',self.file_size))
            self.progress_1_thread = progress_down.down_pro_thread(vid_add = video_link , save_dir = save_location , quality = quality)
            self.progress_1_thread.start()
            self.current_video(self.progress_1_thread.new_title)
            self.progress_1_thread.trigger.connect(self.progress_1)
            self.progress_1_thread.finish.connect(self.finish_Download)

            self.progress_1_thread.exec_()


        except :
            self.finish_Download(False)


    def finish_Download(self, pro):

        if pro == 'done' :
            self.lbl_size_1.setText('{}/{}'.format(self.file_size , self.file_size))
            QMessageBox.information(self, "Download info", "the video downloading finished")
        elif pro == 'cancel' :
            QMessageBox.warning(self, "Download Error", "the download canceled")
        elif pro == 'exit' :
            pass
        else :
            QMessageBox.warning(self, "Download Error", "the download failed")

        self.collect_info(['','','','','','','','',''])
        self.file_size = '0'
        self.progress_1(('0','0','0',0))
        self.lbl_current_1.setText('current video downloading ...')
        self.btn_down_1.setEnabled(True)
        self.btn_check_1.setEnabled(True)


    def Download_playlist(self):
        try:
            playlist_link = self.LE_url_2.text()
            save_location = self.LE_save_2.text() if self.LE_save_2.text()!='' else r'C:\Users\{}\Desktop'.format(os.getlogin())
            playlist = pafy.get_playlist(playlist_link)

            os.chdir(save_location)
            if os.path.exists(str(playlist['title'])) is False :
                os.mkdir(str(playlist['title']))
            os.chdir(str(playlist['title']))

            videos = playlist['items']
            for video in videos :
                v = video['pafy']
                best = v.getbset(preftype  = 'mp4')
                best.download()


            st = v.streams
            quality = self.cb_quality_1.currentIndex()
            down = st[quality].download(save_location)
        except Exception :
            QMessageBox.warning(self, "Download Error", "the download failed")
            return
        QMessageBox.information(self, "Download info", "the video downloading finished")


    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def restore_window(self, reason):
        if reason == QSystemTrayIcon.Critical:
            self.tray_icon.hide()
            # self.showNormal will restore the window even if it was
            # minimized.
            self.showNormal()
        #if reason == QSystemTrayIcon.Context :
        #    self.tray_icon.hide()
        #    self.showNormal()




    def min_taskbar(self):
        self.setWindowState(Qt.WindowMinimized)


    #def min_tray(self):
    #    self.setWindowFlags(self.windowFlags() & ~Qt.Tool)
    #    self.tray_icon.show()

    def min_tray(self):
        self.tray_icon.show()
        self.hide()


    def close_app(self):
        self.cls = True
        try:
            self.cancel_btn(selection='exit')
        except:
            exit()
        self.close()

    def closeEvent(self, event):
        if self.cls:
            event.accept()









def main():
    app  = QApplication(sys.argv)
    window = mainApp()
    window.minimumSizeHint()
    window.show()
    app.exec_()
    #sys.exit(app.exec_())

if __name__ == "__main__":
    main()
