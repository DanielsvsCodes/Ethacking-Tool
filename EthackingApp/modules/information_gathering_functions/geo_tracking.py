import requests
from colorama import init, Fore

init(autoreset=True)

class GeoTracking:
    def __init__(self, ip_address):
        """Initialize the GeoTracking class with an IP address."""
        self.ip_address = ip_address
        self.api_url = f"http://ip-api.com/json/{self.ip_address}"

    def fetch_geolocation(self):
        """Fetch geolocation data for the provided IP address."""
        try:
            print(f"{Fore.CYAN}Fetching geolocation data for {self.ip_address}...{Fore.RESET}")
            response = requests.get(self.api_url)
            data = response.json()

            if data['status'] == 'success':
                self.display_geolocation(data)
            else:
                print(f"{Fore.RED}Failed to fetch geolocation data: {data['message']}{Fore.RESET}")

        except requests.exceptions.RequestException as e:
            print(f"{Fore.RED}An error occurred while fetching geolocation data: {e}{Fore.RESET}")

    def display_geolocation(self, data):
        """Display geolocation data."""
        print(f"{Fore.GREEN}Geolocation data for {self.ip_address}:{Fore.RESET}")
        print(f"  {Fore.YELLOW}Country: {Fore.RESET}{data['country']}")
        print(f"  {Fore.YELLOW}Region: {Fore.RESET}{data['regionName']}")
        print(f"  {Fore.YELLOW}City: {Fore.RESET}{data['city']}")
        print(f"  {Fore.YELLOW}Latitude: {Fore.RESET}{data['lat']}")
        print(f"  {Fore.YELLOW}Longitude: {Fore.RESET}{data['lon']}")
        print(f"  {Fore.YELLOW}ISP: {Fore.RESET}{data['isp']}")
        print(f"  {Fore.YELLOW}Organization: {Fore.RESET}{data['org']}")
        print(f"  {Fore.YELLOW}AS: {Fore.RESET}{data['as']}")
        print(f"  {Fore.YELLOW}Timezone: {Fore.RESET}{data['timezone']}")

    def run(self):
        """Run the geo-tracking process."""
        self.fetch_geolocation()
