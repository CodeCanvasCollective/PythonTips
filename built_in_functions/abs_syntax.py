# Examples

# Integer
print('\nGet the Absolute Value of a Number')
print('Absolute value of -20 is:', abs(-20))  # Output => Absolute value of -20 is: 20
print('Absolute value of 20 is:', abs(20))   # Output => Absolute value of 20 is: 20

print('\n')

# Floating-point
print('\nGet the Absolute Value of a Floating-point number')
print('Absolute value of -2.15 is:', abs(-2.15))  # Output => Absolute value of -2.15 is: 2.15
print('Absolute value of 2.15 is:', abs(2.15))   # Output => Absolute value of 2.15 is: 2.15
print('\n')

# Complex Numbers
'''
For complex numbers, `abs()` returns the magnitude of the number. 
The magnitude of a complex number a + bj is calculated as sqrt(a^2 + b^2).
'''
print('\nGet the Absolute Value of a complex numbers')
print('Absolute value of 3 - 4j is:', abs(3 - 4j))  # Output => Absolute value of 3 - 4j is: 5.0
print('Absolute value of 2 - 1j is:', abs(2 - 1j))  # Output => Absolute value of 2 - 1j is: 2.23606797749979
print('\n')

# Custom Objects
'''
We can also use the `abs()` function with custom objects by defining the __abs__() method in the object's class.
'''
class MyAbsoluteNumber:
    def __init__(self, number):
        self.number = number

    def __abs__(self):
        return abs(self.number)

my_num = MyAbsoluteNumber(-30)
print(abs(my_num))  # Output: 30


# Error Handling
'''
If we pass a non-numeric value to abs(), 
Python will raise a TypeError.
'''
try:
    print(abs("string"))
except TypeError as e:
    print(e)  # Output: bad operand type for abs(): 'str'