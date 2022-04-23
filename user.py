from credentials import Credentials

class User:
    users = []

    def __init__(self, full_name, password):
        self.full_name = full_name
        self.password = password

    
    def save_user(self):
        User.users.append(self)

    @classmethod
    def display_user(cls):
        return cls.users

    @classmethod
    def login(cls, name, password):
        for user in cls.users:
            if user.full_name == name and user.password == password:
                return Credentials.credentials
            return False 

    
    @classmethod
    def find_credential(cls, name):
        for credential in Credentials.credentials:
            if credential.credential_name == name:
                return True
            return False 
    
    @classmethod
    def check_user_exist(cls, name):
        for user in cls.users:
            if user.full_name == name:
                return True
            return False 
