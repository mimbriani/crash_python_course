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
    numbers = list(range(2, n+1))

    prime = []

    for i in range(len(numbers)):
        
        # Initializing the dividers factor    
        k = 0
    
        for j in range(len(numbers)):
            if numbers[i] % numbers[j] == 0 :
                k += 1

        # A prime number should be divisible only for itself between the elements on our list
        if k == 1:
            prime.append(numbers[i])


    return prime



if __name__ == '__main__' :

    prime = prime100( 100 )

    print("Here all al the prime numbers between 2 and 100: ")
    print(prime)
