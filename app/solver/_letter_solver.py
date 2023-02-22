from app.solver._dcdl_dict import Dico

    
class LetterSolver:
    
    def __init__(self,letters:str):
        self.letters = letters.replace(" ","").replace(",","").replace(";","").replace("\n","").replace(":","")
        self.letters = list(self.letters)
        self.letters.sort()
        self.remaining = [True]*len(self.letters)
        self.dicotree = Dico().getTree()
        self.current_word = ""
        self.best_words = []
    
    def run(self):
        """finds solution by calling itself"""
        
        if self.dicotree.is_valid:
            if len(self.best_words)==0:
                self.best_words=[self.current_word]
            elif len(self.best_words[0])==len(self.current_word):
                self.best_words.append(self.current_word)
            elif len(self.best_words[0])<len(self.current_word):
                self.best_words = [self.current_word]
        
        for i in range(len(self.letters)):
            if self.remaining[i]:
                char = self.letters[i]
                if self.dicotree[char] != None:
                    tmp = self.dicotree
                    char = self.letters[i]
                    self.remaining[i]=False
                    self.current_word+=char
                    self.dicotree = self.dicotree[char]
                    
                    self.run()
                    
                    self.dicotree = tmp
                    self.remaining[i]=True
                    self.current_word = self.current_word[:-1]

    @staticmethod
    def solve(lettres:list):
        solver = LetterSolver("".join(lettres))
        solver.run()
        best_words = list(set(solver.best_words))
        result = len(best_words[0])
        return (result,best_words)
