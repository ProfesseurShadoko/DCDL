
import os

slash="\\"
print(slash)

with open("launcher/launcher.py","r") as file:
    launcher_file = file.read()


if "###DEFAULT###" in launcher_file:
    
    #inserting the path of your directory in the python code !
    launcher_file = launcher_file.replace("###DEFAULT###",os.getcwd()).replace(slash,slash+slash)

    with open("launcher/launcher.py","w") as file:
        file.write(launcher_file)
    os.chdir(os.getcwd()+"/launcher")
    
    #creating .exe file
    os.system("pip install pyinstaller")
    os.system("pyinstaller --onefile -w launcher.py")
    
        