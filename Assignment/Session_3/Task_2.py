
"""Write a Python program that takes a user's input for the price of a Zomato order as a string, 
converts it to a float using type casting, adds 18% GST,
 and prints the final bill amount."""

user_input = input("Enter the price of your Zomato order : ")
user_input = float(user_input)
print(f"Your Final Bill is : {user_input+(user_input*18)/100}")