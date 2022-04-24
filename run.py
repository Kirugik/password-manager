from user import User, Credentials

# Creating a new user
def create_new_user(full_name, password):
    '''
    Function to create a new user account on password manager

    Args:
        full_name = Full name of the new user creating the account
        password = Password of the account being created for the new user
    '''
    new_user = User(full_name, password)
    return new_user

# Saving the new user account
def save_user_account(user):
    '''
    Function to save the new user account that has just been created

    Args:
        user = the name of the user account to be saved
    '''
    user.save_user()

# Displaying a list of all user accounts
def show_users_list(name):
    '''
    Function to display a list of all users currently registered
    '''
    return User.check_user_exist(name)

# Logging in to the account
def account_login(name, password):
    '''
    Function that lets a user of an existing account to log into the app
    
    Args:
         name = full name of the user
         password = password of the account 
    '''
    login = User.login(name, password)
    if login != False:
        return User.login(name, password)

# Displaying a list of all user accounts
def display_users():
    '''
    Function that returns a list of all users
    '''
    return User.display_user()

# Creating a new credential
def generate_new_credential(password, account_name, account_password):
    '''
    Function that creates a new credential account with name of the credential and password

    Args:
        password = the password for the user account 
        account_name = name of the credential account e.g Twitter
        account_password = the password of the credentiala account
    '''
    new_credential = Credentials(password, account_name, account_password)
    return new_credential

# Saving the new credential
def save_new_credential(credential):
    '''
    Function to save the new credential that has been created
    '''
    credential.save_credential()

# Checking for a credential
def check_existing_credentials(name):
    '''
    Function that checks if a given credential already exists in the system

    Args:
        name = name of the credential e.g. Slack
    '''
    return Credentials.credential_exist(name)

# Displaying existing credentials
def show_credentials_list(password):
    '''
    Function to display a list of all existing credentials for the user
    '''
    return Credentials.display_credentials(password)

# Generating a password of a credential
def create_generated_password(name):
    '''
    Function that generates a random password for a credential entered by a user

    Args: 
        name = name of the credential
    '''
    password = Credentials.generate_password()
    return password

# Deleting a credential
def delete_credential(name):
    '''
    Function that deletes a credential and updates the credentials list
    '''
    name.delete_credential()



def main():
    '''
    Function that runs the entire application 
    '''

    print('''
    ********** Welcome to Password Manager! ********** \n
    Use the provided codes below to navigate through the application.
    ''')

    while True:
        '''
        While loop at the entry of the application that allows users to choose 
        what they want to do.
        '''

        print('''
        Select: \n
        ca - To create an account \n 
        da - To display a list of existing accounts \n 
        li - To login to your account \n 
        ex - To exit the app
        ''')


        # Getting user to input codes 
        code = input("Enter code: ").lower()

        if code == "ca":
            '''
            Option that lets the user to create an account
            '''

            print("\n")  
            print("Create a new account on Password Manager")
            print("**"*30)
            full_name = input("Enter your full name: ")
            password = input("Enter Password: ")

            # creating a new account and saving it
            save_user_account(create_new_user(full_name, password))

            print("\n")
            print(f'''Hello {full_name} You have successfully created a new account on Password Manager.\n''' )
            print("Do you wish to continue?")

        elif code == "da":
            '''
            Option that displays a list of all existing accounts 
            '''
            if display_users():
                print("\n") 
                print("List of Current Password Manager Users:")
                print("**"*30)

                for user in display_users():
                    print(f"{user.full_name}")
                    print("**"*30) 
            else:
                print("\n")  
                print("Nobody is currently using Password Manager")

        elif code =="li":
            '''
            Option that lets a user log in to the account using full name and password 
            '''

            print("Login to your Password Manager account \n")
            full_name = input("Enter your full name: ")
            password = input("Enter your password: ")

            if account_login(full_name, password) == None:
                print("\n") 
                print("User account does not exist. Create a new account")
            
            else:
                account_login(full_name, password)
                print("\n") 
                print(f"{full_name} You have successfully logged in")
                print("\n") 
                print("Use the codes below to navigate")

                while True:
                    '''
                    While loop that allow logged in users to choose what they want to do
                    '''

                    print('''
                    Select: \n
                    cnc - To create a new credential. \n 
                    dec - To display a list of existing credentials. \n 
                    cgp - To create credential with application-generated password. \n
                    del - To delete credentials account. \n  
                    ex - To exit your credentials account.
                    ''')

                    # Getting user to input codes 
                    code = input("Enter code: ").lower()

                    # create a new credential
                    if code == "cnc":
                        '''
                        Option for logged in user to create a new credential
                        '''

                        print("\n")
                        print("Create a New Credential")
                        print("**"*30)

                        credential_name = input("Credential Name: ")
                        credential_password = input("Credential Password: ")


                        # creating and saving new credentials
                        save_new_credential(generate_new_credential(password, credential_name, credential_password))

                        print("\n")
                        print(f"Credetials for {credential_name} successfully created")
                        print("\n") 
                    
                    # display a list of all credentials
                    elif code == "dec":
                        '''
                        Option for logged in user to display a list of all credentials  
                        '''

                        if show_credentials_list(password):
                            print("\n") 
                            print("Your Current List of Credentials")
                            print("**"*30) 

                            for credential in show_credentials_list(password):
                                print(f"Name of Account: {credential.credential_name}")
                                print(f"Password: {credential.credential_password}")
                                print("**"*30)  
                        else:
                            print(f"{full_name}, you do not have any credentials at the moment")
                    
                    # Allow app to generate password for a credential
                    elif code == "cgp":
                        '''
                        Option for a logged in user to provide a credential name and let the 
                        app generate a random password for that credential
                        '''

                        print("\n") 
                        print("Create a New Credential")
                        print("**"*30)

                        credential_name = input("Credential Name: ")

                        # save new credential with app-generated password 
                        save_new_credential(Credentials(password, credential_name, (create_generated_password(credential_name))))
                        print("\n")
                        print(f"Credetials for {credential_name} successfully created")
                        print("\n") 

                    # deleting a credential
                    elif code == "del":
                        '''
                        Option for a logged in user to delete a credential
                        '''

                        print("\n") 
                        print("Enter the account name of the credentials you want to delete")
                        account_todelete = input("Which account do you want to delete?: ")
                        if check_existing_credentials(account_todelete):
                            account_todelete = check_existing_credentials(account_todelete)
                            delete_credential(account_todelete)
                    
                    # exiting the account 
                    elif code == "ex":
                        '''
                        Option to exit the user account 
                        '''

                        print(f"{full_name}, you have exited from your account")
                        break
                    else:
                        print(f" Invalid code {code}, Try Again")

        elif code == "ex":
            '''
            Option to exit the application 
            '''
            
            print("Goodbye")
            break
        
        else:
            print("You entered a wrong code, Try Again.")

if __name__ == '__main__':
    main()



                                




            
                    