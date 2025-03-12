
def modulus ( x, y ) :
    """A function that checks if the first number in input is divisible by the second one

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

    var1 = int(input("Insert an integer number here: "))
    
    modulus (var1, 2)
    modulus (var1, 3)
    modulus (var1, 5)
    modulus (var1, 7)
    
   
  
