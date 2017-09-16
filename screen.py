from tkinter import *
from windows import *

class Screen(Windows):
	def __init__(self, master=None):
		super(Screen, self).__init__()
		self.master = master
		self.master.title("Learn Python With Python")
		self.pack(fill=BOTH, expand=1)
		self.s0()
		
