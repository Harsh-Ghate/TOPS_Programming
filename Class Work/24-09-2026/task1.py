"""
conditonal statments:

when our program goes on multiple ways it is called conditional statements

There are 3 types of condtions:

1)Normal if/else
2)ladder if/else
3)Nested if/else
"""
age=int(input("Enter age:"))

if(age>100):
    print("Invalid age")

elif(age>=18):
    print("Eligible for voting")

else:
    print("Not Eligible for voting")