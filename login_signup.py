# Initialize empty lists to store usernames and passwords
username = []  
password = []  

# Function to handle user signup
def signup(x, y):
    """
    This function allows a new user to sign up by entering a username and password.
    The credentials are stored in the respective lists.
    """
    user = input("Enter a username: ")  # Prompt user to enter a username
    passw = input("Enter a password: ")  # Prompt user to enter a password

    # Append the credentials to the username and password lists
    username.append(user)
    password.append(passw)

    print("Signup Successful!")  # Confirmation message

# Function to handle user login
def login(x, y):
    """
    This function allows a user to log in by verifying entered credentials
    against the stored username and password lists.
    """
    login_user = input("Enter your username: ")  # Prompt user for username
    login_passw = input("Enter your password: ")  # Prompt user for password

    # Check if the entered username and password match the stored credentials
    if login_user in username and login_passw in password:
        print("Login Successful!")  # Login success message
    else:
        print("Wrong Username or Password!")  # Error message for incorrect credentials

# Main loop for user interaction
while True:
    option = input("Would you like to 'Login' or 'Signup'? ").lower()  # Prompt user for action

    if option == "signup":
        signup(username, password)  # Call signup function
        continue  # Continue the loop to allow login after signup

    elif option == "login":
        login(username, password)  # Call login function
        break  # Exit loop after login attempt

    else:
        print("Invalid option. Please enter 'Login' or 'Signup'.")  # Error message for invalid input
        continue  # Continue looping until the user enters a valid option
