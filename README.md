# Ethacking-Tool

## Overview

**Ethacking-Tool** is a Python-based application designed for educational penetration testing and cybersecurity learning. The tool provides various categories of cybersecurity tools to help users learn about different types of cyber attacks and information gathering techniques in a controlled environment. The application is currently under development, and some modules are available for use.

## Technologies Used

- **Python**: Core programming language for all scripts and functionalities.
- **PyInstaller**: Used for building the application into a standalone executable.
- **Cosign**: Utility for signing and verifying the application binaries for security.
- **Virtualenv**: Python virtual environment for managing dependencies.

## How It Works

The application is structured into different categories, each containing several Python scripts that perform specific cybersecurity tasks. The main entry point is +main.py+, which provides a user interface to select different categories and tools.

- **Information Gathering**: Tools for collecting data about a target network or system, including DNS spoofing, subdomain enumeration, and port scanning.
- **Exploitation Tools**: Tools to test and exploit vulnerabilities in systems, such as brute force attacks, DDoS attacks, and password cracking.
- **Miscellaneous Tools**: Additional tools for cybersecurity, including data stealers and web scrapers.

## Project Structure

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

## Prerequisites

- **Python 3.x**: Ensure Python is installed and available in your system PATH.
- **Virtualenv**: Used for managing dependencies in a virtual environment.
- **PyInstaller**: For building the application into a standalone executable.
- **Cosign**: For signing and verifying the application binaries.

## Getting Started

### Step 1: Set Up the Environment

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/Ethacking-Tool.git
    cd Ethacking-Tool
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate    # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Step 2: Build the Application

To build the application into a standalone executable using PyInstaller:

```bash
pyinstaller --clean EthicalHackingTool.spec
```

### Step 3: Sign the Application

Sign the built application using Cosign:

```bash
.\cosign.exe sign-blob --key cosign.key dist/EthicalHackingTool/EthicalHackingTool.exe --output-signature dist/EthicalHackingTool/EthicalHackingTool.exe.sig
```

### Step 4: Verify the Application

Verify the application signature using Cosign:

```bash
.\cosign.exe verify-blob --key cosign.pub dist/EthicalHackingTool/EthicalHackingTool.exe --signature dist/EthicalHackingTool/EthicalHackingTool.exe.sig
```

## Troubleshooting

### Virtual Environment

- Ensure the virtual environment is activated before installing dependencies or running the application.
- If you encounter permission errors, try running the terminal or command prompt as an administrator.

### PyInstaller

- If the build fails, ensure all dependencies are installed and PyInstaller is correctly configured.
- Check the PyInstaller documentation for troubleshooting specific errors: [PyInstaller Troubleshooting Guide](https://pyinstaller.org/).

### Cosign

- If the signing process fails, check if Cosign is installed and properly configured.
- Ensure the correct keys are being used for signing and verification.

## Disclaimer

This application is intended for educational purposes only. Unauthorized use of this application for malicious activities is strictly prohibited. Currently, only the Information Gathering, Exploitation Tools, and Miscellaneous categories are available.
