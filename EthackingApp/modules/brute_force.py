class BruteForce:
    def __init__(self):
        pass

    def run(self):
        print("Running Brute Force Attack...")
        target_password = "password123"
        attempts = ["123456", "password", "123456789", "password123"]
        for attempt in attempts:
            print(f"Trying: {attempt}")
            if attempt == target_password:
                print(f"Password found: {attempt}")
                break
        else:
            print("Password not found.")

if __name__ == "__main__":
    brute = BruteForce()
    brute.run()
