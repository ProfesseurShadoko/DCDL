import shutil
from app.game_objects.game_msg import GameMsg

GameMsg("REMOVING FOLDER")

try:
    shutil.rmtree("launcher")
    GameMsg("Folder successfully removed")
except FileNotFoundError:
    GameMsg("Inexistant folder")
