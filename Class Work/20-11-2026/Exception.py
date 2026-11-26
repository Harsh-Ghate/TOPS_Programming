"""
Try and except
"""
# a=10
# b=2
# try:
#     result = a/b
#     print("Result of division is :",result)
# except ZeroDivisionError:
#     print("Error: Division by Zero is not allowed")

# print("Program continues ")
"""
Try,except,else and finally block
"""
# try:
#     number = int(input("Enter any Number:"))
# except ValueError:
#     print("Invalid Input")
# else:
#     print(f"Entered Number {number}")
#     print("Program Executed Succesfully")
# finally:
#     print("Thank you for using the application")

try:
    age = int(input("Enter your age:"))
    if age < 18:
        raise ValueError("Age Must be 18 above")
    print("Registration Successfully")
except ValueError as error:
    print("Error:",error)