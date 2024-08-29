class DOSAttack:
    def __init__(self):
        pass

    def run(self):
        print("Simulating DOS Attack...")
        # Simulate a DOS attack
        for i in range(5):  # This loop simulates sending 5 attack requests
            print(f"Sending attack packet {i+1}...")

if __name__ == "__main__":
    dos = DOSAttack()
    dos.run()
