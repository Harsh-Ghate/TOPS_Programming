"""
Regular Expression
"""
import re

text = "My age is 25 and my brother's age is 30"
result = re.findall(r"\d+",text)
print(result)
print(type(result))

"""
Search function
"""

text = "Contact number is 9876543212"
result = re.search(r"\d{10}",text)
if result:
    print("Mobile Number found:",result.group())
else:
    print("Mobile number not found")

"""
Sub Function
"""
text = "My Mobile Number is 9876543212"
result = re.sub(r"\d{10}","xxxxxxxxxx",text)
print(result)

"""
Sub function for removing
"""

text = "Hello@Python123!"

result = re.sub(r"[^a-zA-Z0-9]", "",text)
print(result)

