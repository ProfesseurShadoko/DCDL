from solver import Chiffres,Lettres


if __name__=="__main__":
    from time import perf_counter
    
    numbers = [1,2,5,25,1,3]
    target = 984
    letters = "adelfkrtso"
    
    start = perf_counter()
    ch = Chiffres(numbers,target)
    stop=perf_counter()
    print(f"Solver responded after {(stop-start)*1000:.2f} ms :\n{'#'*20}\n{ch}\n{'#'*20}")
    
    start = perf_counter()
    l = Lettres(letters)
    stop=perf_counter()
    print(f"Solver responded after {(stop-start)*1000:.2f} ms :\n{'#'*20}\n{l}\n{'#'*20}")