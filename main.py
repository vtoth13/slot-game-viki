import random 
from tkinter.tix import COLUMN # Importing COLUMN from tkinter.tix module
from colorama import Fore, Back, Style # Importing color constants from colorama module
from colorama import init # Importing color initialization function from colorama module
init(autoreset=True) # Initializing colorama to automatically reset color settings after each print

MAX_LINES = 3 # Maximum number of lines to bet on
MAX_BET = 100 # Maximum bet amount
MIN_BET = 1 # Minimum bet amount

ROWS = 3 # Number of rows in the slot machine
COLS = 3 # Number of columns in the slot machine

# Dictionary defining the count of each symbol in the slot machine
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

# Dictionary defining the value of each symbol in the slot machine
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_winnings(columns, lines, bet, values):
    """
    Function to check the winnings based on the combination of symbols in the columns.

    Args:
        columns (list of lists): Represents the columns of the slot machine.
        lines (int): Number of lines being bet on.
        bet (int): Bet amount on each line.
        values (dict): Dictionary representing the value of each symbol.

    Returns:
        tuple: A tuple containing the total winnings and the list of winning lines.
    """
    winnings = 0 # Initialize total winnings to 0
    winning_lines = [] # List to store the winning lines
    # Iterate over each line
    for line in range(lines):
        symbol = columns[0][line]  # Get the symbol in the first column of the current line
        # Iterate over each column to check if symbols in the line are the same
        for column in columns:
            symbol_to_check = column[line] # Get the symbol in the current column of the current line
            if symbol != symbol_to_check: # If symbols don't match, break the loop
                break
        else: # If symbols match in all columns for the current line
            winnings += values[symbol] * bet # Add winnings based on the value of the symbol
            winning_lines.append(line + 1) # Append the winning line to the list

    return winnings, winning_lines # Return total winnings and winning lines


def get_slot_machine_spin(rows, cols, symbols):
    """
    Function to simulate a spin of the slot machine.

    Args:
        rows (int): Number of rows in the slot machine.
        cols (int): Number of columns in the slot machine.
        symbols (dict): Dictionary representing the count of each symbol.

    Returns:
        list of lists: Represents the result of the spin (symbols in each column).
    """
    all_symbols = [] # List to store all symbols
    # Iterate over each symbol and its count, and append it to all_symbols list
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = [] # List to store columns of the slot machine
    # Iterate over each column
    for _ in range(cols):
        column = [] # List to store symbols in the current column
        current_symbols = all_symbols[:] # Create a copy of all_symbols list
        # Iterate over each row
        for _ in range(rows):
            value = random.choice(current_symbols) # Choose a random symbol from current_symbols
            current_symbols.remove(value) # Remove the chosen symbol from current_symbols
            column.append(value) # Append the chosen symbol to the column

        columns.append(column) # Append the column to the list of columns

    return columns # Return the list of columns representing the spin result


def print_slot_machine(columns):
    """
    Function to print the result of the slot machine spin.

    Args:
        columns (list of lists): Represents the columns of the slot machine.
    """
    for row in range(len(columns[0])): # Iterate over each row
        for i, column in enumerate(columns): # Iterate over each column
            if i != len(columns) - 1:
                print(column[row], end=" | ") # Print symbol in the current column followed by '|'
            else:
                print(column[row], end="") # Print symbol in the last column of the row

        print() # Print a newline after printing symbols of all columns in the row


def deposit():
    """
    Function to get the deposit amount from the user.

    Returns:
        int: Deposit amount entered by the user.
    """
    while True: # Infinite loop until valid input is received
        amount = input(Fore.GREEN + Style.BRIGHT + "What would you like to deposit? $\n")
        if amount.isdigit(): # Checking if input is a digit
            amount = int(amount) # Converting input to an integer
            if 0 < amount <= 500: # Validating if input is within the range of 1 to MAX_LINES
                break
            else:
                print(Fore.RED + Style.BRIGHT + 'Amount must be between 1 and 500.') # Prompting the user if the amount is out of range
        else:
            print(Fore.RED + Style.BRIGHT + 'Please enter a number.') # Prompting for a numeric input

    return amount # Returning the validated deposit amount


# Function to prompt the user to input the number of lines to bet on
def get_number_of_lines():
    while True:
        lines = input(
            f"Enter the number of lines to bet on (1-{MAX_LINES})? \n")
        if lines.isdigit(): # Checking if input is a digit
            lines = int(lines)
            if 1 <= lines <= MAX_LINES: # Validating if input is within the range of 1 to MAX_LINES
                break
            else:
                print(Fore.RED + Style.BRIGHT + 'Please enter a valid number.') # Prompting for a valid number within the specified range
        else:
            print(Fore.RED + Style.BRIGHT + 'Please enter a number.') # Prompting for a numeric input

    return lines


# Function to prompt the user to input the bet amount for each line
def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $\n")
        if amount.isdigit(): # Checking if input is a digit
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET: # Validating if input is within the range of MIN_BET to MAX_BET
                break
            else:
                print(Fore.RED + Style.BRIGHT + f"Amount must be between ${MIN_BET} - ${MAX_BET}.") # Prompting for a valid amount within the specified range
        else:
            print(Fore.RED + Style.BRIGHT + 'Please enter a number.') # Prompting for a numeric input

    return amount


# Function to simulate the spin of the slot machine and calculate the winnings
def spin(balance):
    """
    Function to simulate the spin of the slot machine and calculate the winnings.

    Args:
        balance (int): Current balance of the player.

    Returns:
        int: Net winnings after deducting the total bet amount.
    """
    lines = get_number_of_lines() # Get the number of lines to bet on
    while True:
        bet = get_bet() # Get the bet amount on each line
        total_bet = bet * lines # Calculate the total bet amount

        if total_bet > balance: # Check if total bet exceeds balance
            print(
                Fore.YELLOW + Style.BRIGHT + f"You don't have enough to bet that amount, your current balance is: ${balance}")
            return False
        else:
            break

    print(
        f"You are betting ${bet} on {lines} lines. Total bet is equal to ${total_bet}.")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count) # Simulate the spin of the slot machine
    print_slot_machine(slots) # Print the result of the spin
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value) # Calculate winnings
    print(Fore.GREEN + Style.BRIGHT + f"You won ${winnings}.") # Print total winnings
    print(Fore.WHITE + Style.BRIGHT + f"You won on lines:", *winning_lines) # Print winning lines
    return winnings - total_bet # Return net winnings after deducting the total bet amount


def main():
    """
    Main function to control the flow of the slot machine game.
    """
    balance = deposit() # Get the initial deposit amount from the player
    while balance > 0: # Continue playing as long as the balance is positive
        print(Fore.YELLOW + f"Current balance is ${balance}.") # Print current balance
        answer = input(f"Press Enter to play {Style.DIM}(Q to Quit){Style.RESET_ALL}: \n") # Prompt user to play or quit
        if answer == "q": # Check if user wants to quit
            break
        balance += spin(balance) # Simulate a spin of the slot machine and update balance accordingly
    
    print(Fore.BLUE + f"Game over! You left with ${balance}") # Print final message when game is over

main() # Execute the main function to start the game