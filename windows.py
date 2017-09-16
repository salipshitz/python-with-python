from tkinter import *
from abc import ABC

class Windows(Frame, ABC):
        def close_app(self):
                self.destroy()
                print("Succesfully killed")
                
        def cenBtn(self):
               b = Button(self, text=txt, command=func)
               b.pack()
                
        def choBtn(self, txt, func, x, y):
                print("self.choBtn")
                print("x: " + str(x) + "\ny: " + str(y))
                btn = Button(self, text=txt, command=func)
                btn.place(x=x, y=y)
                return btn
                
        def btnQuit(self):
                print("Button Ready")
                self.choBtn("Quit", self.close_app, 100, 100)
                
        def new(self):
                print("New screen")
                for widget in self.winfo_children():
                        widget.destroy()
                self.btnQuit()
        
        def __init__(self):
               super(Windows, self).__init__()
        
        def s0(self):
                self.new()
		
