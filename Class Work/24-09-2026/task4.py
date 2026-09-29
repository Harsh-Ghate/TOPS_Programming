"""Comparison of 3 numbers"""

number1=int(input("Enter the First Number: "))
number2=int(input("Enter the Second Number: "))
number3=int(input("Enter the Third Number: "))

if number1>number2:
    if number1>number3:
        print(f"{number1} is greatest")
    else:
        print(number3,"is greatest")

else:
    if number2>number3:
        print(f"{number2} is Greatest")
    else:
        print(number3,"is Greatest")