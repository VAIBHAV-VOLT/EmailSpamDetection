# Email Phishing Analyzer - PowerShell Startup Script
# This script sets up and runs both backend and frontend servers

param(
    [switch]$NoVenv = $false
)

Write-Host "`n============================================" -ForegroundColor Cyan
Write-Host "Email Phishing Analyzer - Startup Script" -ForegroundColor Cyan
Write-Host "============================================`n" -ForegroundColor Cyan

$projectRoot = Get-Location

# Check Python
try {
    $pythonVersion = python --version 2>&1
    Write-Host "[OK] Python found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "[ERROR] Python not found. Download from: https://www.python.org/downloads/" -ForegroundColor Red
    exit 1
}

# Check Node.js
try {
    $nodeVersion = node --version
    Write-Host "[OK] Node.js found: $nodeVersion" -ForegroundColor Green
} catch {
    Write-Host "[ERROR] Node.js not found. Download from: https://nodejs.org/" -ForegroundColor Red
    exit 1
}

Write-Host ""

# Create virtual environment if needed
if ((Test-Path "venv") -eq $false) {
    Write-Host "Creating Python virtual environment..." -ForegroundColor Yellow
    python -m venv venv
    Write-Host "[OK] Virtual environment created" -ForegroundColor Green
    Write-Host ""
}

# Activate venv and install requirements
Write-Host "Setting up Python dependencies..." -ForegroundColor Yellow
& ".\venv\Scripts\Activate.ps1"
python -m pip install -q --upgrade pip
pip install -q -r requirements.txt
Write-Host "[OK] Python dependencies installed" -ForegroundColor Green
Write-Host ""

Write-Host "============================================" -ForegroundColor Cyan
Write-Host "Starting Backend Server..." -ForegroundColor Cyan
Write-Host "============================================`n" -ForegroundColor Cyan

# Start backend in new PowerShell window
$backendScript = @"
Set-Location "$projectRoot\backend"
& "$projectRoot\venv\Scripts\Activate.ps1"
Write-Host "Backend starting... (Ctrl+C to stop)" -ForegroundColor Green
python main.py
Read-Host "Press Enter to close"
"@

$backendEncodedCommand = [Convert]::ToBase64String([Text.Encoding]::Unicode.GetBytes($backendScript))
Start-Process powershell -ArgumentList "-NoExit -EncodedCommand $backendEncodedCommand" -WindowStyle Normal

Write-Host "Backend window opened. Waiting for startup..." -ForegroundColor Yellow
Start-Sleep -Seconds 3

Write-Host ""
Write-Host "============================================" -ForegroundColor Cyan
Write-Host "Starting Frontend Server..." -ForegroundColor Cyan
Write-Host "============================================`n" -ForegroundColor Cyan

# Setup frontend
$frontendPath = "$projectRoot\frontend\emailanalyzer"
Set-Location $frontendPath

if ((Test-Path "node_modules") -eq $false) {
    Write-Host "Installing Node dependencies (first time only)..." -ForegroundColor Yellow
    npm install
    Write-Host "[OK] Node dependencies installed" -ForegroundColor Green
}

# Start frontend in new PowerShell window
$frontendScript = @"
Set-Location "$frontendPath"
Write-Host "Frontend starting... (Ctrl+C to stop)" -ForegroundColor Green
npm run dev
Read-Host "Press Enter to close"
"@

$frontendEncodedCommand = [Convert]::ToBase64String([Text.Encoding]::Unicode.GetBytes($frontendScript))
Start-Process powershell -ArgumentList "-NoExit -EncodedCommand $frontendEncodedCommand" -WindowStyle Normal

Write-Host ""
Write-Host "============================================" -ForegroundColor Green
Write-Host "✓ Both servers are starting!" -ForegroundColor Green
Write-Host "============================================" -ForegroundColor Green
Write-Host ""
Write-Host "Backend:  http://localhost:5000" -ForegroundColor Cyan
Write-Host "Frontend: http://localhost:5173" -ForegroundColor Cyan
Write-Host ""
Write-Host "Application will open in your browser automatically." -ForegroundColor Yellow
Write-Host ""
Write-Host "To stop the servers:" -ForegroundColor Gray
Write-Host "  • Close the command windows, or" -ForegroundColor Gray
Write-Host "  • Press Ctrl+C in each window" -ForegroundColor Gray
Write-Host ""

Set-Location $projectRoot

# Open frontend in browser
Start-Sleep -Seconds 4
Start-Process "http://localhost:5173"
