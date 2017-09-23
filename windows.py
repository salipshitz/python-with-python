from tkinter import *

class Windows(Frame):
        def __init__(self, master=None):
               super(Windows, self).__init__()
        
        def close_app(self):
                self.master.destroy()
                print("Succesfully killed")
                
        def cenBtn(self, txt, func):
               b = Button(self, text=txt, command=func)
               b.pack()
                
        def choBtn(self, txt, func, x, y):
                b = Button(self, text=txt, command=func)
                b.place(x=x, y=y)
                return b
                
        def btnQuit(self):
                return self.choBtn("Quit", self.close_app, 0, 0)

        def btnBack(self):
                return self.choBtn("Back", self.s0, 0, 0)

        def btnNext(self, nextScreen):
                return Button(self, text="Next", command=nextScreen).place(relx=1.0, rely=1.0, anchor=SE)

        def btnPrev(self, prevScreen):
                return Button(self, text="Previous", command=prevScreen).place(relx=0.0, rely=1.0, anchor=SW)
                
        def choLbl(self, txt, x, y):
                lbl = Label(self, text=txt)
                lbl.place(x=x, y=y)
                return lbl
        
        def cenLbl(self, txt):
                return Label(self, text=txt).pack()

        def multiLbl(self, txt):
                return Label(self, text=txt, anchor=W, wraplength=425).pack()
                
        def new(self, home=False):
                for widget in self.winfo_children():
                        widget.destroy()
                if home == True:
                        self.btnQuit()
                else:
                        self.btnBack()
                        
        def s0(self):
                self.new(home=True)
                self.cenLbl("Hello. Welcome to LearningPythonWithPython")
                self.cenBtn("Lesson 1: Setting up the IDE", self.idle)
                self.cenBtn("Lesson 2: Basic syntax", self.syn)
        
        def idle(self):
                self.new()
                self.cenLbl("Lesson 1: Setting up the IDE")
                self.multiLbl("Hello, and welcome to LearnPythonWithPython. Today we will be learning about how to set up the IDE called IDLE but ... come to think about it, you are viewing this application so you probably already have IDLE installed. See you later.")
                self.btnNext(self.syn)

        def syn(self):
                self.new()
                self.cenLbl("Lesson 2: Basic syntax")
                self.multiLbl("Congratulations! You've completed lesson 1. This is lesson 2. To see the basic syntax, look at the source code for this application.")
                self.btnPrev(self.idle)
