from random import choice
import string 

class User:
    '''
    User class that creates instances of user accounts on the app
    '''
    
    # An empty list of users
    users = []


    def __init__(self, full_name, password):
        '''
        Method that defines and initializes the properties of each user object
        '''
        self.full_name = full_name
        self.password = password

    
    # Saving a user account
    def save_user(self):
        '''
        Function that saves a created user account to the users list 
        '''
        User.users.append(self)

    # Displaying users
    @classmethod
    def display_user(cls):
        '''
        Function that retuns a list of all users
        '''
        return cls.users

    # User login 
    @classmethod
    def login(cls, name, password):
        '''
        Function that lets users to login to their accounts on the app
        '''
        for user in cls.users:
            if user.full_name == name and user.password == password:
                return Credentials.credentials
            return False 

    # Finding credentials
    @classmethod
    def find_credential(cls, name):
        '''
        Function that checks if the credentials are correctly recorderd 
        '''
        for credential in Credentials.credentials:
            if credential.credential_name == name:
                return True
            return False 
    
    # Check if a user exists
    @classmethod
    def check_user_exist(cls, name):
        '''
        Function that checks if a user exists in the users list
        '''
        for user in cls.users:
            if user.full_name == name:
                return True
            return False 



class Credentials:
    '''
    Credentials class that creates credentials for the user 
    '''
    credentials = []
    def __init__(self, user_password, credential_name, credential_password):
        '''
        Method that defines the properties of the user
        
        Args:
            credential_name: name of the account 
            credential_password: password for the account
        '''
        self.user_password = user_password
        self.credential_name = credential_name
        self.credential_password = credential_password

    # Saving credential
    def save_credential(self):
        '''
        Function that adds the credentials created by user to the credentials list
        '''
        Credentials.credentials.append(self)
    
    # Deleting a credential
    def delete_credential(self):
        '''
        Function that removes a credential from the credentials list
        '''
        Credentials.credentials.remove(self)

    # Generating random password 
    @classmethod
    def generate_password(cls):
        '''
        Function that generates a random password for a credential entered by a user
        '''
        size = 10
        # generating random alphanumeric passoword
        genpassword = string.ascii_uppercase + string.digits + string.ascii_lowercase 
        # creating password
        password = ''.join(choice(genpassword) for num in range(size))
        return password

    # Displaying a list of credentials
    @classmethod
    def display_credentials(cls, password):
        '''
        Function that returns a list of all credentials for the user
        '''
        user_credential_list = []

        for credential in cls.credentials:
            if credential.user_password == password:
                user_credential_list.append(credential)
        return user_credential_list

    
    # Checking if a credential exist
    @classmethod
    def credential_exist(cls, name):
        '''
        Function that checks whether the credential with the name entered is already existing in the credentials list
        '''
        for credential in cls.credentials:
            if credential.credential_name == name:
                return True 
            return False 

