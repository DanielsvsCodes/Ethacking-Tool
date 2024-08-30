from colorama import init, Fore, Style
from modules.social_engineering_functions.phishing_sim import run_phishing_sim
from modules.social_engineering_functions.clipboard_hijacking import run_clipboard_hijacking
import os
import subprocess

init(autoreset=True)

def clear_console():
    """Clears the terminal screen."""
    if os.name == 'nt':
        subprocess.call('cls', shell=True)
    else:
        subprocess.call('clear', shell=True)

def social_engineering_menu():
    """Menu for Social Engineering Tools"""
    while True:
        print(f"{Style.BRIGHT}{Fore.CYAN}Social Engineering Tools{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}1. Phishing Simulation")
        print(f"{Fore.YELLOW}2. Clipboard Hijacking")
        print(f"{Fore.RED}3. Back to Main Menu")

        choice = input(f"{Fore.GREEN}Select an option: {Style.RESET_ALL}")

        if choice == "1":
            run_phishing_sim()
        elif choice == "2":
            run_clipboard_hijacking()
        elif choice == "3":
            break
        else:
            print(f"{Fore.RED}Invalid choice.")
        
        input(f"{Fore.MAGENTA}Press Enter to return to the social engineering tools menu...{Style.RESET_ALL}")
        clear_console()
