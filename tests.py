import unittest
from user_credentials import User, Credentials


class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    ''' 

    def setUp(self):
        '''
        Set up method to run before each test cases. 
        '''

        # new user object
        self.new_user = User("Robert Kirui","Rob@012345!")
    
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run. 
        '''
        User.users = []


    def test_init(self):
        '''
        Test case to test if the object is initialised correctly
        '''
        self.assertEqual( self.new_user.full_name, "Robert Kirui" )
        self.assertEqual( self.new_user.password, "Rob@012345!" )


    def test_save_user(self):
        '''
        Test case to test if the user is saved into the users list
        '''

        # Save new user
        self.new_user.save_user()

        self.assertEqual( len(User.users), 1 )


    def test_find_credential(self):
        '''
        Test case to test if the User module is importing from Credential module
        '''

        # Save the new user
        self.new_user.save_user()

        test_user = User("Robert Kirui", "Rob@012345!")

        test_user.save_user()

        credential_found = User.find_credential("Slack")

        self.assertEqual( credential_found, True )


    def test_login(self):
        '''
        Test case to test if users can login to their account 
        '''

        # Save the new user
        self.new_user.save_user()

        test_user = User("Robert Kirui", "Rob@012345!")

        test_user.save_user()

        found_credential = User.login("Robert Kirui", "Rob@012345!")

        self.assertEqual(found_credential,  Credentials.credentials )   
    

    def test_display_user(self):
        '''
        Test case to test if a user can see a list of all the users saved
        '''
        self.assertEqual( User.display_user(), User.users )

        
    def test_check_user_exist(self):
        '''
        Test to check if we can return a boolean if we can't find the user
        '''
        
        # Save the new user
        self.new_user.save_user()

        test_user = User("Robert Kirui", "Rob@012345!")

        test_user.save_user()
        
        # use contact exist method
        user_exists = User.check_user_exist("Robert Kirui")
        
        self.assertTrue(user_exists)




class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases. 
        '''

        # Create credential object
        self.new_credential = Credentials("RK","Slack","098765") 


        Credentials.credentials = []


    def test_init(self):
        '''
        Test case to test if the object is initialised correctly
        '''
        self.assertEqual( self.new_credential.user_password, "RK")
        self.assertEqual( self.new_credential.credential_name, "Slack" )
        self.assertEqual( self.new_credential.credential_password, "098765" )

    def test_save_credential(self):
        '''
        Test case to test if the user object is saved into the user list
        '''
        # Saving new credential
        self.new_credential.save_credential()

        self.assertEqual( len(Credentials.credentials), 1)

    def test_generate_password(self):
        '''
        Test case to test if a user can log into their credentials
        '''
        
        generated_password = self.new_credential.generate_password()

        self.assertEqual( len(generated_password), 10)   
    
    def test_display_credentials(self):
        '''
        Test case to test if a user can see a list of all the credentials saved
        '''

        # Saving new credential
        self.new_credential.save_credential()

        test_credential = Credentials("RK","Twitter","@myTwitter055")

        test_credential.save_credential()
        
        self.assertEqual( len(Credentials.display_credentials("RK")) , 2)
        
    def test_credential_exist(self):
        
        '''
        Test to check if we can return a boolean if we can't find the credential
        '''

        # Save the new credential
        self.new_credential.save_credential()

        test_credential = Credentials("RK","Slack","098765")
        test_credential.save_credential()
        
        # use contact exist method
        found_credential = Credentials.credential_exist("Slack")
        self.assertTrue(found_credential, True) 

if __name__ == '__main__':
    unittest.main()