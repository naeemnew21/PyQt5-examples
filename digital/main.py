from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import time
import sys
import os
import threading
import  Digital
from digitals.number_systems.NumberSystems import convert
from digitals.number_systems.operations import operate
from digitals.number_systems.codes import code
from digitals.alpha_numeric import alpha_numeric_code as anc
from digitals.logic_gates.MyTools import fill_tools
from digitals.logic_gates.get_ans import get_gate

cancelMyThread = False

class MyThreadData(QThread  ) : 
    def __init__(self , out , wait , num_gates , pins ,parent = None) : # pins= [list]
        super(MyThreadData,self).__init__(parent)
        self.out = out
        self.wait = wait
        self.num_gates = num_gates
        self.pins = pins
    
    trigger = pyqtSignal(tuple)
    def run(self ):
        global cancelMyThread
        
        MyGate = get_gate(self.out)
        MyGate.set_pins(self.pins)
        threading.Thread(target = MyGate.repeat_start , args = (self.wait , self.num_gates)).start()
        while MyGate.search_finished == False :
            if cancelMyThread :
                MyGate.cancel = True
                break
            self.trigger.emit((MyGate.get_percent, MyGate.search_finished , MyGate.get_solutions , MyGate.cycle_len , MyGate.counter ))
            #self.trigger.emit((MyGate.get_percent, MyGate.counter , MyGate.cycle_len, MyGate.search_finished , MyGate.get_solutions ))
            time.sleep(0.5)
        self.trigger.emit((MyGate.get_percent , MyGate.search_finished , MyGate.get_solutions , MyGate.cycle_len , MyGate.counter ))
        #self.trigger.emit((MyGate.get_percent , MyGate.counter , MyGate.cycle_len, MyGate.search_finished , MyGate.get_solutions ))

class mainApp(QMainWindow , Digital.Ui_MainWindow) :
    def __init__(self) :
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.fill_base() # to fill combox of base for number systems and simple calculator
        self.ns_btn.clicked.connect(self.convert_click)
        self.lg_zero.clicked.connect(self.zero_out)
        self.lg_one.clicked.connect(self.one_out)
        self.lg_out.textChanged.connect(self.len_out)
        self.lg_del.clicked.connect(self.del_out)
        self.lg_ac.clicked.connect(self.clear_out)

        self.sc_add.clicked.connect(self.calc_plus)
        self.sc_sub.clicked.connect(self.calc_min)
        self.sc_mul.clicked.connect(self.calc_mul)
        self.sc_div.clicked.connect(self.calc_div)
        self.sc_correct.clicked.connect(self.calc_div_correct)
        self.sc_rem.clicked.connect(self.calc_remain)
        self.sc_pow.clicked.connect(self.calc_exp)

        self.sc_base.currentIndexChanged.connect(self.hide_btns)
        self.code_btn.clicked.connect(self.my_codes)

        self.cb_btn.clicked.connect(self.AlphaNumeric)

        self.lg_ttable.clicked.connect(self.ttable_click)
        self.logic_gate_out = ''

        self.lg_start.clicked.connect(self.start_logics)

        self.actionNumber_systems_2.triggered.connect(self.visible_ns)
        self.actionSimple_calculator.triggered.connect(self.visible_sc)
        self.actionCodes.triggered.connect(self.visible_co)
        self.actionConvert_to_binary.triggered.connect(self.visible_an)
        self.actionLogic_gates.triggered.connect(self.visible_lg)
        self.actionExit.triggered.connect(self.close)
        self.actionAboutMe.triggered.connect(self.about_me)

    ''' fill base from 2 to 62 in number systems and simple calculator'''
    def fill_base(self) :
        for i in range(2 , 63) :
            self.ns_from.addItem(str(i))
            self.ns_to.addItem(str(i))
            self.sc_base.addItem(str(i))
        self.sc_base.addItem('Add BCD')
        for i in range(7,17):
            self.cb_base.addItem(str(i))
            
    ''' convert button in number systems'''
    def convert_click(self) :
        number = self.ns_number.text()
        from_base = int(self.ns_from.currentText())
        to_base =  int(self.ns_to.currentText())
        try :
            out = convert(number, from_base, to_base).calc()
            self.ns_out.setText(out)
        except :
            self.ns_out.setText('Error')
            
    ''' initialize inputs for operation in simple calculator'''
    def sim_calc(self) :
        num1 = self.sc_first.text()
        num2 = self.sc_second.text()
        if self.sc_base.currentText() == 'Add BCD' :
            base = 'Add BCD'
        else :
            base = int(self.sc_base.currentText())
        return num1,num2,base

    def calc_plus(self) :
        x = self.sim_calc()
        
        if x[2] == 'Add BCD' :
            try :
                 out = code().add_BCD(x[0],x[1])
                 self.sc_out.setText(out)
            except :
                self.sc_out.setText('Error')
        else :
            try:
                out = operate(x[0], x[1], '+' , x[2]).solve()
                self.sc_out.setText(out)
            except :
                self.sc_out.setText('Error')
            

    def calc_min(self) :
        x = self.sim_calc()
        try:
            out = operate(x[0], x[1], '-' , x[2]).solve()
            self.sc_out.setText(out)
        except :
            self.sc_out.setText('Error')

    def calc_mul(self) :
        x = self.sim_calc()
        try:
            out = operate(x[0], x[1], '*' , x[2]).solve()
            self.sc_out.setText(out)
        except :
            self.sc_out.setText('Error')

    def calc_div(self) :
        x = self.sim_calc()
        try:
            out = operate(x[0], x[1], '/' , x[2]).solve()
            self.sc_out.setText(out)
        except :
            self.sc_out.setText('Error')

    def calc_div_correct(self) :
        x = self.sim_calc()
        try:
            out = operate(x[0], x[1], '//' , x[2]).solve()
            self.sc_out.setText(out)
        except :
            self.sc_out.setText('Error')

    def calc_remain(self) :
        x = self.sim_calc()
        try:
            out = operate(x[0], x[1], '%' , x[2]).solve()
            self.sc_out.setText(out)
        except :
            self.sc_out.setText('Error')

    def calc_exp(self) :
        x = self.sim_calc()
        try:
            out = operate(x[0], x[1], '**' , x[2]).solve()
            self.sc_out.setText(out)
        except :
            self.sc_out.setText('Error')
            
    ''' digital codes '''
    def my_codes(self) :
        num = self.code_number.text()
        index = self.code_select.currentIndex()
        try :
            if index == 0:
                out = code(num).ones_comp()
            if index == 1:
                out = code(num).twos_comp()
            if index == 2:
                out = code(num).ones_dec()
            if index == 3:
                out = code(num).twos_dec()
            if index == 4:
                out = code(num).bin2gray()
            if index == 5:
                out = code(num).gray2bin()
            if index == 6:
                out = code(num).gray_dec()
            if index == 7:
                out = code(num).dec2BCD()
            if index == 8:
                out = code(num).BCD2dec()
            self.code_out.setText(out)
        except :
            self.code_out.setText('Error')
            
    ''' AlphaNumeric codes '''
    def AlphaNumeric(self) :
        code = self.cb_input.toPlainText()
        base = int(self.cb_base.currentText())
        try :
            if self.cb_reverse.checkState() :
                out = anc(code , base).num2alpha()
            else:
                out = anc(code , base).alpha2num()
            self.cb_out.setPlainText(out)
        except :
            self.cb_out.setPlainText('Error')
    
    ''' clear out[not solution] of logic gates'''
    def clear_out(self) :
        self.lg_out.setPlainText('')

    def del_out(self) :
        self.lg_out.setPlainText(self.lg_out.toPlainText()[:-1])

    ''' when logic gate out length changes, some of changes happen
    to prevent program from error results'''
    def len_out(self) :
        if self.lg_ttable.text() == 'Truth Table' :
            out_length = len(self.lg_out.toPlainText())
            self.lg_counter.setText(str(out_length))
            if  out_length == 32 :
                self.lg_zero.setEnabled(False)
                self.lg_one.setEnabled(False)
            else :
                self.lg_zero.setEnabled(True)
                self.lg_one.setEnabled(True)
                
            if out_length == 2 or out_length == 4 :
                self.lg_pin2.setEnabled(True)
                self.lg_start.setEnabled(True)
            elif out_length == 8:
                self.lg_pin2.setEnabled(True)
                self.lg_pin3.setEnabled(True)
                self.lg_start.setEnabled(True)
            elif out_length == 16:
                self.lg_pin2.setEnabled(True)
                self.lg_pin3.setEnabled(True)
                self.lg_pin4.setEnabled(True)
                self.lg_start.setEnabled(True)
            elif out_length == 32:
                self.lg_pin2.setEnabled(True)
                self.lg_pin3.setEnabled(True)
                self.lg_pin4.setEnabled(True)
                self.lg_pin5.setEnabled(True)
                self.lg_start.setEnabled(True)
            else :
                self.lg_pin2.setEnabled(False)
                self.lg_pin3.setEnabled(False)
                self.lg_pin4.setEnabled(False)
                self.lg_pin5.setEnabled(False)
                self.lg_start.setEnabled(False)
      

    def zero_out(self) :
        self.lg_out.setPlainText(self.lg_out.toPlainText()+'0')

    def one_out(self) :
        self.lg_out.setPlainText(self.lg_out.toPlainText()+'1')

    ''' truth table from output '''
    def ttable_click(self) :
        if self.lg_ttable.text() == 'Truth Table' :
            try :
                self.logic_gate_out = self.lg_out.toPlainText()
                x = fill_tools().truth_table(int(self.lg_counter.text()),self.lg_out.toPlainText())
                self.lg_ttable.setText('output')
                self.lg_out.setPlainText(x)
                self.lg_zero.setEnabled(False)
                self.lg_one.setEnabled(False)
                self.lg_ac.setEnabled(False)
                self.lg_del.setEnabled(False)     
            except :
                pass
        else :
            self.lg_ttable.setText('Truth Table')
            self.lg_out.setPlainText(self.logic_gate_out)
            self.lg_zero.setEnabled(True)
            self.lg_one.setEnabled(True)
            self.lg_ac.setEnabled(True)
            self.lg_del.setEnabled(True)


    def start_logics(self) :
        global cancelMyThread    
        if self.lg_start.text() == 'start' :
            cancelMyThread = False
            self.start_click()
        else :
            cancelMyThread = True
            self.lg_start.setText('start')
        
    def start_click(self) :
        self.lg_start.setText('cancel')
        x = self.collect_info()
        try :
            self.MyData = MyThreadData(x[0] , x[1] , x[2] , x[3])
            self.MyData.start()
            self.MyData.trigger.connect(self.progress)
        except :
            pass
        

    ''' to initialize for start logic gates search solution'''
    def collect_info(self) :
        out = self.out_info()
        num_gates = self.gates_info()
        wait = self.time_info()
        num_pins = self.pins_info()
        return out, wait , num_gates, num_pins
        
            
    ''' to get out '''
    def out_info(self) :
        if self.lg_ttable.text() == 'Truth Table' :
            out = self.lg_out.toPlainText()
            return [int(i) for i in out]
        else :
            out = self.logic_gate_out
            return [int(i) for i in out]
            
    ''' get number of gates '''
    def gates_info(self) :
        num_gates = {0:7, 1:2, 2:3, 3:4 }
        return num_gates[self.lg_gates.currentIndex()]

    ''' get timeout'''
    def time_info(self) :
        if self.lg_time.currentIndex() == 0:
            return 0
        return int(self.lg_time.currentText())

    ''' get number of pins'''
    def pins_info(self) :
        pins = []
        if self.lg_pin2.checkState() :
            pins.append(2)
        if self.lg_pin3.checkState() :
            pins.append(3)
        if self.lg_pin4.checkState() :
            pins.append(4)
        if self.lg_pin5.checkState() :
            pins.append(5)
        return pins  # as list of integrs

    ''' disable buttons in simple calculator except Additon (+) to add BCD'''
    def hide_btns(self) :
        if self.sc_base.currentIndex() == 61 :
            status = False
        else :
            status = True
        self.sc_sub.setEnabled(status)
        self.sc_mul.setEnabled(status)
        self.sc_div.setEnabled(status)
        self.sc_correct.setEnabled(status)
        self.sc_rem.setEnabled(status)
        self.sc_pow.setEnabled(status)

    '''
    progress bar data
    data = (My.get_percent,My.search_finished,My.get_solutions,My.cycle_len,My.counter)
    '''
    def progress(self , data) :
        global cancelMyThread   
        self.lg_pbar.setValue(int(data[0]))
        self.lg_percent.setText('%'+str(data[0]))
        #print('percent {} ,   {} ,  {} '.format( data[0], data[3] ,data[4]))
        if data[1] :
            self.lg_solution.setText(str(data[2][0][0]))
            self.lg_start.setText('start')
        if  cancelMyThread  :
            self.lg_solution.setText('cancelled')
            self.lg_start.setText('start')

    def visible_ns(self) :
        if self.groupBox.isVisible() :
            self.groupBox.hide()
        else :
            self.groupBox.show()

    def visible_sc(self) :
        if self.groupBox_2.isVisible() :
            self.groupBox_2.hide()
        else :
            self.groupBox_2.show()

    def visible_co(self) :
        if self.groupBox_3.isVisible() :
            self.groupBox_3.hide()
        else :
            self.groupBox_3.show()

    def visible_an(self) :
        if self.groupBox_4.isVisible() :
            self.groupBox_4.hide()
        else :
            self.groupBox_4.show()

    def visible_lg(self) :
        if self.groupBox_5.isVisible() :
            self.groupBox_5.hide()
        else :
            self.groupBox_5.show()

    def about_me(self) :
        QMessageBox.information(self, "info", "this is a simple program, help you in some digital functions\nversion : 0\nfor more inforamation contact :\nhttps://www.facebook.com/ahmednaeem1996")
        

        
def main():
    app  = QApplication(sys.argv)
    window = mainApp()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()
