from app.solver._solver import solve
import random as rd

class Chiffres:
    
    time=0
    timeout=0
    
    def __init__(self,chiffres:list,target:int):
        self.chiffres = chiffres
        self.target = target
        self.score, self.solution = solve(chiffres,target)
        rd.shuffle(self.chiffres)
    
    def totalIsRight(self)->bool:
        return self.score==self.target
    
    def success_str(self)->str:
        """
        Returns:
            str: "Le compte est bon" or "Il n'était pas possible de faire mieux que {solution}..."
        """
        return 'Le compte est bon !' if self.totalIsRight() else 'Il n\'était pas possible de faire mieux que '+str(self.score)+'...'
    
    def solution_msg(self)->str:
        return "Voici comment il fallait procéder :"
    
    def __str__(self)->str:
        return self.success_str()+"\n"+self.solution_msg()+"\n"+self.solution
    
    def cards_to_js(self)->str:
        return str(self.chiffres)
    
if __name__=="__main__":
    ch = [25,10,3,3,2,8]
    tg = 865
    
    ch = Chiffres(ch,tg)
    print(ch)
        


