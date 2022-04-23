import string 
'''
Credentials class that creates user credentials 
'''
class Credentials:
    # initialize an empty list of credentials
    credentials = []
    def __init__(self, user_password, credential_name, credential_password):
        '''
        the __init__ method defines the properties of the user. It takes the following arguments:
        credential_name: name of the account 
        credential_password: password for the account
        '''
        self.user_password = user_password
        self.credential_name = credential_name
        self.credential_password = credential_password

    def save_credential(self):
        '''
        The save_credential() method adds the credentials created by user to the credentials list.
        '''
        Credentials.credentials.append(self)

    @classmethod
    def generate_password(cls):
        # size = 10
        # generate rando alphanumeric
        # alphanum = string.ascii_uppercase + string.digits + string.ascii_lowercase 
        # create password
        # password = ''.join(choice(alphanum) for num in range(size))
        # return password

    @classmethod
    def display_credentials(cls, password):
        '''
        The display_credentials() method returns the list of credentials for the user. It takes user password as a parameter.
        '''
        user_credential_list = []

        for credential in cls.credentials:
            if credential.user_password == password:
                user_credential_list.append(credential)
        return user_credential_list

    
    @classmethod
    def credential_exist(cls, name):
        '''
        This method checks whether the credential with the name entered is already existing in the credentials list. It takes the name of the credential as an argument and returns True if credential exists and False if it does not.
        '''
        for credential in cls.credentials:
            if credential.credential_name == name:
                return True 
            return False 
