# Build cc_hardware executable
# Usage: .\build.ps1

$ErrorActionPreference = "Stop"

Write-Host "Building cc_hardware..." -ForegroundColor Cyan

# Get script directory
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptDir

# Create/activate virtual environment
if (-not (Test-Path ".venv")) {
    Write-Host "Creating virtual environment..."
    python -m venv .venv
}

# Activate venv
. .venv\Scripts\Activate.ps1

# Install dependencies
Write-Host "Installing dependencies..."
pip install --quiet --upgrade pip
pip install --quiet -r requirements.txt

# Build executable
Write-Host "Building executable..."
pyinstaller --clean --noconfirm cc_hardware.spec

# Verify output
if (Test-Path "dist\cc_hardware.exe") {
    $size = (Get-Item "dist\cc_hardware.exe").Length / 1MB
    Write-Host "[OK] Built dist\cc_hardware.exe ($([math]::Round($size, 1)) MB)" -ForegroundColor Green
    exit 0
} else {
    Write-Host "[FAIL] Build failed - cc_hardware.exe not found" -ForegroundColor Red
    exit 1
}
