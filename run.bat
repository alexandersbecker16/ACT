@echo off
title ACT Test Generator
cd /d "%~dp0"
echo Starting ACT Test Generator...
echo.
echo A browser window will open. Keep this window open while you use the app.
echo Press Ctrl+C here to stop the server when you are done.
echo.
py -3 server.py
if errorlevel 1 python server.py
pause
