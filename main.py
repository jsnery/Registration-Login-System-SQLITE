import sqlite3
from pathlib import Path
from abc import ABC, abstractmethod

DIR = Path(__file__).parent
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
        self.database.close()
        return True
        

    def login(self) -> bool:
        ...
    
usr = input('User: ')
pwd = input('Password: ')

system = LoginSystem(usr, pwd)
system.registration()