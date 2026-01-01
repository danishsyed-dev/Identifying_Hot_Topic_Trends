@echo off
echo Setting up project shortcut...

REM Create a junction point to avoid special characters in path
if not exist "C:\HotTopicProject" (
    mklink /J "C:\HotTopicProject" "%~dp0"
    echo Created shortcut at C:\HotTopicProject
) else (
    echo Shortcut already exists at C:\HotTopicProject
)

cd /d "C:\HotTopicProject"
echo.
echo Current directory: %CD%
echo.
echo Starting Django server...
echo Open http://127.0.0.1:8000/ in your browser
echo.

python manage.py runserver 127.0.0.1:8000
pause
