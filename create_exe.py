
import os
from app.game_objects.game_msg import GameMsg

LOC = os.getcwd()+"\\launcher\\dist\\launcher.exe"

if os.path.exists("launcher"):
    GameMsg("File already exists")
    print(f"--> .exe file at: {LOC}")
    exit()

os.mkdir("launcher")

slash="\\"

GameMsg("read launcher.py")
with open("app/launcher/launcher.py","r") as file:
    launcher_file = file.read()

GameMsg("insert path")
launcher_file = launcher_file.replace("###DEFAULT###",os.getcwd()).replace(slash,slash+slash)

with open("launcher/launcher.py","w") as file:
    file.write(launcher_file)
os.chdir(os.getcwd()+"/launcher")

#creating .exe file
GameMsg("create .exe file")
os.system("pip install pyinstaller")
os.system("pyinstaller --onefile -w launcher.py")
GameMsg("File successfully created")

print(f"--> .exe file at: {LOC}")

    
        