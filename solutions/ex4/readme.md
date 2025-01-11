# Exercise 4 - Classes 

This is the directory that contains the package developed to solve the last exercise.
In the package is developed a class that handles **RATIONAL NUMBERS**

## Content
The directory contains the following files:

* A Jupyter notebook ex4classes_test.ipynb that contains some tests to make sure that the class works properly

* A sub directory [rational_package](rational_package) that effectively contains all the modules and the class. More specifically:
	- The __init__ .py file to initialize the package
	- rational_class.py that contains the definition of the class
	- In approx_method.py are contained two functions: continued_fractions that exploits the continued fraction algorithm and takes the number in input and returns the numerator and denominator of the rational number and simplify that is the function that simplify numerator and denominator whether they have common factors (that are found exploiting the functions developed for exercise 3)
	- In ex3_5_module.py there is the module developed for the previous exercise that that is needed in order to simplify the numerator and denominator. The function that are inside are prime100 that finds alla the prime numbers up to a chosen number; scomposition that returns the list of all the prime factors of a number: plus a test function for self checks.

