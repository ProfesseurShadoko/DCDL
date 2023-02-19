from app import app, set_param
from flask import redirect, render_template
from flask import request

from solver.chiffres import Chiffres
from solver.lettres import Lettres
from game import Game
from game_msg import GameMsg

### GLOBALS ###
GAME = Game()
VOWLS=5

### HOME ###
@app.route("/",methods=['GET','POST']) #handle POST from parametres
def home():
    
    
    #has the game ended ?
    global GAME
    previous_game = GAME #useless if GAME.count!=Game.duration
    show_modal="false"
    if GAME.count==Game.duration:
        #we reached the end of the game, we reset it, but we want to display results with a modal.
        previous_game = GAME
        show_modal = "true"
        GameMsg("game reset")
        GAME = Game()
        
    if request.method=="POST":
        if "c-time" in request.form.keys():
            c_time = int(request.form["c-time"])
            l_time = int(request.form["l-time"])
            d_time = float(request.form["d-time"])
            
            Lettres.time = l_time
            Chiffres.time = c_time
            Lettres.timeout = d_time
            Chiffres.timeout = d_time
            GameMsg(f"update param [lettres={l_time},chiffres={c_time}]")
            
        if "reset" in request.form.keys():
            GAME = Game()
            GameMsg("game reset")
    
    #what to do when starting a game / 
    if GAME.count == 0:
        first_button="NOUVELLE PARTIE"
        progress=""
    else:
        first_button="CONTINUER"
        progress=f" ({GAME.count+1}/{Game.duration})"
        first_button+=progress
            
    return render_template("home.html",first_button=first_button,max_score=previous_game.score,show_modal=show_modal)

### PARAMETRES ###
@app.route("/parametres")
def param():
    param = {
        "c-time":Chiffres.time,
        "l-time":Lettres.time,
        "d-time":Chiffres.timeout,
    }
    return render_template("param.html",param=param)


### LETTER NEXT ###
@app.route("/lchoice_next")
def next_letter_choice():
    return render_template("number_choice.html",href="lettres_next")

@app.route("/lettres_next",methods=['GET','POST']) #handle post from choose vowls
def lettre_next():
    if request.method=="POST":
        VOWLS = int(request.form['number'])
        GameMsg(f"response recieved : {VOWLS}")
    lettres = GAME.next(VOWLS)
    round = Lettres(lettres)
    GAME.add_score(round.score) #cb un coup de lettres rapporte
    return render_round(round)

### CHIFFRE NEXT ###
@app.route("/chiffres_next")
def chiffres_next():
    chiffres = GAME.next()
    round=Chiffres(chiffres,GAME.rd_target())
    GAME.add_score(10) #tous les coups de chiffres rapportent 10 points
    return render_round(round)
    
### NEXT ROUND ###
@app.route("/next")
def next_round():    
    if GAME._next=="c":
        return redirect("/chiffres_next")
    else:
        return redirect("/lchoice_next")


### LETTRES ###
@app.route("/lettres",methods=['GET','POST']) #handle post from choose vowls
def lettres():
    if request.method=="POST":
        VOWLS = int(request.form['number'])
        GameMsg(f"response recieved : {VOWLS}")
    game = Game()
    lettres = game.pop("l",VOWLS)
    round = Lettres(lettres)
    return render_round(round)

@app.route("/lchoice")
def letter_choice():
    return render_template("number_choice.html",href="lettres")

### CHIFFRES ###
@app.route("/chiffres")
def chiffres():
    game = Game()
    chiffres = game.pop("c")
    round=Chiffres(chiffres,game.rd_target())
    return render_round(round)


def render_round(round):
    return render_template("round.html",round=round)

if __name__=="__main__":
    lettres = Lettres("ceocinelelc")
    print(lettres.cards_to_js())
    chiffres = Chiffres([1,2,5,6,25,2],972)
    print(chiffres.cards_to_js())