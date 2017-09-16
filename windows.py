from tkinter import *
from PIL import Image
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
                if self.logoimg is not None:
                        self.logoview.setimage(self.logoimg)
                elif None not in [self.logoview, self.logopath]:
                        self.logoimg = Image(self.logopath)
                        if type(self.logoview) is ImageView:
                                self.logoview.setimage(self.logoimg)
                        else:
                                raise TypeError("Windows.logoview not of ImageView type")
                else:
                        raise ValueError("Windows.logoview or Windows.logopath equal None")
        
        def s0(self):
                self.new()
                self.cenLbl("Hello. Welcome to LearningPythonWithPython")
                self.cenBtn("Lesson 1: Setting up the IDE", s1)
        
        def s1(self):
                
