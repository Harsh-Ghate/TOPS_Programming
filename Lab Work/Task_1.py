
#Task:1
"""Take 100 entries from user and append it into a list"""

new_list= ["item1","iteam2"]
amount_item = int(input("Enter the amount items you want enter in number:"))
print(f"Amount of items : {amount_item}")

for i in range(0,amount_item,1):
    new_item = (input("Enter the Iteam : "))
    new_list.append(new_item)
print(f"List after appending new items: {new_list}")
