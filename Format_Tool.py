import tkinter as tk
from tkinter import scrolledtext
import logging
import threading
import ctypes
import inspect
import time

class defult():

    def defult_window(self,master,masterpage):
        self.back = tk.Button(self,text="回首頁",command=lambda:self.switch_frame(master,masterpage) )
        self.back.grid(row=0,column=99)

        self.start = tk.Button(self,text="Start (F9)",command=self.Start,width=20)
        self.start.grid(row=99,column=0, pady=10)

        self.stop = tk.Button(self,text="Stop (F12)",command=self.Stop,width=20, state="disabled")
        self.stop.grid(row=99,column=98, pady=10)

    def ParserRun(self):
        pass

    def switch_frame(self,master,masterpage):
        master.switch_frame(masterpage)
        
    def Start(self):
        global parser_thread
        self.stop.config(state="normal")
        self.start.config(state="disabled")
        parser_thread = threading.Thread(target=self.ParserRun)
        parser_thread.start()
    
    def Stop(self):
        self.start.config(state="normal")
        self.stop.config(state="disabled")
        global parser_thread
        stop_thread(parser_thread)
    
    

class stop_thread:
    '''
        刻意產生錯誤終止程序
    '''
    def __init__(self,thread):
        self._async_raise(thread.ident,SystemExit)

    def _async_raise(self,tid,exctype):
        tid = ctypes.c_long(tid)
        if not inspect.isclass(exctype):
            exctype = type(exctype)
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid,ctypes.py_object(exctype))
        if res ==0:
            raise ValueError('invalid thread id')
        elif res != 1 :
            ctypes.pythonapi.PyThreadState_SetAsyncExc(tid,None)
            raise SystemError('PyThreadState_SetAsyncExc failed')
        



class ScrolledTextHandler(logging.Handler,defult):
    def __init__(self, text_widget):
        super().__init__()
        self.text_widget = text_widget

    def emit(self, record):
        msg = self.format(record)
        self.text_widget.config(state="normal")
        self.text_widget.insert(tk.END, msg + "\n")
        self.text_widget.config(state="disabled")
        self.text_widget.see(tk.END)
    
    def setup_logging(self,text_widget):
        handler = ScrolledTextHandler(text_widget)
        # formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        # handler.setFormatter(formatter)
        logging.getLogger().addHandler(handler)
        logging.getLogger().setLevel(logging.INFO)
    

class GUI_Fomat_Tool(ScrolledTextHandler):

    row = 1
    row_colun_dict = dict()

    def GUI_Log_Text(self,column = 0,columnspan=1):
        if str(columnspan).upper()=='END':columnspan=100
        log_Text = scrolledtext.ScrolledText(self, wrap=tk.WORD, width=80, height=10, state="disabled")
        log_Text.grid(row = self.row ,column=column,columnspan=columnspan)
        self.row_colun_dict[self.row] = column+1
        self.row+=1
        return log_Text
    
    def GUI_button(self,text,command,column=0,columnspan=1,rowadd=True):
        '''
            rowadd -> 向下增加row(True) 排在前值右側(False) 
        '''
        if str(columnspan).upper()=='END':columnspan=99
        if not rowadd:column = self.row_colun_dict[self.row if rowadd else self.row-1]
        button = tk.Button(self, text=text, command=command)
        button.grid(row=self.row if rowadd else self.row-1,column=column,columnspan=columnspan)
        self.row_colun_dict[self.row if rowadd else self.row-1] = column+columnspan
        if rowadd:self.row+=1
        return button


    def GUI_label(self,text,column=0,columnspan=1,rowadd=True,font=("Helvetica", 14, "bold")):
        '''
            rowadd -> 向下增加row(True) 排在前值右側(False) 
        '''
        if str(columnspan).upper()=='END':columnspan=99
        if not rowadd:column = self.row_colun_dict[self.row if rowadd else self.row-1]
        label = tk.Label(self, text=text, font=font, anchor='w')
        label.grid(row=self.row if rowadd else self.row-1,column=column,columnspan=columnspan)
        self.row_colun_dict[self.row if rowadd else self.row-1 ] = column+columnspan
        if rowadd:self.row+=1
        return label
    
    def GUI_Entry(self,column=0,columnspan=1,width=20,rowadd=True):
        '''
            rowadd -> 向下增加row(True) 排在前值右側(False) 
        '''
        if str(columnspan).upper()=='END':columnspan=99
        if not rowadd:column = self.row_colun_dict[self.row if rowadd else self.row-1]
        Entry_input = tk.Entry(self, width=width)
        Entry_input.grid(row=self.row if rowadd else self.row-1,column=column,columnspan=columnspan)
        self.row_colun_dict[self.row if rowadd else self.row-1] = column+columnspan
        if rowadd:self.row+=1
        return Entry_input
    
    