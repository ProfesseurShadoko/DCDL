from solver.chiffres import Chiffres
from solver.lettres import Lettres
import random as rd
from .game_msg import GameMsg

class CardSet:
    
    _voyelles = {
        "a":165,
        "e":386,
        "i":160,
        "o":146,
        "u":135,
        "y":8,
    }

    _consonnes = {
        "b":28,
        "c":50,
        "d":71,
        "f":34,
        "g":26,
        "h":23,
        "j":7,
        "k":2,
        "l":95,
        "m":50,
        "n":138,
        "p":55,
        "q":22,
        "r":111,
        "s":130,
        "t":98,
        "v":31,
    }
    
    
    def __init__(self):
        self.consonnes = self.consonnes_set()
        self.voyelles = self.voyelles_set()
        self.chiffres = self.chiffres_set()
        
    def __call__(self,type:str):
        """pops an element from the set of cards.

        Args:
            type (str): "chiffre" or "consonne" or "voyelle"
        """
        
        if "ch" in type:
            return self.pop_chiffre()
        if "co" in type:
            return self.pop_consonne()
        if "vo" in type:
            return self.pop_voyelle()
        return 
    
    def pop(self,type:str):
        """pops an element from the set of cards.

        Args:
            type (str): "chiffre" or "consonne" or "voyelle"
        """
        return self.__call__(type)
    
    def pop_chiffre(self):
        if len(self.chiffres) == 0:
            GameMsg(f"NUMBERS RESET")
            self.chiffres = self.chiffres_set()
        return self.chiffres.pop()
    
    def pop_voyelle(self):
        if len(self.voyelles) == 0:
            GameMsg(f"VOWLS RESET")
            self.voyelles = self.voyelles_set()
        return self.voyelles.pop()

    def pop_consonne(self):
        if len(self.consonnes) == 0:
            GameMsg(f"CONSONANTS RESET")
            self.consonnes = self.consonnes_set()
        return self.consonnes.pop()
    
    @staticmethod
    def chiffres_set():
        out = [i for i in range(1,11)]*2 + [25,50,75,100]
        rd.shuffle(out)
        return out
    
    @staticmethod
    def voyelles_set():
        out=[]
        for key,value in CardSet._voyelles.items():
            out+=[key]*value
        rd.shuffle(out)
        return out
    
    @staticmethod
    def consonnes_set():
        out=[]
        for key,value in CardSet._consonnes.items():
            out+=[key]*value
        rd.shuffle(out)
        return out
    



class Game:
    
    duration=16
    
    def __init__(self):
        GameMsg("new game initialized")
        self.cards = CardSet()
        self.count=0
        self._next="c"
        self.score=0
    
    def pop(self,type:str,vowls:int=5)->list:
        """this function doesn't increment self.count ! please prefer self.next()

        Args:
            type (str): "chiffre" ou "lettres
            vowls (int, optional): necessary if "lettres". Defaults to 5.

        Returns:
            list: tirage (if chiffres)
        """
        out=[]
        self.count+=1
        
        if "c" in type:
            for i in range(6):
                out.append(self.cards("ch"))
            return out
        
        if "l" in type:
            for _ in range(vowls):
                out.append(self.cards("vo"))
            for _ in range(10-vowls):
                out.append(self.cards("co"))
            rd.shuffle(out)
            return out
        
        raise(Exception(f"invalid argument {type} in Game.pop"))
    
    def next(self,vowls:int=5)->list:
        """renvoie le prochain tirage (des lettres ou de chiffres, selon le précédent)
        incrémente le nombre de coups joués.

        Args:
            vowls (int, optional): nécessaire si le prochaine coup est un coup de lettres. Defaults to 5.

        Returns:
            list: list of numbers or list of strings. Both work with solve function !
        """
        if self._next=="c":
            GameMsg(f"REQUEST <CHIFFRES> [COUNT={self.count+1}]")
            self._next="l"
            return self.pop("c")
        else:
            GameMsg(f"REQUEST <LETTRES> [COUNT={self.count+1}]")
            self._next="c"
            return self.pop("l",vowls)
    
    def add_score(self,score:int)->int:
        self.score+=score

    @staticmethod
    def rd_target()->int:
        """return rd.randint(100,999)"""
        return rd.randint(100,999)
                     

if __name__=="__main__":
    """from time import perf_counter
    start = perf_counter()
    set = CardSet.voyelles_set()
    print(perf_counter()-start)
    print(set.count("a"))
    print(CardSet.consonnes_set().count("b"))
    print(CardSet.chiffres_set())
    
    cards = CardSet()
    
    for i in range(25):
        print(cards("ch"),end=" // ")"""
    
    game = Game()
    print(game.next())
    print(game.next())
    
    print("OK\n")
    
    chiffres = game.next()
    chiffres = Chiffres(chiffres, Game.rd_target())
    print(chiffres)
    
    lettres = game.next()
    lettres = Lettres(lettres)
    print(lettres)
    
    
    
    for i in range(20):
        game.next()
        
    