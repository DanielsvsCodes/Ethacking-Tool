from colorama import init, Fore, Style
from EthackingApp.modules.network_tools_functions.port_scanner import run_port_scanner
from EthackingApp.modules.network_tools_functions.network_sniffing import run_network_sniffing
from EthackingApp.modules.network_tools_functions.wireless_tools import run_wireless_tools
import os
import subprocess

init(autoreset=True)

def clear_console():
    """Clears the terminal screen."""
    if os.name == 'nt':
        subprocess.call('cls', shell=True)
    else:
        subprocess.call('clear', shell=True)

def network_tools_menu():
    """Menu for Network Tools"""
    while True:
        print(f"{Style.BRIGHT}{Fore.CYAN}Network Tools{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}1. Port Scanning")
        print(f"{Fore.YELLOW}2. Network Sniffing")
        print(f"{Fore.YELLOW}3. Wireless Tools")
        print(f"{Fore.RED}4. Back to Main Menu")

        choice = input(f"{Fore.GREEN}Select an option: {Style.RESET_ALL}")

        if choice == "1":
            run_port_scanner()
        elif choice == "2":
            run_network_sniffing()
        elif choice == "3":
            run_wireless_tools()
        elif choice == "4":
            break
        else:
            print(f"{Fore.RED}Invalid choice.")
        
        input(f"{Fore.MAGENTA}Press Enter to return to the network tools menu...{Style.RESET_ALL}")
        clear_console()
