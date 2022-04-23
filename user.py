from credentials import Credentials

class User:
    users = []

    def __init__(self, full_name, password):
        self.full_name = full_name
        self.password = password
        
