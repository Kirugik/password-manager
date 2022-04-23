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

def generate_new_credential(password, account_name, account_password):
    new_credential = Credentials(password, account_name, account_password)
    return new_credential

def save_new_credential(credential):
    credential.save_credential()

def check_existing_credentials(name):
    return Credentials.credential_exist(name)

def show_credentials_list(password):
    return Credentials.display_credentials(password)


def create_generated_password(name):
    password = Credentials.generate_password()
    return password
