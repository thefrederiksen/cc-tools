@echo off
REM Build cc-tools-setup executable
REM Usage: build-setup.bat

echo Building cc-tools-setup...
cd /d "%~dp0..\src\cc_setup"
powershell -ExecutionPolicy Bypass -File "build.ps1"
if %ERRORLEVEL% NEQ 0 (
    echo Build failed!
    exit /b 1
)
echo Done!
