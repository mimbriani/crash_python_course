def modulus ( x, y ) :
    """A function that tells if an integer is divisible by another

    Parameters
    ----------
    x : int 
        First integer number that we want to now if is divisible

    y : int 
        Second integer number, divisor

    Returns
    -------
    None
    
    """

    if x % y == 0 :
        print(x, " is divisible by ", y)

    else:
        print(x, " is not divisible by ", y)
        
    return 




if __name__ == '__main__' :
    print("I will evaluate if two integers can be divided by each other")
    print("If you enter real numbers, only the integer part will be considered, be careful!")

    var1 = int(input("Please, enter now the first integer: "))
    var2 = int(input("Please, enter now the second integer: "))
    
    modulus (var1, var2)
    modulus (var2, var1)

    print("All done, see you soon!")

    
