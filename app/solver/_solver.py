from app.solver._chiffre_solver import ChiffresSolver
from app.solver._letter_solver import LetterSolver


def solve(*args):
    """
    Args:
        - list of numbers , target => solving for chiffres
        - string or list of strings => solving for lettres

    Returns:
        _tuple_: score,solution
    """
    if len(args)==2:
        return ChiffresSolver.solve(args[0],args[1])
    else:
        if type(args[0]==str):
            lettres = list(args[0])
        else:
            lettres = args[0]
        return LetterSolver.solve(lettres)


if __name__=="__main__":
    from time import perf_counter
    
    numbers = [1,1,2,25,9,9]
    target = 820
    letters = "natellogault"
    
    start = perf_counter()
    res,sol = solve(numbers,target)
    stop=perf_counter()
    print(f"ChiffreSolver responded after {(stop-start)*1000:.2f} ms :\n{sol}")
    
    start = perf_counter()
    res,sol = solve(letters)
    stop=perf_counter()
    print(f"LetterSolver responded after {(stop-start)*1000:.2f} ms :\n'{sol}'")




        