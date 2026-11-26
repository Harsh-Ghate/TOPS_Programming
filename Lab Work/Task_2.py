
#Task2
"""performing CRUD Operations on list"""
while True:
    list1 = ["item1","item2","item3"]
    print(f"list item : {list1} ")
    print(" 1: Create \n 2: Read \n 3: Update \n 4: Delete \n 5: Exit")
    number = int(input("Enter the Number any of the above for performing operation : "))

    if number == 1: 
        print("performing 1st operation of creating a new list")
        new_list=[]
    
        amount_item = int(input("Enter the amount items you want enter in the list in number:"))
        print(f"Amount of items : {amount_item}")

        for i in range(0,amount_item,1):
            new_item = (input(f"Enter the Item {i}: "))
            new_list.append(new_item)
        print(f"printing the new list : {new_list}")
    elif number == 2:
        print("Performing Read Operation")
        for i in range(len(list1)):
            print(list1[i])
    elif number == 3:
        print("Performing The Update Operation:")
        index = int(input("Enter The Index number for updating the item on that index: "))
        new_item = (input("Enter the Item : "))
        list1[index]=new_item
        print(f"printing the new list : {list1}")
    elif number == 4:
        print("Perfroming Delete operation:")
        delete = input("Enter the item you want delete:")
        list1.remove(delete)
    elif number == 5:
        break
    else:
        print("Invalid Input")

