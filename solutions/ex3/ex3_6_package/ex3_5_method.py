"""File: ex3.5_module.py
"""

def prime100(n):
    """A function that finds all the prime numbers up to a given value

    Parameters
    ----------
    n : int 
        the value up to which we find the prime numbers

    Returns
    -------
    : list
        a list with the prime numbers up to n
    """
    numbers = {n for n in range(2,n+1)}


    prime = numbers

    # Iterating on all the elements a set with the multiples of each number is generated
    
    for i in numbers:
        multiples = {i * j for j in range(2, 100 // i + 1)}

        # Subtractiong the multiples from the set with all the numbers
        prime = prime - multiples
        

    # Sort the number in increasing order
    prime = sorted(prime)  
        
        
    return prime



def scomposition(n):
    """A function that decompose a given number in prime factors

    Parameters
    ----------
    n : int 
        the number we want to decompose

    Returns
    -------
    : list
        of the prime factors of n
    """
    factors = []

    # The divisors are found computing all the prime numbers up to n
    divisors = prime100(n)
    i = 0

    # Until I reach 1 I iterate on all the prime numbers
    while n > 1:
        while n % divisors[i] == 0:
            factors.append(divisors[i])
            n /= divisors[i]
    
        i +=1
    return factors


def _test():
    """A test function that checks if the decomposition is done correctly

    Parameters
    ----------
    

    Returns
    -------
    : None
    """
    # Check the decomposition for all the numbers between 1 and 100
    # First decompose  
    for n in range(1,101):
        factorize = scomposition(n)
        
        # Secondly I multiply back to check
        check=1
        for fac in factorize:
            check *= fac
            
        if check != n : (print("Something went wrong for n = ",n))
            
    print("All done!")
    
    return None




if __name__ == '__main__' :
    # portion of code with self-checks
    
    _test()
