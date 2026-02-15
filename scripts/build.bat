@echo off
REM Build script wrapper for cc_markdown.exe
REM Usage: scripts\build.bat

echo CC Markdown Build Script
echo ========================
echo.

REM Change to cc_markdown source directory
cd /d "%~dp0..\src\cc_markdown"

REM Check if PowerShell is available
where powershell >nul 2>&1
if errorlevel 1 (
    echo ERROR: PowerShell not found
    exit /b 1
)

REM Run the PowerShell build script
powershell -ExecutionPolicy Bypass -File "build.ps1"

echo.
echo Build output is in: src\cc_markdown\dist\cc_markdown.exe
