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
    return Credentials.credential_exist(name)

def show_credentials_list(password):
    return Credentials.display_credentials(password)


def create_generated_password(name):
    password = Credentials.generate_password()
    return password



def main():
    print('''
    ********** Welcome to Password Manager! ********** \n
    Use the provided codes below to navigate through the application.
    ''')

    while True:
        print('''
        Select: \n
        ca - To create an account \n 
        da - To display a list of existing accounts \n 
        li - To login to your account \n 
        ex - To exit the app
        ''')

        code = input("Enter code: ").lower()

        if code == "ca":
            print("\n")  
            print("Create a new account on Password Manager")
            print("**"*30)
            # print("Enter your full name:")
            full_name = input("Enter your full name: ")
            # print("Enter Password:")
            password = input("Enter Password: ")

            # creating a new account and saving it
            save_user_account(create_new_user(full_name, password))

            print("\n")
            print(f'''Hello {full_name} You have successfully created a new account on Password Manager.\n''' )
            print("Do you wish to continue?")

        elif code == "da":
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
            print("Login to your Password Manager account \n")
            # print("Enter your full name: ")
            full_name = input("Enter your full name: ")

            # print("Enter your password: ")
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
                    print('''
                    Select: \n
                    cnc - To create a new credential. \n 
                    dec - To display a list of existing credentials. \n 
                    cgp - To create credential with application-generated password. \n
                    del - To delete credentials account. \n  
                    ex - To exit your credentials account.
                    ''')

                    code = input("Enter code: ").lower()

                    if code == "cnc":
                        print("\n")
                        print("Create a New Credential")
                        print("**"*30)
                        # print("Credential Name: ")
                        credential_name = input("Credential Name: ")

                        # print("Credential Password: ")
                        credential_password = input("Credential Password: ")


                        # creating and saving new credentials
                        save_new_credential(generate_new_credential(password, credential_name, credential_password))

                        print("\n")
                        print(f"Credetials for {credential_name} successfully created")
                        print("\n") 
                    
                    elif code == "dec":
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
                    
                    elif code == "cgp":
                        print("\n") 
                        print("Create a New Credential")
                        print("**"*30)

                        # print("Credential Name: ")
                        credential_name = input("Credential Name: ")

                        # save new credential with app-generated password 
                        save_new_credential(Credentials(password, credential_name, (create_generated_password(credential_name))))
                        print("\n")
                        print(f"Credetials for {credential_name} successfully created")
                        print("\n") 


                    elif code == "ex":
                        print(f"{full_name}, you have exited from your account")
                        break
                    else:
                        print(f" Invalid code {code}, Try Again")

        elif code == "ex":
            print("Goodbye")
            break
        
        else:
            print("You entered a wrong code, Try Again.")

if __name__ == '__main__':
    main()



                                




            
                    