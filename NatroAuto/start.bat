@echo off
echo NatroAuto
echo Discord bot by SRP
echo Natro Macro made by the Natro Team
echo The bot will be minimized on taskbar.
echo installing requirements...
pip install nextcord pyautogui setuptools pywin32 configparser pillow pystray
start pythonw.exe bot.py
