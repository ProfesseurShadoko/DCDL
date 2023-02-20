
#let's open localhost after waiting 2s
#in order to give enough time for creating the dictionnary

from time import sleep
import webbrowser
from threading import Thread
from game_objects.game_msg import GameMsg


#open the webbrowser after 2s
GameMsg("start in 2 seconds")

def start():
    sleep(2)
    webbrowser.open("http://127.0.0.1:5000/")

thread = Thread(target=start)
thread.start()


#let's run the app
GameMsg("initializing")
from views import *
from app import app

GameMsg("LAUNCHING APP")
app.run(debug=False)

