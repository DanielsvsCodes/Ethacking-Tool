from colorama import init, Fore, Style
from EthackingApp.modules.miscellaneous_functions.dark_web_scraper import DarkWebScraper
from EthackingApp.modules.miscellaneous_functions.data_stealer import DataStealer
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
        print(f"{Fore.YELLOW}2. Data Stealer")
        print(f"{Fore.RED}3. Back to Main Menu")

        choice = input(f"{Fore.GREEN}Select an option: {Style.RESET_ALL}")

        if choice == "1":
            clear_console()
            url = input(f"{Fore.GREEN}Enter the .onion URL to scrape: ").strip()
            try:
                scraper = DarkWebScraper(url)

                renew_choice = input(f"{Fore.GREEN}Do you want to renew the Tor circuit before scraping? (yes/no): ").strip().lower()
                if renew_choice == 'yes':
                    scraper.renew_tor_connection()

                scraper.run()
            except Exception as e:
                print(f"{Fore.RED}An error occurred while running the Dark Web Scraper: {e}")
        elif choice == "2":
            clear_console()
            data_stealer = DataStealer()
            data_stealer.run()
        elif choice == "3":
            break
        else:
            print(f"{Fore.RED}Invalid choice.")
        
        input(f"{Fore.MAGENTA}Press Enter to return to the [Miscellaneous] tools menu...{Style.RESET_ALL}")
        clear_console()

if __name__ == "__main__":
    miscellaneous_menu()
