from colorama import init, Fore, Style
from EthackingApp.modules.miscellaneous_functions.dark_web_scraper import run_dark_web_scraper
from EthackingApp.modules.miscellaneous_functions.log_analysis import run_log_analysis
import os
import subprocess

init(autoreset=True)

def clear_console():
    """Clears the terminal screen."""
    if os.name == 'nt':
        subprocess.call('cls', shell=True)
    else:
        subprocess.call('clear', shell=True)

def miscellaneous_menu():
    """Menu for Miscellaneous Tools"""
    while True:
        print(f"{Style.BRIGHT}{Fore.CYAN}Miscellaneous Tools{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}1. Dark Web Scraper")
        print(f"{Fore.YELLOW}2. Log File Analysis")
        print(f"{Fore.RED}3. Back to Main Menu")

        choice = input(f"{Fore.GREEN}Select an option: {Style.RESET_ALL}")

        if choice == "1":
            run_dark_web_scraper()
        elif choice == "2":
            run_log_analysis()
        elif choice == "3":
            break
        else:
            print(f"{Fore.RED}Invalid choice.")
        
        input(f"{Fore.MAGENTA}Press Enter to return to the miscellaneous tools menu...{Style.RESET_ALL}")
        clear_console()
