@echo off
echo ============================================================
echo   Identifying Hot Topic Trends - Starting Server
echo ============================================================
echo.

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python 3.10 or higher from https://www.python.org/
    pause
    exit /b 1
)

echo [1/3] Checking Python installation...
python --version
echo.

echo [2/3] Checking if dependencies are installed...
python -c "import django" >nul 2>&1
if errorlevel 1 (
    echo Error: Django is not installed!
    echo Installing dependencies...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo Failed to install dependencies.
        pause
        exit /b 1
    )
)
echo Dependencies OK!
echo.

echo [3/3] Starting Django server...
echo.
echo Open your browser and navigate to:
echo     http://127.0.0.1:8000/
echo.
echo Admin credentials:
echo     Username: Admin
echo     Password: Admin
echo.
echo Press Ctrl+C to stop the server
echo.

python manage.py runserver 127.0.0.1:8000
pause
