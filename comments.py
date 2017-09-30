from tkinter import *
import sqlite3

class Comments:
        def __init__(self):
                login = sqlite3.connect("login.db")
                comments = sqlite3.connect("comments.db")
