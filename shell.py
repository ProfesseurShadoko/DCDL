from app.solver._solver import solve
from app.solver._dcdl_dict import Dico
import os

shell_help = """
\033[96m

Bienvenue dans la console DCDL ! Voici quelques commandes pour l'utiliser :

>>> -q ou quit() : Quitter la console
>>> -v <mot> : vérifier si le mot est dans le dictionnaire DCDL
>>> -l <10 lettres> : résoud le coup de lettres correspondant
>>> -c <cible> <nbr1> <nbr2> ... : résoud le compte correspondant

Il est aussi possible de rentre directement un coup (de lettres ou de chiffres)

>>> <10 lettres> : si les 10 lettres ne forment pas déjà un mot valide, résoud le coup de lettres correspondant
>>> <cible> <nbr1> <nbr2> ... : résoud le compte correspondant
>>> <mot> : vérifie si le mot est dans le dictionnaire DCDL

Bon jeu !

\033[0m
"""

class ExitShell(Exception):
    
    def __init__(self) -> None:
        super().__init__()

class Shell:
    
    @staticmethod
    def start():
        os.system("cls")
        print(shell_help)
    
    @staticmethod
    def run():
        Shell.start()
        try:
            while True:
                Shell.loop()
        except ExitShell:
            return
    
    @staticmethod
    def loop():
        
        msg = input("\n\033[96m>>> ")
        print("\033[0m",end="")
        
        if "quit()" in msg or "exit()" in msg:
            raise ExitShell()
        
        if msg[0]=="-":
            
        
            if "-v" in msg:
                msg = msg.replace("-v","").replace(" ","")
                
                if not msg.isalpha():
                    print("I am sorry, I dont know what you mean...")
                    Shell.loop()
                else:
                    if Dico()(msg.lower()):
                        print(f"\033[092m'{msg}'\033[0m est un mot valide !")
                    else:
                        print(f"\033[091m'{msg}'\033[0m n'est pas un mot valide !")
            
            if "-q" in msg:
                raise ExitShell()
            
            if "-c" in msg:
                msg = msg.replace("-c","")
                nums = [int(num) for num in msg.split(" ") if num.isalnum()]
                
                print()
                score,solution = solve(nums[1:],nums[0])
                
                if score==nums[0]:
                    print("Le compte est bon ! Voici comment il fallait procéder : \n")
                else:
                    print(f"Il n'était pas possible de faire mieux que {score}. Voici comment il fallait procéder :\n")
                
                print("\n".join("\t"+ line for line in solution.split("\n")))
            
            if "-l" in msg:
                msg = msg.replace("-l","").replace(" ","")
                score,solution = solve(msg)
                print(f"J'ai {score} lettres avec :",*solution)

        else:
            
            # lettres
            if all(
                [char.isalpha() or char == " " for char in msg]
            ):
                msg = msg.replace(" ","")
                
                if Dico()(msg):
                    print(f"\033[092m'{msg}'\033[0m est un mot valide !")
                else:
                    if len(msg)==10:
                        # we consider that we need to solve for those 10 lettres
                        score,solution = solve(msg)
                        print(f"J'ai {score} lettres avec :",*solution)
                    
                    else:
                        print(f"\033[091m'{msg}'\033[0m n'est pas un mot valide !")
            
            # chiffres
            elif all(
                [char.isalnum() or char=="" for char in msg.split(" ")]
            ):
                print()
                nums = [int(num) for num in msg.split(" ") if num.isalnum()]      
                score,solution = solve(nums[1:],nums[0])
                
                if score==nums[0]:
                    print("Le compte est bon ! Voici comment il fallait procéder : ")
                else:
                    print(f"Il n'était pas possible de faire mieux que {score}. Voici comment il fallait procéder :\n")
                
                print("\n".join("\t"+ line for line in solution.split("\n")))
                
                
if __name__=="__main__":
    Shell.run()
    
    