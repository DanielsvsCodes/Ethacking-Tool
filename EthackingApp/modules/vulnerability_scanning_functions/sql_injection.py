class SQLInjection:
    def __init__(self):
        pass

    def run(self):
        print("Testing for SQL Injection...")
        payloads = ["' OR '1'='1", "' OR 'x'='x", "'; DROP TABLE users; --"]
        vulnerable = False
        for payload in payloads:
            print(f"Trying payload: {payload}")
            if payload == "' OR '1'='1":
                print("Vulnerable to SQL Injection!")
                vulnerable = True
                break
        if not vulnerable:
            print("No vulnerabilities found.")

if __name__ == "__main__":
    sql = SQLInjection()
    sql.run()
