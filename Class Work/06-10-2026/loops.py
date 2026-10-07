"""Types of loops in Python:
    1)while loop
    2)for loop with (range function)"""

#WHILE LOOP
i=1
while  i<=10:
    print(i)
    i+=1

i=10
while i>=1:
    print(i)
    i-=1

#FOR LOOP
for i in range(1,10):
    print(i)

for i in range(10,1,-1):
    print(i)

#FOR LOOP with list
models= ["GEMINI","CHATGPT","CLAUDE"]

for i in models:
    print(i)

#FOR LOOP WITH BREAK AND CONTINUE STATMENTS
for i in range(1,10):
    if i == 5:
        break
    print(i)

for i in range(1,11):
    if i==5 or i==8:
        continue
    print(i)



#FOR LOOP WITH STRING
str="Harsh"
for i in str:
    print(i)

#The third loop in python is called as iter

"""
An iterator is an object that contains a countable number of values.
An iterator is an object that can be iterated upon, meaning that you can 
traverse through all the values.
Technically, in Python, an iterator is an object which implements the 
iterator protocol, which consist of the methods __iter__() and __next__().

Lists, tuples, dictionaries, and sets are all iterable objects. 
They are iterable containers which you can get an iterator from.


"""

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))
