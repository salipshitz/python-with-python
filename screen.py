from tkinter import *
from windows import *
from UIHandler import ImageView

class Screen(Windows):
	def __init__(self, master=None):
		super(Screen, self).__init__(master)
		self.master = master
		self.master.title("Learn Python With Python")
		self.logoview = ImageView(master).pack()
		self.pack(fill=BOTH, expand=1)
		self.s0()
		
