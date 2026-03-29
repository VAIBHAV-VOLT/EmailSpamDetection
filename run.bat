@echo off
REM Email Phishing Analyzer - Windows Startup Script
REM This script sets up and runs both backend and frontend servers

setlocal enabledelayedexpansion

echo.
echo ============================================
echo Email Phishing Analyzer - Startup Script
echo ============================================
echo.

set PROJECT_ROOT=%~dp0
cd /d "%PROJECT_ROOT%"

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Download from: https://www.python.org/downloads/
    pause
    exit /b 1
)

REM Check if Node.js is installed
node --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Node.js is not installed or not in PATH
    echo Download from: https://nodejs.org/
    pause
    exit /b 1
)

echo [OK] Python and Node.js found
echo.

REM Create virtual environment if it doesn't exist
if not exist "venv" (
    echo Creating Python virtual environment...
    python -m venv venv
    echo [OK] Virtual environment created
)

echo.
echo ============================================
echo Starting Backend Server...
echo ============================================
echo.
echo Opening backend in new terminal window...
echo.

REM Open backend in new terminal
start "Email Phishing Analyzer - Backend" cmd.exe /k ^
    "cd /d "%PROJECT_ROOT%backend" & ^
    "%PROJECT_ROOT%venv\Scripts\activate.bat" & ^
    python main.py"

timeout /t 3 /nobreak

echo.
echo ============================================
echo Starting Frontend Server...
echo ============================================
echo.
echo Opening frontend in new terminal window...
echo.

REM Open frontend in new terminal
start "Email Phishing Analyzer - Frontend" cmd.exe /k ^
    "cd /d "%PROJECT_ROOT%frontend\emailanalyzer" & ^
    npm install --legacy-peer-deps & ^
    npm run dev"

echo.
echo ============================================
echo ✓ Both servers are starting!
echo ============================================
echo.
echo Backend:  http://localhost:5000
echo Frontend: http://localhost:5173
echo.
echo Application will open in your browser automatically.
echo.
echo To stop the servers:
echo   - Close the command windows, or
echo   - Press Ctrl+C in each window
echo.
pause
