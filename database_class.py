import sqlite3
from user_class import User

class Database:
    def __init__(self, User.username, User.login_password):
        self.username = User.username
        self.login_password = User.login_password

conn = sqlite3.connect('firefox_passwords.db')