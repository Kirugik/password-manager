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
    return User.display_user()

def generate_new_credential(password, account_name, account_password):
    new_credential = Credentials(password, account_name, account_password)
    return new_credential

def save_new_credential(credential):
    credential.save_credential()

def check_existing_credentials(name):
    return Credentials.credential_exist(name)\

def show_credentials_list(password):
    return Credentials.display_credentials(password)


# def create_generated_password(name):
#     password = Credentials.generate_password()
#     return password



def main():
    print('''
    ********** Welcome!!!!! ********** \n
    Use the provided codes below for navigation.
    ''')

    while True:
        print('''
        CODES: \n
        ca - To create an account \n 
        da - To display a list of existing accounts \n 
        li - To login to your account \n 
        ex - To exit the app
        ''')

        code = input("Enter code:").lower()

        if code == "ca":
            print('''
            You are about to Create a New Account \n
            *************************************************** \n
            ''')
            print("Enter Your Full Name:")
            full_name = input()

            print("Enter Password:")
            password = input()

            # creating a new account and saving it
            save_user_account(create_new_user(full_name, password))

            print(f'''Hello {full_name} You have successfully Created a new account on Password Manager.\n''' )
            print("Do you wish to continue?")

        elif code == "da":
            if display_users():
                print('''
                List of Current Password Manager Users: \n
                ***************************************************
                ''')

                for user in display_users():
                    print(f"{user.full_name}")
                    print('''
                    ***************************************************
                    ''')
            else:
                print("Nobody is currently using Password Manager")

        elif code =="li":
            print("You are about to Login to your Password Manager account \n")
            print("Enter your full name:")
            full_name = input()

            print("Enter your password:")
            password = input()

            if account_login(full_name, password) == None:
                print("User account does not exist. Create a new account")
            
            else:
                account_login(full_name, password)
                print(f'''{full_name} You have successfully logged in \n
                Use the codes below to navigate''')

                while True:
                    print('''
                    CODES: \n
                    ca - To create an account \n 
                    da - To display a list of existing accounts \n 
                    li - To login to your account \n 
                    ex - To exit the app
                    ''')

                    code = input().lower()

                    if code == "ca":
                        print("Create a New Credential:")
                        print("*******************************************")

                        print("Credential Name:")
                        credential_name = input()

                        print("Credential Password:")
                        credential_password = input()

                        # creating and saving new credentials
                        save_new_credential(generate_new_credential(password, account_name, account_password))

                        print(f"Credetials for {account_name} Successfully created")
                    
                    elif code == "da":
                        if show_credentials_list(password):
                            print(f"Credentials for {full_name}:")
                            print("*******************************************")

                            for credential in show_credentials_list(password):
                                print(f"Name of Account: {credential.account_name}")
                                print(f"Password: {credential.account_password}")
                                print("*******************************************") 
                        else:
                            print(f"{full_name} You do not have any credentials at the moment")
                    
                    elif code == "ex":
                        print(f"You are exiting your account, {full_name}")
                        break
                    else:
                        print(f" Invalid code {code}, Try Again")

        elif code == "ex":
            print(f"Goodbye {full_name}")
            break
        
        else:
            print("You entered a wrong code, Try Again")

if __name__ == '__main__':
    main()



                                




            
                    