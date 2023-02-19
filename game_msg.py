from datetime import datetime

class GameMsg:
    green = "\033[0;32m"
    white = "\033[0;37m"
    
    def __init__(self,message:str):
        message = message.upper()
        print(f"{self.green}GAME-MSG{self.white} - - {self.date_str()} \"{self.green}{message}{self.white}\"")
    
    @staticmethod
    def date_str():
        return "["+datetime.now().strftime('%Y-%m-%d %H:%M:%S')+"]"
    

if __name__=="__main__":
    GameMsg("everything's fine !")