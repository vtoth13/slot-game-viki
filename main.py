import random
from tkinter.tix import COLUMN
from colorama import Fore, Back, Style
from colorama import init
init(autoreset=True)

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()


def deposit():
    while True:
        amount = input(Fore.GREEN + Style.BRIGHT + "What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if 0 < amount <= 500:
                break
            else:
                print(Fore.RED + Style.BRIGHT + 'Amount must be between 1 and 500.')
        else:
            print(Fore.RED + Style.BRIGHT + 'Please enter a number.')

    return amount


def get_number_of_lines():
    while True:
        lines = input(
            f"Enter the number of lines to bet on (1-{MAX_LINES})? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(Fore.RED + Style.BRIGHT + 'Please enter a valid number.')
        else:
            print(Fore.RED + Style.BRIGHT + 'Please enter a number.')

    return lines


def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(Fore.RED + Style.BRIGHT + f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print(Fore.RED + Style.BRIGHT + 'Please enter a number.')

    return amount


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(
                Fore.YELLOW + Style.BRIGHT + f"You don't have enough to bet that amount, your current balance is: ${balance}")
            return False
        else:
            break

    print(
        f"You are betting ${bet} on {lines} lines. Total bet is equal to ${total_bet}.")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(Fore.GREEN + Style.BRIGHT + f"You won ${winnings}.")
    print(Fore.WHITE + Style.BRIGHT + f"You won on lines:", *winning_lines)
    return winnings - total_bet


def main():
    balance = deposit()
    while balance > 0:
        print(Fore.YELLOW + f"Current balance is ${balance}.")
        answer = input(f"Press Enter to play {Style.DIM}(Q to Quit){Style.RESET_ALL}: ")
        if answer == "q":
            break
        balance += spin(balance)
    
    print(Fore.BLUE + f"Game over! You left with ${balance}")

main()