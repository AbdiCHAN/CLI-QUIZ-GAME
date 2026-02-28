# CLI entry point for CLI Quiz Game
# This file runs the program and controls the main menu

from models.game import Game  # Import the Game class from the models/game.py file

def main():
    game = Game()  # Create an instance (object) of the Game class

    while True:  # Start an infinite loop so the menu keeps showing until user exits
        print("\n=== CLI Quiz Game ===")  # Print the game title
        print("1. Register")  # Option 1: Register a new user
        print("2. Login")  # Option 2: Login an existing user
        print("3. Play Quiz (7 questions)")  # Option 3: Start the quiz
        print("4. Exit")  # Option 4: Exit the program

        choice = input("Choose option: ")  # Ask the user to choose an option

        if choice == "1":  # If user selects option 1
            username = input("Enter username: ")  # Ask for username
            password = input("Enter password: ")  # Ask for password
            game.register(username, password)  # Call the register method from Game class

        elif choice == "2":  # If user selects option 2
            username = input("Enter username: ")  # Ask for username
            password = input("Enter password: ")  # Ask for password
            game.login(username, password)  # Call the login method from Game class

        elif choice == "3":  # If user selects option 3
            game.play_quiz()  # Call the play_quiz method from Game class

        elif choice == "4":  # If user selects option 4
            print("Goodbye!")  # Print exit message
            break  # Stop the loop and exit the program

        else:  # If user enters something invalid
            print("Invalid choice. Try again.")  # Show error message


# This ensures the main() function runs only when this file is executed directly
if __name__ == "__main__":
    main()  # Call the main function to start the program