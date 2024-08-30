import socket
from urllib.parse import urlparse
from colorama import init, Fore, Style
import re

init(autoreset=True)

class BannerGrabbing:
    def __init__(self, host=None, port=None):
        """Initialize the BannerGrabbing class with optional host and port."""
        self.host = host
        self.port = port

    def grab_banner(self):
        """Grab the banner from the specified host and port."""
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(5)
            s.connect((self.host, self.port))
            s.send(b'HEAD / HTTP/1.1\r\nHost: ' + self.host.encode() + b'\r\n\r\n')
            banner = s.recv(1024)
            print(f"{Fore.GREEN}Banner from {self.host}:{self.port}:\n{banner.decode()}")
            s.close()
        except socket.error as e:
            print(f"{Fore.RED}Socket error: {e}")
        except Exception as e:
            print(f"{Fore.RED}Error: {e}")

    def sanitize_host_input(self, host):
        """Sanitize host input to extract the domain from a URL if needed."""
        parsed_url = urlparse(host)
        return parsed_url.netloc if parsed_url.netloc else parsed_url.path

    def validate_host(self, host):
        """Validate the host to ensure it's a valid domain or IP address."""
        domain_regex = re.compile(
            r'^(?:[a-zA-Z0-9]'
            r'(?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+'
            r'[a-zA-Z]{2,6}$'
            r'|localhost|'
            r'(\d{1,3}\.){3}\d{1,3}$')
        return domain_regex.match(host)

    def validate_port(self, port):
        """Validate the port number to ensure it's within the valid range."""
        return port.isdigit() and 1 <= int(port) <= 65535

    def run(self):
        """Run the banner grabbing function based on user input."""
        while True:
            host = input(f"{Fore.GREEN}Enter the host to grab the banner from (e.g., example.com): {Fore.RESET}").strip()
            sanitized_host = self.sanitize_host_input(host)

            if not sanitized_host or not self.validate_host(sanitized_host):
                print(f"{Fore.RED}Error: No value or invalid value entered. Please enter a valid domain or IP address.")
                continue

            port = input(f"{Fore.GREEN}Enter the port number (e.g., 80): {Fore.RESET}").strip()
            if not self.validate_port(port):
                print(f"{Fore.RED}Error: Invalid port number. Please enter a number between 1 and 65535.")
                continue

            self.host = sanitized_host
            self.port = int(port)

            self.grab_banner()
            break

if __name__ == "__main__":
    bg = BannerGrabbing()
    bg.run()
