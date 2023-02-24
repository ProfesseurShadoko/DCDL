
class ChiffresSolver:
    
    memory={}
    compute_best=True
    
    @staticmethod
    def solve_memoized(numbers:list,target:int)->tuple:
        """returns (result:int,solution:str)"""
        key = ChiffresSolver.toString(numbers,target)
        
        #let's not twice the same thing (this is O(1))
        if key in ChiffresSolver.memory:
            return ChiffresSolver.memory[key]
        
        #base case
        if len(numbers)==1:
            return numbers[0],""
        
        #let's find best result by searching over the cards
        best_result=numbers[0]
        
        for number in numbers:
            if abs(number-target)<abs(best_result-target):
                best_result=number
        best_solution=""
        
        for n1 in numbers:
            if best_result==target:
                if not ChiffresSolver.compute_best:
                    break
            numbers.remove(n1)
            
            for n2 in numbers:
                if best_result==target:
                    if not ChiffresSolver.compute_best:
                        break
                numbers.remove(n2)
                
                n_max,n_min=max(n1,n2),min(n1,n2)
                
                for ope in ["+","-","//","*"]:
                    
                    if ope!="//" or n_max%n_min==0:
                        new_card = eval(f"{n_max}{ope}{n_min}")
                        
                        if new_card!=0 and not new_card in [n1,n2]:
                            numbers.append(new_card)
                            result,solution = ChiffresSolver.solve_memoized(numbers,target)
                            
                            solution=f"{n_max}{ope}{n_min}={new_card}\n"+solution
                            
                            if abs(result-target)<=abs(best_result-target):
                                if abs(result-target)<abs(best_result-target) or len(solution) < len(best_solution):
                                    #une meilleure solution ou une solution plus courte
                                    best_result=result
                                    best_solution=solution
                                    
                            numbers.remove(new_card)
                
                numbers.append(n2)
            numbers.append(n1)
        
        numbers.sort()
        #storing best solution
        ChiffresSolver.memory[ChiffresSolver.toString(numbers,target)]=best_result,best_solution
        
        return best_result,best_solution.replace("//","/")
                        
    
    @staticmethod
    def toString(numbers:list,target:int):
        return " ".join(str(number) for number in sorted(numbers))+" "+str(target)
    
    @staticmethod
    def solve(chiffres:list,target:int):
        ChiffresSolver.memory={}
        return ChiffresSolver.solve_memoized(chiffres,target)

if __name__=="__main__":
    chiffres=[2,100,1,1,25,75]
    target=202
    ChiffresSolver.compute_best=False
    print(ChiffresSolver.solve(chiffres,target)[1])
    
    chiffres=[2,100,1,1,25,75]
    ChiffresSolver.compute_best=True
    print(ChiffresSolver.solve(chiffres,target)[1])
    
    
