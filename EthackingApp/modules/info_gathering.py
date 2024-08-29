import requests
import socket
import whois
import dns.resolver
from urllib.parse import urlparse
from colorama import init, Fore, Style

init(autoreset=True)

class InfoGathering:
    def __init__(self, domain):
        self.domain = self.extract_domain(domain)

    def extract_domain(self, domain):
        parsed_url = urlparse(domain)
        return parsed_url.netloc if parsed_url.netloc else parsed_url.path

    def get_ip(self):
        try:
            ip_address = socket.gethostbyname(self.domain)
            print(f"{Fore.GREEN}IP Address: {ip_address}")
        except socket.gaierror:
            print(f"{Fore.RED}Error: Unable to get IP address for the domain.")

    def get_http_status(self):
        try:
            response = requests.get(f"http://{self.domain}")
            print(f"{Fore.GREEN}HTTP Status Code: {response.status_code}")
        except requests.RequestException as e:
            print(f"{Fore.RED}Error: Unable to get HTTP status for the domain. {e}")

    def get_whois_info(self):
        try:
            domain_info = whois.whois(self.domain)
            print(f"{Fore.YELLOW}WHOIS Information:")
            for key, value in domain_info.items():
                print(f"{Fore.CYAN}{key}: {value}")
        except Exception as e:
            print(f"{Fore.RED}Error: Unable to get WHOIS information. {e}")

    def get_dns_records(self):
        try:
            print(f"{Fore.YELLOW}DNS Records:")
            for record_type in ['A', 'AAAA', 'MX', 'NS', 'TXT', 'SOA']:
                try:
                    answers = dns.resolver.resolve(self.domain, record_type)
                    for answer in answers:
                        print(f"{Fore.GREEN}{record_type} Record: {answer}")
                except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
                    print(f"{Fore.RED}No {record_type} record found.")
                except Exception as e:
                    print(f"{Fore.RED}Error retrieving {record_type} record: {e}")
        except Exception as e:
            print(f"{Fore.RED}Error: Unable to get DNS records. {e}")

    def run(self):
        print(f"{Style.BRIGHT}Gathering information for: {Fore.CYAN}{self.domain}")
        self.get_ip()
        self.get_http_status()
        self.get_whois_info()
        self.get_dns_records()

if __name__ == "__main__":
    domain = input("Enter the domain (e.g., example.com): ")
    info = InfoGathering(domain)
    info.run()
