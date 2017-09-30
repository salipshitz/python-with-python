from tkinter import *
from window import Window

class Screen:
        def __init__(self, i, text, func):
                self.text = "Lesson "+i+": "+text
                self.screen_func = func

class Screens(Window):
        def __init__(self, master=None):
                super(Screens, self).__init__(master)
                self.master = master
                self.master.title("LearnPythonWithPython")
                self.pack(fill=BOTH, expand=1)
                self.s = [
                        Screen(1, "Setting up the IDE", self.idle),
                        Screen(2, "Basic syntax", self.syn),
                        Screen(3, "Variables", self.var),
                        Screen(4, "Data types", self.data_types),
                        Screen(5, "Hello, world!", self.hello_world),
                        Screen(6, "Input", self.inp),
                        Screen(7, "If statements", self.if_statement)
                        Screen(8, "Else and elif statements", self.else_elif)
                ]
		
        def s_init(self):
                self.new(home=True)
                for i in range(len(self.screens)):
                        s = self.s[i]
                        ind = i+1
                        self.cenBtn(s.text, s.screen_func)
        
        def idle(self):
                self.new()
                self.cenLbl(self.s[0].text)
                self.multiLbl("Hello, and welcome to LearnPythonWithPython. Today we will be learning about how to set up the IDE called IDLE but ... come to think about it, you are viewing this application so you probably already have IDLE installed. See you later.")
                self.btnNext(self.syn)

        def syn(self):
                self.new()
                self.cenLbl(self.s[1].text)
                self.multiLbl("Congratulations! You've completed lesson 1. This is lesson 2. To see the basic syntax, look at the source code for this application.")
                self.btnPrev(self.idle)
                self.btnNext(self.var)

        def var(self):
                self.new()
                self.cenLbl(self.s[2].text)
                self.multiLbl("Just like literally every single coding language in the world (except for maybe like BASIC and Assembly) and for sure every C based coding language (hint hint: Python is a C-based language), there are variables. There are many different types of variables in Python. Some examples are booleans (coming from Boolean algebra), lambdas (from lambda calculus) and numbers (from litterally every single form of math). Unlike 6th grade math, 7th grade math, 8th grade math, 9th grade math (Algebra I), 10th grade math (Geometry), 11th grade math (Algebra II), 12th grade math(Trigonometry?), college math(Calculus, Linear algebra, etc, etc, etc, and etc.), and some high school and college science(physics), variables in coding can have names longer than 1 letter with subscript. The only downside is that it takes up memory, and it takes up soooo mmuch storage. Like entire bytes. Soooooooo much!!!")
                self.btnPrev(self.syn)
                self.btnNext(self.data_types)
	
	def data_types(self):
                self.new()
                self.cenLbl(self.s[3].text)
                self.multiLbl("As I said last lesson, variables can be mmmmmmaaaaaannnnnnyyyyyy different types of things. A variable can be an str which is an str-ing of text surrounded by quotes (e.g. \"Hello, world!\"), an int which is an int-eger (e.g. 42), a float which is a float-ing point number (e.g. 3.14159265358979323846264338327950288419716939937510), a boolean which is a boolean value (which is either True or False. I think it's False. Wait nevermind it's true.), an array which stores an array of values surrounded in brackets where all the values are seperated by ,s (e.g. [\"Why?\", \"Are we stronger than the elements?\", \"What's yellow and dangerous?\", \"What do you get when you multiply six by seven?\", \"How many Vogons does it take to change a lightbulb?\", \"How many roads must a man walk down?\", 42, True, [\"Waaaait... an array inside an array?\", \"that's cray-cray\"], \"Is the array done yet?\", False,...] you get the idea.), a dictionary which is basically a dictionary for variables (e.g. ages = {\"Bob\": 100, \"Me\": 11}) and sooooo on and soooo forth")
                self.btnPrev(self.var)
                self.btnNext(self.hello_world)
                
        def hello_world(self):
                self.new()
                self.cenLbl(self.s[4].text)
                self.multiLbl("Hello world programs are usually the first to be learned because they are so simple, but why do they make them so simple? Those programs could be made harder and more fun by just a little bit. First things first, you need to know what a hello world program looks like, so look in the console. Go on. I'm not going anywhere. You want to be able to do that? Well, that sucks for you. This lesson is not about hello world. It's about the base methods in Python. \"What's a method?\" I hear you typing in the comments. Well, I'm not telling you. And also I don't read the comments. So sucks for you.\nSo any ways, there are many base methods >:(don't even try asking):< such as print and input. Print prints text to the console. Input asks the user for input. That simple. Well not really. In print you have to put () after it because it's a *method* and inside those parentheses put what you want to say (HAS TO BE AN STR (can be a variable)), for example print(\"LearnPythonWithPython\") will print LearnPythonWithPython. Seriously. Try it. PRESS LE BUTTON!!!")
                self.cenBtn("print(\"LearnPythonWithPython\")", self.hello_world_code)
                self.cenLbl("It's time for CHALLENGE TIME: Try to make a hello world program by declaring a variable called string and print()ing it")
                self.btnPrev(self.data_types)
                self.btnNext(self.inp)
        
        def inp(self):
                self.new()
                self.cenLbl(self.s[5].text)
                self.multiLbl("Hello, world! That last (mini) project was fun...ish. We want to make programs with UI! We want user input() ... i mean interface lol lmao rofl lellellellellelelelelelllelleleellelelelellelelel. so user \"interface\" as they call it is an interface where users interact. Hey! There's another possible name! User Interaction stuf! well anyways, let's get to the point. The input() method is a good starting point for UI. It allows the user to enter ... wait for it ... input()! Inside the parentheses thingies, you have to type in what ever you want the computer to ask you. For instance, press the button that has a line of code on it.")
                self.cenBtn("inp = input(\"Enter your input here: \")\nprint(inp)", self.inp_code)
                self.cenLbl("Now you try to figure out a practical purpose for the input() method. Enter it in the comments (that I tooooootally read)")
                self.btnPrev(self.hello_world)
                self.btnNext(self.if_statement)
        
        def if_statement(self):
                self.new()
                self.cenLbl(self.s[6].text)
                self.multiLbl("If statements determine *if* a condition (e.g. 1>2 is False and \"hello\" == \"hello\" is True) is True, then it does the stuff indented after the colon(:). One example is")
                btnTxt = """if True:
                \tprint(\"Yay! It's True!\")
                if False:
                \tprint(\":( It's False")
                """
                self.cenBtn(btnText, self.if_code)
                self.btnPrev(self.inp)
                self.btnNext(self.else_elif)
        
        def else_elif(self):
                self.new()
                self.cenLbl(self.s[7].text)
                self.multiLbl("\"But ... what if you want to test if something you just tested is not True? Do you need another if statement with (whatever condition) == False?\" I hear you commenting in the comment section. Well, the answer is NO STUPID!!! THIS IS PROGRAMMING!!! AND THIS LESSON EXISTS!!! WHAT DID YOU THINK IT WOULD BE ABOUT??? The solution lies in else statements, which literally translate to ... else. You just type else: and then whatever the **** you want if it is false. \"But what if you want to have an if and else statement *inside* an else statement?\" The answer is THIS IS CODING YOU NOT SMART PERSON. And plus, it says it in the title. elif is short for else if which is short for else-erwise if this is true.")
                self.btnPrev(self.if_statement)
                
        def hello_world_code(self):
                print("LearnPythonWithPython")
        
        def inp_code(self):
                inp = input("Enter your input here: ")
                print(inp)
                
        def if_code(self):
                if True:
                        print("Yay! It's True!")
                if False:
                        print(":( It's False.")
                
                              
