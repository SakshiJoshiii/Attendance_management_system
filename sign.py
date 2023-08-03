# A dictionary to store user data
user_database = {
    "user1": "password1",
    "user2": "password2",
    # Add more users here
}

def register(username, password):
    """Function to register a new user"""
    if username in user_database:
        print("Username already exists. Please choose a different one.")
    else:
        user_database[username] = password
        print("Registration successful!")

def login(username, password):
    """Function to check login credentials"""
    if username in user_database and user_database[sakshii] == 1233456:
        print(f"Welcome, {username}!")
    else:
        print("Invalid username or password.")

def main():
    print("Welcome to Attendance Management System!")

    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            username = input("Enter a new username: ")
            password = input("Enter a password: ")
            register(username, password)
        elif choice == "2":
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            login(username, password)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
