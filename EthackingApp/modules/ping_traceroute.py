import os
import platform
import subprocess
from urllib.parse import urlparse
from colorama import init, Fore

init(autoreset=True)

def ping(host):
    """Ping a host and display the result."""
    param = '-n' if platform.system().lower() == 'windows' else '-c'

    command = ['ping', param, '4', host]
    try:
        print(f"{Fore.CYAN}Pinging {host}...")
        output = subprocess.check_output(command, universal_newlines=True)
        print(f"{Fore.GREEN}{output}")
    except subprocess.CalledProcessError as e:
        print(f"{Fore.RED}Failed to ping {host}: {e}")

def traceroute(host, max_hops, timeout):
    """Perform a traceroute to a host and display the result."""
    if platform.system().lower() == 'windows':
        command = ['tracert', '-h', str(max_hops), host]
    else:
        command = ['traceroute', '-m', str(max_hops), '-w', str(timeout), host]

    try:
        print(f"{Fore.CYAN}Performing traceroute to {host} with max hops={max_hops} and timeout={timeout} seconds per hop...")
        output = subprocess.check_output(command, universal_newlines=True, stderr=subprocess.STDOUT)
        print(f"{Fore.GREEN}{output}")
    except subprocess.CalledProcessError as e:
        print(f"{Fore.RED}Failed to perform traceroute to {host}: {e}")
    except Exception as e:
        print(f"{Fore.RED}Error during traceroute: {e}")

def sanitize_host_input(host):
    """Sanitize host input to extract the domain from a URL if needed."""
    parsed_url = urlparse(host)
    return parsed_url.netloc if parsed_url.netloc else parsed_url.path

def run_ping_traceroute():
    """Run the ping and traceroute functions based on user input."""
    host = input(f"{Fore.GREEN}Enter the host to ping and traceroute (e.g., example.com): {Fore.RESET}")
    sanitized_host = sanitize_host_input(host)

    try:
        max_hops = int(input(f"{Fore.GREEN}Enter max hops for traceroute (default 30): {Fore.RESET}") or 30)
    except ValueError:
        max_hops = 30

    try:
        timeout = int(input(f"{Fore.GREEN}Enter timeout per hop in seconds for traceroute (default 5): {Fore.RESET}") or 5)
    except ValueError:
        timeout = 5

    if sanitized_host:
        ping(sanitized_host)
        traceroute(sanitized_host, max_hops, timeout)
    else:
        print(f"{Fore.RED}Invalid host input. Please enter a valid domain or IP address.")

