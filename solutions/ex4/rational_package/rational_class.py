from .approx_method import *


class Rational () :
    """
    A class to represent and manage rational numbers.

    Attributes
    ----------
    numerator : int
        The numerator of the rational number.
    denominator : int
        The denominator of the rational number.
    precision : float
        The precision for approximating the rational number.

    Methods
    -------
    __init__(x, precision=1e-5):
        Initializes the rational number with a given value and precision.
    __str__():
        Returns a string representation of the rational number in 'numerator/denominator' format.
    __repr__():
        Returns the formal string representation of the Rational object.
    __abs__():
        Returns the absolute value of the rational number as a new Rational object.
    __add__(other):
        Adds two rational numbers and returns the result as a new Rational object.
    __sub__(other):
        Subtracts one rational number from another and returns the result as a new Rational object.
    __mult__(other):
        Multiplies two rational numbers and returns the result as a new Rational object.
    __truediv__(other):
        Divides one rational number by another and returns the result as a new Rational object.
    __eq__(other):
        Checks for equality between two Rational objects.
    __gt__(other):
        Compares two Rational objects to determine if one is greater than the other.
    __float__():
        Converts the Rational object to a floating-point number.
    __int__():
        Converts the Rational object to an integer.
    """
    def __init__(self, x, precision=1e-5):
        if precision <= 0 or precision > 1:
            raise ValueError("Precision must be between 0 and 1.")
            
        if type(x) == int :
            self.numerator, self.denominator = x , 1
        elif x == 0 :
            self.numerator = 0
        else :
            self.numerator, self.denominator = continued_fraction(x, precision)
        
    def __str__ ( self ) :
    	return f'Number:\n{self.numerator}/{self.denominator}'
    
    def __repr__ ( x ) :
    	return f'Rational({x}, precision=1.e-5)'
    
    def __abs__(self):
        """Return the absolute value of the rational number."""
        return Rational(abs(self.numerator)/ self.denominator)
    
    def __add__(self, other):
        num = self.numerator * other.denominator + other.numerator * self.denominator
        denom = self.denominator * other.denominator
        return Rational(num / denom) # The simplification is inside the class
    
    def __sub__(self, other):
        num = self.numerator * other.denominator - other.numerator * self.denominator
        denom = self.denominator * other.denominator
        return Rational(num / denom)
    
    def __mult__(self, other):
        num = self.numerator * other.numerator
        denom = self.denominator * other.denominator
        return Rational(num / denom)
    
    def __truediv__(self, other):
        num = self.numerator * other.denominator
        denom = self.denominator * other.numerator
        return Rational(num / denom)
    
    def __eq__(self, other):
        return (self.numerator,self.denominator) == (other.numerator, other.denominator)
    
    def __gt__(self, other):
        """Return True if self > other, False otherwise."""
        # Compare a/b > c/d by cross-multiplying: a*d > c*b
        return self.numerator * other.denominator > other.numerator * self.denominator

    def __float__(self):
        return self.numerator / self.denominator
    
    def __int__(self):
        return int(self.numerator / self.denominator)
   
