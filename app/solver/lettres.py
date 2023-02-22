from app.solver._solver import solve

class Lettres:
    
    time=0
    timeout=0
    
    def __init__(self,lettres:str):
        if type(lettres)==list:
            lettres = "".join(lettres)
        self.lettres = lettres
        self.score, self.solution = solve(lettres)
        self.target=""
    
    def success_str(self)->str:
        """_summary_

        Returns:
            str: "J'ai _ lettres avec le(s) mot(s) :"
        """
        if len(self.solution)==1:
            return f"J'ai {self.score} lettres avec le mot : "
        else:
            return f"J'ai {self.score} lettres avec les mots : "
    
    def __str__(self)->str:
        return self.success_str()+"\n"+"\n".join(self.solution)
    
    def cards_to_js(self):
        lettres = [f"'{lettre}'" for lettre in self.lettres.upper()]
        return "["+",".join(lettres)+"]"

if __name__=="__main__":
    lettres = "elmtoeiusst"
    l = Lettres(lettres)
    print(l)