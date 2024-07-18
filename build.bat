@echo off

pip install -r requirements.txt
pyinstaller -w --icon=resources/icon.ico --onefile --name "OSU-Cleaner" src/main.py

del /f /s /q Build
rmdir /s /q Build

move dist\OSU-Cleaner.exe ..\osu-cleaner-main
rmdir /s /q dist
ren OSU-Cleaner.exe osu!cleaner.exe

del OSU-Cleaner.spec
pause
