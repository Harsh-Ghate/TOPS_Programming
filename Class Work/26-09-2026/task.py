"""and and or operator"""
number1=int(input("Enter the First Number :"))
number2=int(input("Enter the Second Number :"))
number3=int(input("Enter the Third Number :"))

if number1>number2 and number1>number3:
    print(number1,"is greatest")
elif number2>number1 and number2>number3:
    print(number2,"is greatest")
else:
    print(number3,"is greatest")