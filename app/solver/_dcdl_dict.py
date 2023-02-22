
class DicoTree:
    
    def __init__(self):
        self.is_valid=False
        self.children = [None for _ in range(26)]
    
    def __str__(self):
        return "<DicoTree object>"
    
    def __getitem__(self,char:str):
        """
        Args:
            char (str): lowercase letter

        Returns:
            DicoTree or None: returns subtree corresponding to letter, returns None if no word corresponding to the letter
        """
        return self.children[ord(char.lower())-ord("a")]
    
    def __setitem__(self,char:str,dicotree) -> None:
        self.children[ord(char.lower())-ord("a")]=dicotree
    
    def __len__(self) -> int:
        return int(self.is_word()) + sum(len(self[char]) for char in self.next_chars())
    
    def is_word(self) -> bool:
        return self.is_valid
    
    def next_chars(self) -> list:
        """
        Returns:
            list[char]: list of characters that correspond to valid subtrees
        """
        return [chr(ord("a")+i) for i in range(26) if self.children[i]!=None]

    def contains(self,word:str) -> bool:
        if len(word)==0:
            return self.is_valid
        
        next_char,new_search = word[0],word[1:]
        child = self[next_char]
        
        if (child==None):
            return False
        else:
            return child.contains(new_search)
    
    def append(self,char:str)->None:
        """Appends empty DicoTree to children

        """
        if (self[char]==None):
            self[char]=DicoTree()
    
    def append_word(self,word:str)->None:
        """Append word to root

        Args:
            word (str): lowercase word !
        """
        if (len(word)==0):
            self.is_valid=True
        else:
            char,rest = word[0],word[1:]
            self.append(char)
            self[char].append_word(rest)
    
    @staticmethod
    def create(filename:str):
        """creates DicoTree from words in filename
        """
        words = open(filename,"r").read().split("\n")
        dico = DicoTree()
        for word in words:
            if word=="":
                continue
            dico.append_word(word)   
        return dico

class Dico:
    
    _computed=None
    _filename="app/solver/_dcdl.txt"
    
    def __init__(self):
        if self._computed==None:
            #print("Contructing dictionnary...")
            Dico._computed = DicoTree.create(Dico._filename)
        self.dico=self._computed
    
    def __getitem__(self,word:str) -> bool:
        return self.dico.contains(word)
    
    def __call__(self,word:str)->bool:
        return self.dico.contains(word)

    def getTree(self)->DicoTree:
        return self.dico

Dico()
        
if __name__=="__main__":
    print(Dico()("premier"))
    print(Dico()("deuzieme"))


