from colorama import init, Fore, Style
from categories.information_gathering import information_gathering_menu
# from categories.vulnerability_scanning import vulnerability_scanning_menu
from categories.exploitation_tools import exploitation_tools_menu
# from categories.network_tools import network_tools_menu
# from categories.social_engineering import social_engineering_menu
# from categories.miscellaneous import miscellaneous_menu

init(autoreset=True)

def clear_console():
    """Clears the terminal screen."""
    import os
    import subprocess
    if os.name == 'nt':
        subprocess.call('cls', shell=True)
    else:
        subprocess.call('clear', shell=True)

def main():
    while True:
        print(f"{Style.BRIGHT}{Fore.CYAN}Welcome to the Ethical Hacking Tool{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}1. Information Gathering")
        print(f"{Fore.YELLOW}2. Vulnerability Scanning")
        print(f"{Fore.YELLOW}3. Exploitation Tools")
        print(f"{Fore.YELLOW}4. Network Tools")
        print(f"{Fore.YELLOW}5. Social Engineering")
        print(f"{Fore.YELLOW}6. Miscellaneous")
        print(f"{Fore.RED}7. Exit")

        choice = input(f"{Fore.GREEN}Select a category: {Style.RESET_ALL}")

        if choice == "1":
            clear_console()
            information_gathering_menu()
        # elif choice == "2":
        #     clear_console()
        #     vulnerability_scanning_menu()
        elif choice == "3":
            clear_console()
            exploitation_tools_menu()
        # elif choice == "4":
        #     clear_console()
        #     network_tools_menu()
        # elif choice == "5":
        #     clear_console()
        #     social_engineering_menu()
        # elif choice == "6":
        #     clear_console()
        #     miscellaneous_menu()
        elif choice == "7":
            print(f"{Fore.GREEN}Exiting the program. Goodbye!")
            break
        else:
            print(f"{Fore.RED}Invalid choice.")
        clear_console()

if __name__ == "__main__":
    clear_console()
    main()
