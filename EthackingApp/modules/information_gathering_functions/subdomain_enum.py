import os
import dns.resolver
from colorama import init, Fore
from urllib.parse import urlparse
import re

init(autoreset=True)

class SubdomainEnumerator:
    def __init__(self, domain, wordlist_path=None):
        """Initialize the SubdomainEnumerator with a domain and wordlist."""
        self.domain = self.sanitize_domain(domain)
        self.wordlist_path = wordlist_path if wordlist_path else os.path.join('EthackingApp', 'resources', 'default_wordlist.txt')

    def sanitize_domain(self, domain):
        """Sanitize and validate the domain input."""
        parsed_url = urlparse(domain)
        sanitized_domain = parsed_url.netloc if parsed_url.netloc else parsed_url.path
        if not self.validate_domain(sanitized_domain):
            print(f"{Fore.RED}Error: Invalid domain. Please enter a valid domain (e.g., example.com).{Fore.RESET}")
            return None
        return sanitized_domain

    def validate_domain(self, domain):
        """Validate the domain to ensure it's a proper domain name."""
        domain_regex = re.compile(
            r'^(?:[a-zA-Z0-9]'
            r'(?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+'
            r'[a-zA-Z]{2,6}$'
        )
        return domain_regex.match(domain)

    def load_wordlist(self):
        """Load subdomains from the provided wordlist file."""
        try:
            with open(self.wordlist_path, 'r') as file:
                subdomains = file.read().splitlines()
            return subdomains
        except FileNotFoundError:
            print(f"{Fore.RED}Wordlist file not found: {self.wordlist_path}{Fore.RESET}")
            return []

    def check_subdomain(self, subdomain):
        """Check if a subdomain exists by performing a DNS query."""
        try:
            dns.resolver.resolve(subdomain, 'A')
            return True
        except dns.resolver.NXDOMAIN:
            return False
        except dns.resolver.NoAnswer:
            return False
        except dns.exception.Timeout:
            print(f"{Fore.YELLOW}DNS query for {subdomain} timed out.{Fore.RESET}")
            return False
        except Exception as e:
            print(f"{Fore.RED}Error checking subdomain {subdomain}: {e}{Fore.RESET}")
            return False

    def run(self):
        """Run the subdomain enumeration."""
        if not self.domain:
            return

        subdomains = self.load_wordlist()
        if not subdomains:
            return

        print(f"{Fore.CYAN}Starting subdomain enumeration for {self.domain}...{Fore.RESET}")
        found_subdomains = []

        for subdomain in subdomains:
            full_subdomain = f"{subdomain}.{self.domain}"
            if self.check_subdomain(full_subdomain):
                print(f"{Fore.GREEN}Found subdomain: {full_subdomain}{Fore.RESET}")
                found_subdomains.append(full_subdomain)

        if found_subdomains:
            print(f"{Fore.CYAN}Subdomain enumeration completed. Found {len(found_subdomains)} subdomains:{Fore.RESET}")
            for sub in found_subdomains:
                print(f" - {sub}")
        else:
            print(f"{Fore.YELLOW}No subdomains found for {self.domain}.{Fore.RESET}")


if __name__ == "__main__":
    domain = input("Enter the domain to enumerate subdomains for (e.g., example.com): ").strip()

    use_default = input("Do you want to use the default wordlist? (y/n): ").strip().lower()
    if use_default == 'y':
        wordlist_path = None
    else:
        wordlist_path = input("Enter the path to your subdomain wordlist file (press [ENTER] to use the default list): ").strip()
        if not os.path.isfile(wordlist_path):
            print(f"{Fore.RED}Error: The specified wordlist file does not exist.{Fore.RESET}")
            wordlist_path = None

    enumerator = SubdomainEnumerator(domain, wordlist_path)
    enumerator.run()
