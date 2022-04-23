from credentials import Credentials

class User:
    users = []

    def __init__(self, full_name, password):
        self.full_name = full_name
        self.password = password

    
    def save_user(self):
        User.users.append(self)

    @classmethod
    def display_users(cls):
        return cls.users
        
    @classmethod
    def login(cls, name, pword):
        for user in cls.users:
            if user.full_name == name and user.password == pword:
                return Credentials.credentials
            return False 


