import requests
from bs4 import BeautifulSoup
from stem import Signal
from stem.control import Controller
import time

class DarkWebScraper:
    def __init__(self, url, headers=None):
        """
        Initialize the DarkWebScraper class with necessary parameters.
        :param url: The .onion URL to scrape.
        :param headers: (Optional) HTTP headers to use for the requests.
        """
        self.url = url
        self.session = requests.Session()
        self.session.proxies = {
            'http': 'socks5h://127.0.0.1:9050',
            'https': 'socks5h://127.0.0.1:9050'
        }
        self.headers = headers or {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
    def renew_tor_connection(self):
        """
        Signal Tor to renew the connection, which changes the Tor circuit.
        """
        with Controller.from_port(port=9051) as controller:
            controller.authenticate(password="your_password_here")
            controller.signal(Signal.NEWNYM)
            print("[*] Tor circuit renewed.")
    
    def scrape(self):
        """
        Scrape the specified URL and return the parsed HTML.
        """
        try:
            print(f"[*] Scraping URL: {self.url}")
            response = self.session.get(self.url, headers=self.headers)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            return soup
        except requests.RequestException as e:
            print(f"[-] Request failed: {e}")
            return None

    def run(self):
        """
        Run the scraping process.
        """
        try:
            soup = self.scrape()
            if soup:
                for link in soup.find_all('a'):
                    print(link.get('href'))
            else:
                print("[-] Failed to scrape the page.")
        except KeyboardInterrupt:
            print("\n[*] Scraping interrupted. Exiting...")
    
if __name__ == "__main__":
    url = input("Enter the .onion URL to scrape: ").strip()
    scraper = DarkWebScraper(url)

    scraper.renew_tor_connection()
    scraper.run()
