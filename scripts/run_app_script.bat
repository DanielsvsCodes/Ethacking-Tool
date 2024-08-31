@echo off
REM
net session >nul 2>&1
if %errorLevel% == 0 (
    echo Running as admin...
    cd /d "%~dp0"  REM
    call venv\Scripts\activate  REM
    python EthackingApp\main.py  REM
) else (
    echo Not running as admin, restarting with admin privileges...
    powershell -Command "Start-Process '%~dp0venv\Scripts\python.exe' -ArgumentList '%~dp0EthackingApp\main.py' -WorkingDirectory '%~dp0' -Verb runAs"
)
pause
