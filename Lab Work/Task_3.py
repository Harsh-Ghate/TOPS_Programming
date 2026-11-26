"""
Performing Crud operation with set{}
"""
while True:
    Set1 = {"Item1","Item2","Item3"}
    print(Set1)
    print(" 1)Create \n 2)Read \n 3)Update \n 4)Delete \n 5)Exit")
    user_input = int(input("Enter the number for performing the desire operation:"))
    if user_input == 1:
        print("Performing Operation of Creating a new Set:")
        new_set = set()
        
        number_of_set_items = int(input("Enter the amount items you want enter in the SET in number:"))
        for i in range(number_of_set_items):
            set_items = input(f"Enter the item {i}:")
            new_set.add(set_items)
        print(f"After Adding Items in the new set: {new_set}")
    
    elif user_input == 2:
        print("Performing Operation of Read a Set:")
        for i in Set1:
            print(f"Set item: {i}")

    elif user_input == 3:
        print("Performing Operation of Updating a Set:")
        index = int(input("Enter the Index number where u want to update"))
        Update_value = input("Enter the Update value: ")
        Set1[index]=Update_value
        print(Set1)
    elif user_input == 4:
        print("Performing the DELETE Operation:")
        discard_item = input("Enter the Value which you want to remove from the set:")
        Set1 = Set1.discard(discard_item)
        print(f"After Performing The Delete Operation: {Set1}")
    elif user_input == 5:
        exit
    else:
        print("Invalid Input")
            
