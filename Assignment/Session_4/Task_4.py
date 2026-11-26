
"""<p>Finish by printing a 4-item receipt with f-strings: item name left-aligned in 15 characters, 
quantity in 6 characters, and amount right-aligned in 10 characters with `:,.2f`. 
Print a final total line using `str.format()`. Run Restart & Run All and submit the notebook.</p>"""

list1 = [["Apple",5,100],["Mango",8,200],["Banana",12,60],["Papaya",2,100]]
total=0
list2=["Items","Quantity","Amount"]
print(f"{list2[0]:<15} {list2[1]:<6} {list2[2]:>10}")
print("-"*33)
for i in range(len(list1)):
    print(f"{list1[i][0]:<15} {list1[i][1]:<6} {list1[i][2]:>10,.2f}")
    total = total + list1[i][2]
print("-"*33)
print("Total {:>27,.2f}".format(total))


