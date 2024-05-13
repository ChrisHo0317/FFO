
import tkinter as tk
from Genshin_Impact.Genshin_Impact import Genshin_Impact
from Format_Tool import GUI_Fomat_Tool,defult,stop_thread
import time
import sys
import pythoncom


class SampleApp(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.title("Parser GUI")
        self.switch_frame(StartPage)
        self.geometry("700x450")
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.close)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

    def close(self):
        sys.exit()

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        label = tk.Label(self, text="Start page", font=("Helvetica", 18, "bold"))
        Button1 = tk.Button(self, text="原神連結", command=lambda: master.switch_frame(PageOne),relief = 'ridge')
        Button2 = tk.Button(self, text="座標模式", command=lambda: master.switch_frame(PageTwo),relief = 'ridge')

        label.grid(row = 2,columnspan=2)
        Button1.grid(row = 0,column=0)
        Button2.grid(row = 0,column=1)




class PageOne(tk.Frame,GUI_Fomat_Tool,defult):
    def __init__(self, master):
        self.user_input = 1
        tk.Frame.__init__(self, master)
        tk.Label(self, text="原神連結", font=("Helvetica", 18, "bold")).grid(row=0,column=0)
        self.defult_window(master,StartPage)
        self.window() 

    def window(self):
        self.log_Text = self.GUI_Log_Text(columnspan='end')
        self.setup_logging(self.log_Text)
        self.bind_all("<Key>", self.keyboard_pressed)

    def keyboard_pressed(self,event):
        if event.keysym == 'F9':
            self.Start()
        if event.keysym == 'F12':
            self.Stop()

    def ParserRun(self):
        self.satuts = Genshin_Impact.Run(self.user_input)
        self.Stop

class PageTwo(tk.Frame,GUI_Fomat_Tool,defult):
    def __init__(self, master):
        self.X=0
        self.Y=0
        tk.Frame.__init__(self, master)
        tk.Label(self, text="座標模式", font=("Helvetica", 18, "bold")).grid(row=0,column=0)
        self.defult_window(master,StartPage)
        self.window() 

    def window(self):
        self.Label_x = self.GUI_label(text = f'X座標 : {self.X}',columnspan='end')
        self.Label_y = self.GUI_label(text = f'Y座標 : {self.Y}',columnspan='end')
        self.Label_1 = self.GUI_label(text = f'暫存座標1 : ',columnspan='end')
        self.Label_2 = self.GUI_label(text = f'暫存座標2 : ',columnspan='end')
        self.Label_3 = self.GUI_label(text = f'暫存座標3 : ',columnspan='end')
        self.bind_all("<Key>", self.keyboard_pressed)

    def ParserRun(self):
        self.loop=True
        while self.loop:
            self.X,self.Y = Genshin_Impact.get_mouse_position()
            self.Label_x.config(text=f'X座標 : {self.X}')
            self.Label_y.config(text=f'Y座標 : {self.Y}')
            time.sleep(0.05)

    def keyboard_pressed(self,event):
        if event.keysym == 'F9':self.Start()
        if event.keysym == 'F12':
            self.Stop()
            self.loop = False
        if event.keysym == '1' and (event.state & 0x4) != 0:
            self.Label_1.config(text=f'暫存座標1 : {self.X} , {self.Y}')
        if event.keysym == '2' and (event.state & 0x4) != 0:
            self.Label_2.config(text=f'暫存座標2 : {self.X} , {self.Y}')
        if event.keysym == '3' and (event.state & 0x4) != 0:
            self.Label_3.config(text=f'暫存座標3 : {self.X} , {self.Y}')




if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()