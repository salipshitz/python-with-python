from tkinter import *
from abc import ABC

class Windows(Frame, ABC):
        def close_app(self):
                self.master.destroy()
                print("Succesfully killed")
                
        def cenBtn(self):
               b = Button(self, text=txt, command=func)
               b.pack()
                
        def choBtn(self, txt, func, x, y):
                btn = Button(self, text=txt, command=func)
                btn.place(x=x, y=y)
                return btn
                
        def btnQuit(self):
                self.choBtn("Quit", self.close_app, 0, 0)
                
        def new(self):
                for widget in self.winfo_children():
                        widget.destroy()
                self.btnQuit()
        
        def __init__(self, master=None):
               super(Windows, self).__init__()
        
        def s0(self):
                self.new()
		
