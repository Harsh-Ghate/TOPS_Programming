"""
Here's why lists fit this use case:

Lists allow us to add, remove and change items.
A shopping cart can change
Items in a list ar ordered. A stopping cart shows items in the order they are  added.
Lists allow duplicate Values



cart = ["T-shirts","lamp","Pen"] #lists
print(cart)


my_list = [1,"Python",3.14] #A list of mixed data types
print(my_list)


my_list =[] #Empty list
print(my_list)

Python List Methods

append()   Adds an item to the end of the list
pop()      returns and remove the list item or item at the given index

insert()   Inserts an item at the specified index
remove()   Removes the specified value from the list


clear()    Removes all items from the list
del(2)     Remove specific index list value
del        Remove list variable 

extend()   Adds all the items from another list (or any other iterable)
index()    Returns the index of the first matched item
count()    Returns the count of the specified item
sort()     Sorts the list in ascending/descending order
reverse()  Reverses the list 
copy()     Returns the shallow copy of a list

Built-in functions such as enumerate(),len(),max(),min(),sorted() etc.
"""