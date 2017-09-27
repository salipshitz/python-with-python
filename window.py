from tkinter import *

class Window(Frame):
        def __init__(self, master=None):
               super(Window, self).__init__()
               self.s_init()
        
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
                return self.choBtn("Back", self.s_init, 0, 0)

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
