import os
from colorama import Fore, Back
from colorama import init
init(autoreset=True)

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