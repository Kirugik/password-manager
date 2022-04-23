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
    def display_credentials(cls, password):
        '''
        The display_credentials() method returns the list of credentials for the user. It takes user password as a parameter.
        '''
        user_credential_list = []

        for credential in cls.credentials:
            if credential.user_password == password:
                user_credential_list.append(credential)
        return user_credential_list
