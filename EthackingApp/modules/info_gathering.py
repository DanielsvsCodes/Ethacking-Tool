class InfoGathering:
    def __init__(self):
        pass

    def run(self):
        print("Running Website Information Gathering...")
        website_info = {
            'Domain': 'example.com',
            'IP Address': '93.184.216.34',
            'Server': 'Apache',
            'Location': 'US'
        }
        for key, value in website_info.items():
            print(f"{key}: {value}")

if __name__ == "__main__":
    info = InfoGathering()
    info.run()
