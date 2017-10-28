# DO NOT EDIT!!!

from tkinter import Tk
from screens import Screens

q = False
while not q:
    master = Tk()
    app = Screens(master=master)
    master.mainloop()
    done = False
    inp = input("Are you sure you want to quit (y/n)")
    while not done:
        if inp == 'y':
            done = True
            q = True
            break
        elif inp == 'n':
            done = True
            continue
        inp = input("Seriously. (y/n)")
