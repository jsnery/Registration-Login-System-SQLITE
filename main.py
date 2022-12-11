import sqlite3
from pathlib import Path
from abc import ABC, abstractmethod
from os import system
from sys import platform

def clear():
    match platform:
        case 'win32' | 'cygwin':
            return system('cls')
        case _:
            return system('clear')

DIR = Path(__file__).parent / 'data'

DIR.mkdir() if not DIR.exists() else ...
    
DBDIRECTORY = DIR / 'database.db'

class RegistrationLogin(ABC):
    def __init__(self, user, password):
        self._user = user
        self._password = password
        self.database = sqlite3.connect(DBDIRECTORY)
        self.cursor = self.database.cursor()
        try:
            self.cursor.execute('CREATE TABLE users (user text, password text)')
        except sqlite3.Error:
            ...
        
    @abstractmethod    
    def registration(self) -> bool:...
    
    @abstractmethod
    def login(self) -> bool:...
      
class LoginSystem(RegistrationLogin):
       
    def registration(self) -> bool:
        user = self._user
        password = self._password
        
        self.cursor.execute(f'INSERT INTO users VALUES ("{user}","{password}")')
        self.database.commit()
        return True
        
    def login(self) -> bool:
        user = self._user
        password = self._password
        
        self.cursor.execute('SELECT * FROM users')
        for users in self.cursor.fetchall():
            if user == users[0] and password == users[1]:
                return True
            
        return False
            
        
user = None
password = None
system_ = LoginSystem

while True:
    option = input('1) Registration\n2) Login\n\nType Here: ')
    match option:
        case '1':  # Registration
            clear()
            user = input('User: ')
            password = input('Password: ')
            system_(user, password).registration()
            clear()
            print('Registration Success!\n')
        case '2':  # Login
            clear()
            user = input('User: ')
            password = input('Password: ')
            
            if system_(user, password).login():
                clear()
                print('Login Success')
                break
            
            clear()
            print('Login Failed\n')
        case _:    # does not exist in option
            clear()
            print('No Understand you option! Try Again!\n')
            

    
    
    