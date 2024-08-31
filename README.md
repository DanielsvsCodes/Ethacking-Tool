# Ethacking-Tool
A Python application for educational penetration testing and cybersecurity learning

## Build with cosign validation

1. Build Application:
´´´
pyinstaller --clean EthicalHackingTool.spec
´´´

2. Sign the application:
´´´
.\cosign.exe sign-blob --key cosign.key dist/EthicalHackingTool/EthicalHackingTool.exe --output-signature dist/EthicalHackingTool/EthicalHackingTool.exe.sig
´´´

3. Verify the application:
´´´
.\cosign.exe verify-blob --key cosign.pub dist/EthicalHackingTool/EthicalHackingTool.exe --signature dist/EthicalHackingTool/EthicalHackingTool.exe.sig
´´´