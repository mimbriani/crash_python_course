""" File: ex.3.4.py """

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



if __name__ == '__main__' :

    prime = prime100( 100 )

    print("Here all al the prime numbers between 2 and 100: ")
    print(prime)
