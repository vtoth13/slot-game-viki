# Import necessary modules
import os
from colorama import Fore, Back, Style
from colorama import init
init(autoreset=True) # Initialize colorama to automatically reset colors


# Function to display the rules of the game
def show_rules():
    print(Back.GREEN + 'Rules:')
    print("1. Deposit money to start.")
    print("2. Choose number of lines to bet on (1-3).")
    print("3. Place a bet ($1-$100).")
    print("4. The machine spins automatically.")
    print("5. Match symbols on active lines to win.")
    print("6. Win amount depends on symbol value and bet.")
    print("7. Keep playing until balance runs out or choose to quit.")
    print("8. Have fun!")
    print(Back.CYAN + "Press Enter to go back to the main menu...")
    input()


# Function to start the game
def play_game():
    os.system('python main.py')


# Function to quit the program
def quit_program():
    print(Fore.MAGENTA + Style.BRIGHT + 'Thank you for using the program, {}. Hope to see you again!'.format(username))
    exit()


# Main function to interact with the user
def main():
    global username
    while True:
        username = input("Please enter your name: ")
        if username.strip() == '' or username.isdigit():
            print(Back.RED + Style.BRIGHT + 'Invalid username. Please enter a valid name that is not empty and does not consist of only numbers.')
        else:
            print(Fore.CYAN + Style.BRIGHT + 'Welcome, {}! '.format(username))
            break


    while True:
        print(Back.BLUE + 'Menu:')
        print("1. Rules")
        print("2. Play Game")
        print("3. Quit")
        choice = input(Fore.YELLOW + 'Please enter your choice: ' + Fore.RESET)

        # Branch based on user choice
        if choice == "1":
            show_rules()
        elif choice == "2":
            play_game()
        elif choice == "3":
            quit_program()
        else:
            print(Back.RED + Style.BRIGHT + 'Invalid choice. Please enter a number from 1 to 3.')

# Entry point of the program
if __name__ == "__main__":
    main()