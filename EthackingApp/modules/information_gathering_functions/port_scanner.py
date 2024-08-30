import socket
from urllib.parse import urlparse
from colorama import init, Fore, Style
import re
import threading
import time

init(autoreset=True)

class PortScanner:
    def __init__(self, host):
        """Initialize the PortScanner class with a target host."""
        self.host = self.sanitize_host_input(host)
        self.stop_animation = False
        self.scanned_ports = []

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

    def show_animation(self):
        """Show a simple animation while port scanning is running."""
        animation_chars = "|/-\\"
        idx = 0
        while not self.stop_animation:
            print(f"{Fore.YELLOW}{animation_chars[idx % len(animation_chars)]} Scanning ports...", end="\r")
            idx += 1
            time.sleep(0.1)
        print("\r", end="")

    def scan_ports(self, start_port, end_port):
        """Scan a range of ports on the specified host."""
        open_ports = []

        if not self.validate_host(self.host):
            print(f"{Fore.RED}Error: Invalid host. Please enter a valid domain or IP address.")
            return

        print(f"{Fore.CYAN}Scanning ports {start_port} to {end_port} on {self.host}...\n")

        self.stop_animation = False
        animation_thread = threading.Thread(target=self.show_animation)
        animation_thread.start()

        for port in range(start_port, end_port + 1):
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(1)
                result = s.connect_ex((self.host, port))
                self.scanned_ports.append(port)

                if result == 0:
                    open_ports.append(port)
                    print(f"{Fore.GREEN}Port {port} is open...")
                else:
                    print(f"{Fore.RED}Port {port} is closed...")

                s.close()
            except socket.gaierror as e:
                print(f"{Fore.RED}Socket error: {e}")
                break
            except Exception as e:
                print(f"{Fore.RED}Error: {e}")
                continue

        self.stop_animation = True
        animation_thread.join()

        if not open_ports:
            print(f"{Fore.YELLOW}No open ports found in the range {start_port} to {end_port}.")
        else:
            print(f"{Fore.GREEN}Open ports on {self.host}: {open_ports}")

    def run(self):
        """Run the port scanner based on user input."""
        while True:
            try:
                start_port = int(input(f"{Fore.GREEN}Enter the start port number (e.g., 1): {Style.RESET_ALL}"))
                end_port = int(input(f"{Fore.GREEN}Enter the end port number (e.g., 1024): {Style.RESET_ALL}"))

                if start_port < 1 or end_port > 65535 or start_port > end_port:
                    print(f"{Fore.RED}Error: Invalid port range. Please enter a valid range between 1 and 65535.")
                    continue

                self.scan_ports(start_port, end_port)
                break
            except ValueError:
                print(f"{Fore.RED}Error: Please enter valid numerical values for the port range.")

if __name__ == "__main__":
    host = input("Enter the host to scan (e.g., example.com): ").strip()
    scanner = PortScanner(host)
    scanner.run()
