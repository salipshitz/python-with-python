import sqlite3
import smtplib

class UserError(Exception):
    pass

class SqlHandler:
    def __init__(self):
        self.connection = sqlite3.connect("comments.db")
        self.cursor = self.connection
        
        cmd = """
        CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT
        email TEXT
        password TEXT);"""
        
        self.cursor.execute(cmd)
                
        cmd = """
        CREATE TABLE IF NOT EXISTS comments (
        id INTEGER PRIMARY KEY,
        senderId INTEGER
        comment TEXT);"""
        
        self.cursor.execute(cmd)
        
    def login(self, username, password):
        cmd = "SELECT 1 FROM users WHERE ((username = {0} OR email = {0}) AND password = {1});".format(username, password)
        self.cursor.execute(cmd)
        user = self.cursor.fetchone()
        try:
           assert user != None
        except AssertionError:
            raise UserError("While logging in: Username or password not correct.")
        return user
    
    def signup(self, username, email, password):
        cmd = "SELECT 1 FROM users WHERE (username = \"{0}\" OR email = \"{1}\");".format(username, email)
        self.cursor.execute(cmd)
        try:
            assert user == None
        except AssertionError:
            raise UserError("While signing up: User with username or email already exists")
            return False
        cmd = "INSERT INTO users VALUES(NULL, {0}, {1}, {2});\n SELECT 1 FROM users WHERE (username = {0});".format(username, email, password)
        self.cursor.execute(cmd)
        return self.cursor.fetchone()
    
    def sendComment(self, senderId, comment):
        cmd = "INSERT INTO comments VALUES(NULL, {0}, {1});".format(senderId, comment)
        self.cursor.execute(cmd)
    
    def showComments(self):
        cmd = "SELECT * FROM comments"
        self.cursor.execute(cmd)
        return self.fetchall
        
        
