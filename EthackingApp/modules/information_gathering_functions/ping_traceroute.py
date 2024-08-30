import os
import platform
import subprocess
from urllib.parse import urlparse
from colorama import init, Fore, Style
import threading
import time
import re

init(autoreset=True)

class PingTraceroute:
    def __init__(self):
        """Initialize the PingTraceroute class."""
        self.stop_animation = False

    def ping(self, host):
        """Ping a host and display the result."""
        param = '-n' if platform.system().lower() == 'windows' else '-c'
        command = ['ping', param, '4', host]
        try:
            print(f"{Fore.CYAN}Pinging {host}...")
            output = subprocess.check_output(command, universal_newlines=True)
            print(f"{Fore.GREEN}{output}")
        except subprocess.CalledProcessError as e:
            print(f"{Fore.RED}Failed to ping {host}: {e}")

    def traceroute(self, host, max_hops, timeout):
        """Perform a traceroute to a host and display the result."""
        if platform.system().lower() == 'windows':
            command = ['tracert', '-h', str(max_hops), host]
        else:
            command = ['traceroute', '-m', str(max_hops), '-w', str(timeout), host]

        print(f"{Fore.CYAN}Performing traceroute to {host} with max hops={max_hops} and timeout={timeout} seconds per hop...")

        self.stop_animation = False
        animation_thread = threading.Thread(target=self.show_animation)
        animation_thread.start()

        start_time = time.time()

        try:
            output = subprocess.check_output(command, universal_newlines=True, stderr=subprocess.STDOUT)
            elapsed_time = time.time() - start_time

            self.stop_animation = True
            animation_thread.join()

            print(f"{Fore.GREEN}{output}")
            print(f"{Fore.CYAN}Traceroute completed in {elapsed_time:.2f} seconds.")
        except subprocess.CalledProcessError as e:
            self.stop_animation = True
            animation_thread.join()
            print(f"{Fore.RED}Failed to perform traceroute to {host}: {e}")
        except Exception as e:
            self.stop_animation = True
            animation_thread.join()
            print(f"{Fore.RED}Error during traceroute: {e}")

    def show_animation(self):
        """Show a simple animation while traceroute is running."""
        animation_chars = "|/-\\"
        idx = 0
        start_time = time.time()
        while not self.stop_animation:
            elapsed_time = int(time.time() - start_time)
            minutes, seconds = divmod(elapsed_time, 60)
            print(f"{Fore.YELLOW}\r{animation_chars[idx % len(animation_chars)]} Waiting for traceroute... {minutes}m {seconds}s elapsed", end="")
            idx += 1
            time.sleep(0.1)
        print("\r", end="")

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

    def run(self):
        """Run the ping and traceroute functions based on user input."""
        while True:
            host = input(f"{Fore.GREEN}Enter the host to ping and traceroute (e.g., example.com): {Fore.RESET}").strip()
            sanitized_host = self.sanitize_host_input(host)

            if not sanitized_host or not self.validate_host(sanitized_host):
                print(f"{Fore.RED}Error: No value or invalid value entered. Please enter a valid domain or IP address.")
                input(f"{Fore.YELLOW}Press Enter to try again...{Style.RESET_ALL}")
                continue

            max_hops = self.get_valid_number_input(f"{Fore.GREEN}Enter max hops for traceroute (default 30): {Fore.RESET}", 30)
            timeout = self.get_valid_number_input(f"{Fore.GREEN}Enter timeout per hop in seconds for traceroute (default 5): {Fore.RESET}", 5)

            self.ping(sanitized_host)
            self.traceroute(sanitized_host, max_hops, timeout)
            break

    def get_valid_number_input(self, prompt, default):
        """Prompt user for a number and validate input."""
        while True:
            user_input = input(prompt).strip()
            if user_input == "":
                return default
            if user_input.isdigit():
                return int(user_input)
            else:
                print(f"{Fore.RED}Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    pt = PingTraceroute()
    pt.run()
