import os
import subprocess
from modules.info_gathering import InfoGathering
from modules.dos import DOSAttack
from modules.brute_force import BruteForce
from modules.sql_injection import SQLInjection
from modules.ping_traceroute import run_ping_traceroute
from colorama import init, Fore, Style

init(autoreset=True)

def clear_console():
    """Clears the terminal screen."""
    if os.name == 'nt':
        subprocess.call('cls', shell=True)
    else:
        subprocess.call('clear', shell=True)

def main():
    while True:
        print(f"{Style.BRIGHT}{Fore.CYAN}Welcome to the Ethical Hacking Tool{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}1. Website Information Gathering")
        print(f"{Fore.YELLOW}2. Ping and Traceroute")
        print(f"{Fore.YELLOW}3. Brute Force Attack")
        print(f"{Fore.YELLOW}4. SQL Injection Testing")
        print(f"{Fore.YELLOW}5. DOS/DDoS Attacks")
        print(f"{Fore.YELLOW}6. Exit")

        choice = input(f"{Fore.GREEN}Select an option: {Style.RESET_ALL}")

        if choice == "1":
            domain = input(f"{Fore.GREEN}Enter the domain (e.g., example.com): {Style.RESET_ALL}")
            info = InfoGathering(domain)
            info.run()
        elif choice == "2":
            print(f"{Fore.CYAN}Ping and Traceroute")
            run_ping_traceroute()
        elif choice == "3":
            print(f"{Fore.CYAN}Starting Brute Force Attack...")
            brute = BruteForce()
            brute.run()
        elif choice == "4":
            print(f"{Fore.CYAN}Testing for SQL Injection...")
            sql = SQLInjection()
            sql.run()
        elif choice == "5":
            print(f"{Fore.CYAN}Starting DOS/DDoS Attack...")
            dos = DOSAttack()
            dos.run()
        elif choice == "6":
            print(f"{Fore.GREEN}Exiting the program. Goodbye!")
            break
        else:
            print(f"{Fore.RED}Invalid choice.")

        input(f"{Fore.MAGENTA}Press Enter to return to the main menu...{Style.RESET_ALL}")
        clear_console()

if __name__ == "__main__":
    clear_console()
    main()
