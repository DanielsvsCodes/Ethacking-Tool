import dns.resolver
from colorama import init, Fore

init(autoreset=True)

class SubdomainEnumerator:
    def __init__(self, domain, wordlist_path):
        """Initialize the SubdomainEnumerator with a domain and wordlist."""
        self.domain = domain
        self.wordlist_path = wordlist_path

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
