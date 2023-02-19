from flask import Flask
from solver.chiffres import Chiffres
from solver.lettres import Lettres

app = Flask(__name__)
app.secret_key = "kangouroo"


def set_param(display_delay:float=None,lettres_time:int=None,chiffres_time:int=None):
    if display_delay!=None:
        Chiffres.timeout = display_delay
        Lettres.timeout = display_delay
        
    if lettres_time!=None:
        Lettres.time = lettres_time
    
    if chiffres_time!=None:
        Chiffres.time = chiffres_time

    
set_param(
    display_delay = 1,
    lettres_time = 45,
    chiffres_time = 90
)