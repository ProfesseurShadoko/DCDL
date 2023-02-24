from flask import Flask
from app.solver.chiffres import Chiffres
from app.solver.lettres import Lettres
from app.game_objects.game import Game
from app.game_objects.game import GameMsg

app = Flask(__name__)
app.secret_key = "kangouroo"


def set_param(display_delay:float=None,lettres_time:int=None,chiffres_time:int=None,game_duration:int=None):
    if display_delay!=None:
        Chiffres.timeout = display_delay
        Lettres.timeout = display_delay
        GameMsg(f"update param [{display_delay=}]")
        
    if lettres_time!=None:
        Lettres.time = lettres_time
        GameMsg(f"update param [{lettres_time=}]")
    
    if chiffres_time!=None:
        Chiffres.time = chiffres_time
        GameMsg(f"update param [{chiffres_time=}]")
        
    if game_duration!=None:
        Game.duration = game_duration
        GameMsg(f"update param [{game_duration=}]")