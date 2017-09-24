from tkinter import *
from window import Window

class Screens(Window):
        def __init__(self, master=None):
                super(Screen, self).__init__(master)
                self.master = master
                self.master.title("Learn Python With Python")
                self.pack(fill=BOTH, expand=1)
		
        def s_init(self):
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
