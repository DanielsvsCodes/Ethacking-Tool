from colorama import init, Fore, Style
from modules.information_gathering_functions.info_gathering import InfoGathering
from modules.information_gathering_functions.ping_traceroute import PingTraceroute
from modules.information_gathering_functions.banner_grabbing import BannerGrabbing
from modules.information_gathering_functions.subdomain_enum import SubdomainEnumerator
from modules.information_gathering_functions.geo_tracking import GeoTracking
from modules.information_gathering_functions.dns_spoofing import DNSSpoofing
from modules.information_gathering_functions.port_scanner import PortScanner
import os
import subprocess

init(autoreset=True)

def clear_console():
    """Clears the terminal screen."""
    if os.name == 'nt':
        subprocess.call('cls', shell=True)
    else:
        subprocess.call('clear', shell=True)

def information_gathering_menu():
    """Menu for Information Gathering Tools"""
    while True:
        print(f"{Style.BRIGHT}{Fore.CYAN}Information Gathering Tools{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}1. Website Information Gathering")
        print(f"{Fore.YELLOW}2. Ping and Traceroute")
        print(f"{Fore.YELLOW}3. Port Scanner")
        print(f"{Fore.YELLOW}4. Banner Grabbing")
        print(f"{Fore.YELLOW}5. Subdomain Enumeration")
        print(f"{Fore.YELLOW}6. Geolocation Tracking")
        print(f"{Fore.YELLOW}7. DNS Spoofing")
        print(f"{Fore.YELLOW}8. Back to Main Menu")

        choice = input(f"{Fore.GREEN}Select an option: {Style.RESET_ALL}")

        if choice == "1":
            domain = input(f"{Fore.GREEN}Enter the domain (e.g., example.com): {Style.RESET_ALL}")
            info = InfoGathering(domain)
            info.run()
        elif choice == "2":
            pt = PingTraceroute()
            pt.run()
        elif choice == "3":
            host = input(f"{Fore.GREEN}Enter the host to scan for open ports (e.g., example.com): {Style.RESET_ALL}")
            port_scanner = PortScanner(host)
            port_scanner.run()
        elif choice == "4":
            host = input(f"{Fore.GREEN}Enter the host to grab the banner from (e.g., example.com): {Style.RESET_ALL}")
            port = input(f"{Fore.GREEN}Enter the port number (e.g., 80): {Style.RESET_ALL}")

            banner_grabber = BannerGrabbing()

            if banner_grabber.validate_host(host) and banner_grabber.validate_port(port):
                banner_grabber.grab_banner(host, int(port))
            else:
                print(f"{Fore.RED}Invalid input. Please enter a valid host and port number.")
        elif choice == "5":
            domain = input(f"{Fore.GREEN}Enter the domain to enumerate subdomains for (e.g., example.com): {Style.RESET_ALL}")
            wordlist_path = input(f"{Fore.GREEN}Enter the path to the subdomain wordlist file: {Style.RESET_ALL}")
            sub_enum = SubdomainEnumerator(domain, wordlist_path)
            sub_enum.run()
        elif choice == "6":
            ip_address = input(f"{Fore.GREEN}Enter the IP address to track (e.g., 8.8.8.8): {Style.RESET_ALL}")
            geo_tracker = GeoTracking(ip_address)
            geo_tracker.run()
        elif choice == "7":
            target_domain = input(f"{Fore.GREEN}Enter the target domain to spoof (e.g., example.com): {Style.RESET_ALL}")
            fake_ip = input(f"{Fore.GREEN}Enter the fake IP address to redirect traffic to: {Style.RESET_ALL}")
            dns_spoofer = DNSSpoofing(target_domain, fake_ip)
            dns_spoofer.run()
        elif choice == "8":
            break
        else:
            print(f"{Fore.RED}Invalid choice.")
        
        input(f"{Fore.MAGENTA}Press Enter to return to the [Information Gathering] menu...{Style.RESET_ALL}")
        clear_console()
