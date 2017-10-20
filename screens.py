from tkinter import *
from window import Window

class Screen:
        def __init__(self, title, showAs, func):
                self.title = title
                self.showAs = showAs
                self.func = func

class LessonScreen(Screen):
        def __init__(self, i, text, screenFunc):
                title = "Lesson "+str(i)+": "+text
                showAs = title
                func = screenFunc
                super(LessonScreen, self).__init__(title, showAs, func)
                
class ProjectScreen(Screen):
        def __init__(self, unit, proj, partTitle, screenFunc):
                text = "Unit "+str(unit)+" - "+proj+": "+partTitle
                showAs = partTitle
                func = screenFunc
                super().__init__(text, showAs, func)

class Screens(Window):
        
        def new_lesson(self, unit, screenNum):
                screenNum -= 1
                self.master.geometry(self.screenBounds)
                unitStr = "self.u"+str(unit)
                u = eval(unitStr)
                self.new(1)
                self.cenLbl(u[screenNum].title)
                if screenNum > 0:
                        self.btnPrev(u[screenNum-1].func)
                if screenNum < len(u)-1:
                        self.btnNext(u[screenNum+1].func)
        
        def __init__(self, master=None):
                self.homeBounds = "800x1000"
                self.screenBounds = "800x400"
                self.u1 = [
                        LessonScreen(1, "Setting up the IDE", self.idle),
                        LessonScreen(2, "Basic syntax", self.syn),
                        LessonScreen(3, "Variables", self.var),
                        LessonScreen(4, "Data types", self.data_types),
                        LessonScreen(5, "Hello, world!", self.hello_world),
                        LessonScreen(6, "Input", self.inp),
                        LessonScreen(7, "If statements", self.if_statement),
                        LessonScreen(8, "Else and elif statements", self.else_elif),
                        LessonScreen(9, "\"WHAT THE HECK IS A METHOD!?!?!?\" (your comments)", self.methods),
                        LessonScreen(10, "A function. Ok? I will tell you what a function is.", self.functions),
                        LessonScreen(11, "I told you. Object oriented programming is classes. Well, sort of.", self.oop),
                        LessonScreen(12, "Loop-da-loops", self.loops)
                ]
                PROJ = "Battleship"
                self.p1 = [
                        ProjectScreen(1, PROJ, "What you're building", None),
                        ProjectScreen(1, PROJ, "An empty list", None),
                        ProjectScreen(1, PROJ, "Making the board", None),
                        ProjectScreen(1, PROJ, "Printing the board", None),
                        ProjectScreen(1, PROJ, "Hide", None),
                        ProjectScreen(1, PROJ, "and go seek!", None),
                        ProjectScreen(1, PROJ, "#CHEAT-OS!!!", None),
                        ProjectScreen(1, PROJ, "We have a winner!!!", None),
                        ProjectScreen(1, PROJ, "YOU SAX!!!", None),
                        ProjectScreen(1, PROJ, "Next time, try to aim *inside* the ocean", None),
                        ProjectScreen(1, PROJ, "\"Insanity: doing the same thing over and over and expecting different results\" - Albert Einstein", None)
                ]
                super(Screens, self).__init__(master)
                self.master = master
                self.master.title("LearnPythonWithPython")
                self.pack(fill=BOTH, expand=1)
                
        def s_init(self, unitNum):
                self.new(0)
                s = "self.unit_"+str(unitNum)+"()"
                exec(s)
                self.master.geometry(self.homeBounds)
        
        def p_init(self, unitNum):
                self.new(0)
                s = "self.proj_"+str(unitNum)+"()"
                print(s)
                exec(s)
                self.master.geometry(self.homeBounds)
                
        def unit_1(self):
                for s in self.u1:
                        self.cenBtn(s.showAs, s.func)
                self.cenBtn("Unit project: Battleship", lambda: self.p_init(1))
                self.cenBtn("Unit 2: Turtle graphics", None) #s_init(2)
        
        def proj_1(self):
                for s in self.p1:
                        self.cenBtn(s.showAs, s.func)
                self.cenBtn("Back to unit 1", lambda: self.s_init(1))
                self.cenBtn("Unit 2: Turtle graphics", None) #s_init(2)
        
        def idle(self):
                self.new_lesson(1, 1)
                self.multiLbl("Hello, and welcome to LearnPythonWithPython. Today we will be learning about how to set up the IDE called IDLE but ... come to think about it, you are viewing this application so you probably already have IDLE installed. See you later.")

        def syn(self):
                self.new_lesson(1, 2)
                self.multiLbl("Congratulations! You've completed lesson 1. This is lesson 2. To see the basic syntax, look at the source code for this application.")

        def var(self):
                self.new_lesson(1, 3)
                self.multiLbl("Just like literally every single coding language in the world (except for like binary) and for sure every C based coding language (hint hint: Python is a C-based language), there are variables. There are many different types of variables in Python. Some examples are booleans (coming from Boolean algebra), lambdas (from lambda calculus) and numbers (from litterally every single form of math). Unlike 6th grade math, 7th grade math, 8th grade math, 9th grade math (Algebra I), 10th grade math (Geometry), 11th grade math (Algebra II), 12th grade math(Trigonometry?), college math(Calculus, Linear algebra, etc, etc, etc, and etc.), and some high school and college science(physics), variables in coding can have names longer than 1 letter with subscript. The only downside is that it takes up memory, and it takes up soooo mmuch storage. Like entire bytes. Soooooooo much!!!")

        def data_types(self):
                self.new_lesson(1, 4)
                self.multiLbl("As I said last lesson, variables can be mmmmmmaaaaaannnnnnyyyyyy different types of things. A variable can be an str which is an str-ing of text surrounded by quotes (e.g. \"Hello, world!\"), an int which is an int-eger (e.g. 42), a float which is a float-ing point number (e.g. 3.14159265358979323846264338327950288419716939937510), a boolean which is a boolean value (which is either True or False. I think it's False. Wait nevermind it's true.), an array which stores an array of values surrounded in brackets where all the values are seperated by ,s (e.g. [\"Why?\", \"Are we stronger than the elements?\", \"What's yellow and dangerous?\", \"What do you get when you multiply six by seven?\", \"How many Vogons does it take to change a lightbulb?\", \"How many roads must a man walk down?\", 42, True, [\"Waaaait... an array inside an array?\", \"that's cray-cray\"], \"Is the array done yet?\", False,...] you get the idea.), a dictionary which is basically a dictionary for variables (e.g. ages = {\"Bob\": 100, \"Me\": 11}) and sooooo on and soooo forth")
                
        def hello_world(self):
                self.new_lesson(1, 5)
                self.multiLbl("Hello world programs are usually the first to be learned because they are so simple, but why do they make them so simple? Those programs could be made harder and more fun by just a little bit. First things first, you need to know what a hello world program looks like, so look in the console. Go on. I'm not going anywhere. You want to be able to do that? Well, that sucks for you. This lesson is not about hello world. It's about the base methods in Python. \"What's a method?\" I hear you typing in the comments. Well, I'm not telling you. And also I don't read the comments. So sucks for you.\nSo any ways, there are many base methods >:(don't even try asking):< such as print and input. Print prints text to the console. Input asks the user for input. That simple. Well not really. In print you have to put () after it because it's a *method* and inside those parentheses put what you want to say (HAS TO BE AN STR (can be a variable)), for example print(\"LearnPythonWithPython\") will print LearnPythonWithPython. Seriously. Try it. PRESS LE BUTTON!!!")
                code = """print("LearnPythonWithPython")"""
                self.cenBtn(code, lambda: exec(code))
                self.cenLbl("It's time for CHALLENGE TIME: Try to make a hello world program by declaring a variable called string and print()ing it")
                
        def inp(self):
                self.new_lesson(1, 6)
                self.multiLbl("Hello, world! That last (mini) project was fun...ish. We want to make programs with UI! We want user input() ... i mean interface lol lmao rofl lellellellellelelelelelllelleleellelelelellelelel. so user \"interface\" as they call it is an interface where users interact. Hey! There's another possible name! User Interaction stuf! well anyways, let's get to the point. The input() method is a good starting point for UI. It allows the user to enter ... wait for it ... input()! Inside the parentheses thingies, you have to type in what ever you want the computer to ask you. For instance, press the button that has a line of code on it.")
                code = """inp = input("Enter your input here: ")
print(inp)\t\t\t\t"""
                self.cenBtn(code, lambda: exec(code))
                self.cenLbl("Now you try to figure out a practical purpose for the input() method. Enter it in the comments (that I tooooootally read)")
                
        def if_statement(self):
                self.new_lesson(1, 7)
                self.multiLbl("If statements determine *if* a condition (e.g. 1>2 is False and \"hello\" == \"hello\" is True) is True, then it does the stuff indented after the colon(:). One example is")
                code = """if True:\t\t\t\t\t
\tprint("if True: is always evaluated")
if False:\t\t\t\t\t
\tprint("if False: is always evaluated")"""
                self.cenBtn(code, lambda: exec(code))
                
        def else_elif(self):
                self.new_lesson(1, 8)
                self.multiLbl("\"But ... what if you want to test if something you just tested is not True? Do you need another if statement with (whatever condition) == False?\" I hear you commenting in the comment section. Well, the answer is NO STUPID!!! THIS IS PROGRAMMING!!! AND THIS LESSON EXISTS!!! LOOK AT THE TITLE!!! WHAT DID YOU THINK IT WOULD BE ABOUT??? The solution lies in else statements, which literally translate to ... you guessed it — else. You just type else: and then whatever the print(\"****\") you want if the condition you tested is false. \"But what if you want to have an if and else statement *inside* an else statement?\" The answer is THIS IS CODING YOU NOT SMART PERSON. And plus, it says it in the title. elif is short for else if which is short for else-erwise if this is true.")
        
        def methods(self):
                self.new_lesson(1, 9)
                self.multiLbl("Now, we're finally going to answer that question: \"WHAT THE HECK IS A METHOD?!?!?!?!?!?!?!?!?!\" Geez. Stop commenting. ITZ BAD 4 UR PUNCSHOOASHUN CUPZ LOC KEE AN SPILEENG. IT WILL TURN THE SQL DATABASE THAT I DON'T READ INTO A YOUTUBE COMMENTS! I LITTERALLY MAKE THE WORDS UR COMMENT HAS BEEN RECIEVED APPEAR EVEN IF I NEVER READ IT!!! SHOOT MY CUPZ LUC KEE IZ BROCEN I M USING A MAC ALL MY TEXT IS NOW AND FOREVER CAPITALIZED :(:(:(:(:(:(:(")
                self.multiLbl("SO, ANYWAYS, A METHOD IS A FUNCTION INSIDE OF A CLASS. \"WHAT ARE FUNCTIONS AND CLASSES?\" YOU WILL FIND OUT NEXT LESSON.")
        
        def functions(self):
                self.new_lesson(1, 10)
                self.multiLbl("A function. Use:\n def function_name(args):\n\t#insert_code_here\n to create a function and function_name(args) to call it. You can have as many args as you want and they can be whatever you want. Be warned. Functions are eeeeevvvvveeeeerrrrryyyyywwwwwhhhhheeeeerrrrreeeee. Print is a function. Input is a function. If you look at the source code, you might see functions such as eval and exec. There are many other functions just 2 name a few.")
        
        def oop(self):
                self.new_lesson(1, 11)
                self.multiLbl("You thought this lesson was going to be about classes? Ha! weeeelllllll, technically object oriented programming is classes. You see, a class has the basic methods and variables. An object is one version of a class. Let me explain and show you the syntax for a class at the same time by making a student class. I'll show you how.")
                code = """class Student:\t\t\t\t\t
\tdef __init__(self, name, grade, gpa):\t\t\t
\t\tself.name = name\t\t\t\t\t\t
\t\tself.grade = grade\t\t\t\t\t\t
\t\tself.gpa = gpa\t\t\t\t\t\t\t\t
\tdef __repr__(self):\t\t\t\t\t\t
\t\treturn self.name+" has been in school for "+str(self.grade+1)+" years and has a gpa of "+str(self.gpa)

billy = Student(\"Billy Bob Joe\", 5, 3.95)\t\t\t\t
print(billy)\t\t\t\t\t"""
                self.cenBtn(code, lambda: exec(code))
                self.multiLbl("Two underscores signify a special keyword, and in the case of a class, it's usually a method name. The __init__ method is run as soon as the object is initialized, and it takes in self and whatever other arguments you want it to. Self refers to the class. The __repr__ and __str__ methods are what happen when you want it to be a string, __repr__ is like the official one and __str__ is called when you use str(object_name). You also have __del__ and __call__ and many, many more. You can also create methods but the first argument is always self and to run it from another method in the class, you have to do self.method_name or you can run it like ObjectName.method_name. You can also have static methods which are called by ClassName.method_name(args) and don't have a self. To define a static method, you do @staticmethod above the line with the method.")

        def loop_1_12_1(self, i):
                if i < 3:
                        print(i)
                        self.master.after_idle(self.loop_1_12_1, i+1)

        def loop_1_12_2(self, i):
                if i < 4:
                        print(i)
                        i += 1
                        self.master.after_idle(self.loop_1_12_2, i)

        def loops(self):
                self.new_lesson(1, 12)
                self.multiLbl("I'm doing this out of order but who cares. A loop is something that repeats. There are two types of loops. A for loop and a while loop. This should show you the difference")
                code = """for i in range(3):
        print(i)
"""
                self.cenBtn(code, lambda: self.loop_1_12_1(0))
                code = """i = 0
while i < 4:
\tprint(i)
\ti += 1"""
                self.cenBtn(code, lambda: self.loop_1_12_2(0))
                self.multiLbl("So as you can see, a for loop loops for every item in a list and a while loop repeats while a condition is true. For for loops, a function that is commonly used is range(n). Range makes a list of numbers between 0 (inclusive) and n (exclusive). So range(3) returns [0, 1, 2] and range(1) returns [0]. If you're using for with a dictionary, for thing in dict will make thing the key but for key, value in dict will have key as the key and value as the value. Mind blown. A while loop will run while the condition is True.")
