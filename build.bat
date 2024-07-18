@echo off

pip install -r requirements.txt
pyinstaller -F -w src/main.py --name "OSU-Cleaner"

del /f /s /q Build
rmdir /s /q Build

move dist\OSU-Cleaner.exe ..\osu-cleaner-main
rmdir /s /q dist

del OSU-Cleaner.spec
pause
