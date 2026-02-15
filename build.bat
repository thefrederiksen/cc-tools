@echo off
REM Build all cc-tools and copy to C:\cc-tools
REM Usage: build.bat

setlocal enabledelayedexpansion

echo ============================================
echo Building all cc-tools
echo ============================================
echo.

set "REPO_DIR=%~dp0"
set "INSTALL_DIR=C:\cc-tools"
set "FAILED="
set "SUCCESS_COUNT=0"
set "FAIL_COUNT=0"

REM Create install directory if it doesn't exist
if not exist "%INSTALL_DIR%" (
    echo Creating %INSTALL_DIR%...
    mkdir "%INSTALL_DIR%"
)

REM List of tools to build
set "TOOLS=cc_gmail cc_image cc_markdown cc_setup cc_transcribe cc_video cc_voice cc_whisper"

for %%T in (%TOOLS%) do (
    echo.
    echo --------------------------------------------
    echo Building %%T...
    echo --------------------------------------------

    set "TOOL_DIR=%REPO_DIR%src\%%T"

    if exist "!TOOL_DIR!\build.ps1" (
        pushd "!TOOL_DIR!"
        powershell -ExecutionPolicy Bypass -File build.ps1

        if !errorlevel! equ 0 (
            REM Copy exe to install directory
            if exist "dist\%%T.exe" (
                copy /Y "dist\%%T.exe" "%INSTALL_DIR%\" >nul
                echo [OK] %%T.exe copied to %INSTALL_DIR%
                set /a SUCCESS_COUNT+=1
            ) else (
                echo [FAIL] %%T.exe not found after build
                set "FAILED=!FAILED! %%T"
                set /a FAIL_COUNT+=1
            )
        ) else (
            echo [FAIL] Build failed for %%T
            set "FAILED=!FAILED! %%T"
            set /a FAIL_COUNT+=1
        )
        popd
    ) else (
        echo [SKIP] No build.ps1 found for %%T
    )
)

echo.
echo ============================================
echo Build Summary
echo ============================================
echo Successful: %SUCCESS_COUNT%
echo Failed: %FAIL_COUNT%
if defined FAILED (
    echo Failed tools:%FAILED%
    exit /b 1
) else (
    echo All tools built successfully!
    echo Executables installed to: %INSTALL_DIR%
    echo.
    echo Run install.bat to add %INSTALL_DIR% to your PATH
)
