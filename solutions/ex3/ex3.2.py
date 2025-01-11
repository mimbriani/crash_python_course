"""File: ex3.2_solution.py
"""
def fibonacci (n) :
    """A function that calculates the Fibonacci sequence up to the n-th term

    Parameters
    ----------
    n : int 
        the n-th term of the sequence

    Returns
    -------
    : list
        a list with the Fibonacci sequence
    """
    
    fibb = [0,1]
    t1 = 0
    t2 = 1
    indx = 2
    
    # Controls on the negative indeces 
    if  n<= 0: 
        print("Need a positive index!")
        return None
        
    # Control on the first index
        
    if n == 1 :
        del fibb[1]
 
    
    
    while indx < n :
        nvalue = t1 + t2
        fibb.append(nvalue)
        t1 = t2
        t2 = nvalue
        indx += 1
        
    return fibb



def _test1():
    # Test of the fibonacci function for an input value
    n = int(input("Please, enter an integer value: "))
    
    seq = fibonacci(n)
    
    if n > 0 :
     print("The Fibonacci sequence up to the ", n, " term is ", seq)
    
    fib_even = []
    fib_odd = []
    
    
    for i in range(n) :
        if (i+1) % 2 == 0 :
            fib_even.append(seq[i])
        else :
            fib_odd.append(seq[i])
    
    print("Elements with even index:")
    print(fib_even)
    print("Elements with odd index:")
    print(fib_odd)
    
    return None



def _test2( n ):
    #Test of the fibonacci function for a given value
    seq = fibonacci(n)
    
    if n > 0 :
        print("The Fibonacci sequence up to the ", n, " term is ", seq)
    
        fib_even = []
        fib_odd = []


        for i in range(n) :
            if (i+1) % 2 == 0 :
                fib_even.append(seq[i])
            else :
                fib_odd.append(seq[i])

        print("Elements with even index:")
        print(fib_even)
        print("Elements with odd index:")
        print(fib_odd)
    
    return None




if __name__ == '__main__' :
    
    # Testing the fibonacci function for an external integer
    print("Test 1")
    _test1()
    
    #Testing the function for a fixed value
    print("Test 2")
    _test2(5)
    
    #Testing the function for a negative integer
    print("Test 3")
    _test2(-3)
