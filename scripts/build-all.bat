@echo off
REM Build all cc-tools executables
REM Usage: build-all.bat

echo ============================================================
echo Building all cc-tools...
echo ============================================================
echo.

echo [1/3] Building cc_markdown...
cd /d "%~dp0..\src\cc_markdown"
powershell -ExecutionPolicy Bypass -File "build.ps1"
if %ERRORLEVEL% NEQ 0 (
    echo cc_markdown build failed!
    exit /b 1
)
echo.

REM cc_transcribe build script doesn't exist yet - skip for now
REM echo [2/3] Building cc_transcribe...
REM cd /d "%~dp0..\src\cc_transcribe"
REM powershell -ExecutionPolicy Bypass -File "build.ps1"
REM if %ERRORLEVEL% NEQ 0 (
REM     echo cc_transcribe build failed!
REM     exit /b 1
REM )
REM echo.

echo [2/3] Building cc-tools-setup...
cd /d "%~dp0..\src\cc_setup"
powershell -ExecutionPolicy Bypass -File "build.ps1"
if %ERRORLEVEL% NEQ 0 (
    echo cc-tools-setup build failed!
    exit /b 1
)
echo.

echo ============================================================
echo All builds completed successfully!
echo ============================================================
echo.
echo Executables:
echo   src\cc_markdown\dist\cc_markdown.exe
echo   src\cc_setup\dist\cc-tools-setup.exe
