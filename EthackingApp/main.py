from modules.info_gathering import InfoGathering
from modules.dos import DOSAttack
from modules.brute_force import BruteForce
from modules.sql_injection import SQLInjection

def main():
    print("Welcome to the Ethical Hacking Tool")
    print("1. Website Information Gathering")
    print("2. DOS/DDoS Attacks")
    print("3. Brute Force Attack")
    print("4. SQL Injection Testing")
    
    choice = input("Select an option: ")
    
    if choice == "1":
        info = InfoGathering()
        info.run()
    elif choice == "2":
        dos = DOSAttack()
        dos.run()
    elif choice == "3":
        brute = BruteForce()
        brute.run()
    elif choice == "4":
        sql = SQLInjection()
        sql.run()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
