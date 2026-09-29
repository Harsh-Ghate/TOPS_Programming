"""Comparison of 2 numbers"""

number1=int(input("Enter the First Number: "))
number2=int(input("Enter the Second Number: "))

if(number1>number2):
    print("First Number:",number1,"is greater than second number",number2)

elif(number1==number2):
    print("Both First and Second Number are same")

else:
    print("Second Number:",number2 ,"is Greater than First Number:",number1)