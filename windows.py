from tkinter import *
from abc import ABC

class Windows(Frame, ABC):
        def __init__(self, master=None):
               super(Windows, self).__init__()
        
        def close_app(self):
                self.master.destroy()
                print("Succesfully killed")
                
        def cenBtn(self, txt, func):
               b = Button(self, text=txt, command=func)
               b.pack()
                
        def choBtn(self, txt, func, x, y):
                btn = Button(self, text=txt, command=func)
                btn.place(x=x, y=y)
                return btn
                
        def btnQuit(self):
                return self.choBtn("Quit", self.close_app, 0, 0)
                
        def choLbl(self, txt, x, y):
                lbl = Label(self, text=txt)
                lbl.place(x=x, y=y)
                return lbl
        
        def cenLbl(self, txt):
                return Label(self, text=txt).pack()
                
        def new(self):
                for widget in self.winfo_children():
                        widget.destroy()
                self.btnQuit()
        
        
        
        def s0(self):
                self.new()
                self.cenLbl("Hello. Welcome to LearningPythonWithPython")
                self.cenBtn("Lesson 1: Setting up the IDE", s1)
        
        def s1(self):
                
