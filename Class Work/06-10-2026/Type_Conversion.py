"""
    Python type conversion

    There are two types of type conversion in Python:
    1. Implicit Type Conversion - Automatic type conversion
    2. Explicit Type Conversion - manual type conversion

"""

#Implicit Type Conversion
integer_number=5
float_number=10.5

new_number = integer_number + float_number

print(new_number)
print(type(new_number))

#Explicit Type Conversion
d=str(integer_number)
e=int(float_number)

print(d)
print(type(d)) 

print(e)
print(type(e))