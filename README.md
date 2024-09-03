# Ethacking-Tool

**Ethacking-Tool** is a Python-based application designed for educational penetration testing and cybersecurity learning. The tool provides various categories of cybersecurity tools to help users learn about different types of cyber attacks and information gathering techniques in a controlled environment. The application is currently under development, and some modules are available for use.

## Features

- **Information Gathering**: Tools for collecting data about a target network or system, including DNS spoofing, subdomain enumeration, and port scanning.
- **Exploitation Tools**: Tools to test and exploit vulnerabilities in systems, such as brute force attacks, DDoS attacks, and password cracking.
- **Miscellaneous Tools**: Additional tools for cybersecurity, including data stealers and web scrapers.

## How It Works

The application is structured into different categories, each containing several Python scripts that perform specific cybersecurity tasks. The main entry point is `main.py`, which provides a user interface to select different categories and tools.

## File Structure

```plaintext
Ethacking-Tool/
├── EthackingApp/
│   ├── categories/
│   │   ├── exploitation_tools.py
│   │   ├── information_gathering.py
│   │   ├── miscellaneous.py
│   │   ├── network_tools.py
│   │   ├── social_engineering.py
│   │   └── vulnerability_scanning.py
│   ├── modules/
│   │   ├── exploitation_tools_functions/
│   │   │   ├── brute_force.py
│   │   │   ├── crack_wifi_password.py
│   │   │   ├── ddos.py
│   │   │   ├── mitm_attack.py
│   │   │   ├── packet_injection.py
│   │   │   ├── password_cracking.py
│   │   │   └── reverse_shell.py
│   │   ├── information_gathering_functions/
│   │   │   ├── banner_grabbing.py
│   │   │   ├── dns_spoofing.py
│   │   │   ├── geo_tracking.py
│   │   │   ├── info_gathering.py
│   │   │   ├── ping_traceroute.py
│   │   │   ├── port_scanner.py
│   │   │   └── subdomain_enum.py
│   │   ├── miscellaneous_functions/
│   │   │   ├── dark_web_scraper.py
│   │   │   └── data_stealer.py
│   │   ├── network_tools_functions/
│   │   │   ├── network_sniffing.py
│   │   │   ├── port_scanner.py
│   │   │   └── wireless_tools.py
│   │   ├── social_engineering_functions/
│   │   │   ├── clipboard_hijacking.py
│   │   │   └── phishing_sim.py
│   │   └── vulnerability_scanning_functions/
│   │       ├── encryption_checker.py
│   │       ├── file_inclusion.py
│   │       ├── sql_injection.py
│   │       ├── web_vuln_scanner.py
│   │       └── xss_tester.py
│   ├── resources/
│   ├── main.py
│   └── utils.py
├── resources/
├── scripts/
├── venv/
├── EthicalHackingTool.spec
├── LICENSE
├── README.md
└── requirements.txt
```

## Build with Cosign Validation

To build, sign, and verify the application with Cosign:

1. **Build the Application:**

    ```
    pyinstaller --clean EthicalHackingTool.spec
    ```

2. **Sign the Application:**

    ```
    .\cosign.exe sign-blob --key cosign.key dist/EthicalHackingTool/EthicalHackingTool.exe --output-signature dist/EthicalHackingTool/EthicalHackingTool.exe.sig
    ```

3. **Verify the Application:**

    ```
    .\cosign.exe verify-blob --key cosign.pub dist/EthicalHackingTool/EthicalHackingTool.exe --signature dist/EthicalHackingTool/EthicalHackingTool.exe.sig
    ```

## Disclaimer

This application is intended for educational purposes only. Unauthorized use of this application for malicious activities is strictly prohibited. Currently, only the Information Gathering, Exploitation Tools, and Miscellaneous categories are available.
