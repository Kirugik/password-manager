from user import User
from credentials import Credentials

def create_new_user(full_name, password):
    new_user = User(full_name, password)
    return new_user


def save_user_account(user):
    user.save_user()

def show_users_list(name):
    return User.check_user_exist(name)

def account_login(name, password):
    login = User.login(name, password)
    if login != False:
        return User.login(name, password)

def display_users():
    return User.display_user