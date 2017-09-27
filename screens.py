from tkinter import *
from window import Window

class Screens(Window):
        def __init__(self, master=None):
                super(Screens, self).__init__(master)
                self.master = master
                self.master.title("Learn Python With Python")
                self.pack(fill=BOTH, expand=1)
		
        def s_init(self):
                self.new(home=True)
                self.cenLbl("Hello. Welcome to LearningPythonWithPython")
                self.cenBtn("Lesson 1: Setting up the IDE", self.idle)
                self.cenBtn("Lesson 2: Basic syntax", self.syn)
                self.cenBtn("Lesson 3: Variables", self.var)
        
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
                self.btnNext(self.var)

        def var(self):
                self.new()
                self.cenLbl("Lesson 3: Variables")
                self.multiLbl("Just like literally every single coding language in the world (except for maybe like BASIC and Assembly) and for sure every C based coding language (hint hint: Python is a C-based language), there are variables. There are many different types of variables in Python. Some examples are booleans (coming from Boolean algebra), lambdas (from lambda calculus) and numbers (from litterally every single form of math). Unlike 6th grade math, 7th grade math, 8th grade math, 9th grade math (Algebra I), 10th grade math (Geometry), 11th grade math (Algebra II), 12th grade math(Trigonometry?), college math(Calculus, Linear algebra, etc, etc, etc, and etc.), and some high school and college science(physics), variables in coding can have names longer than 1 letter possibly with some subscript. The only downside is that it takes up memory, and it takes up soooo mmuch storage. Like entire bytes. Soooooooo much!!!")
                self.btnPrev(self.syn)
