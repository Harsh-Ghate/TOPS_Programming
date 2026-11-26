
"""CRUD operations on Dictionary"""
while True:
    List1 = [
                {"Name":"Harsh",
                 "Email":"harshghate4@gmail.com",
                 "City":"Ahmedabad"}
                 ]
    print(List1[0])
    print(" 1: Create \n 2: Read \n 3: Update \n 4: Delete \n 5: Exit")
    user_input = int(input("Enter The Number for Performing an Operation:"))

    if user_input == 1:
        print("performing 1st operation of creating a new Dictionary")
        new_Dict = {}
        keys_value = int(input("Enter The Amount of items you wanna add in the dictionary in number:"))
        for i in range(keys_value):
            keys,Value = input("Enter the Key and Value: ").split()
            new_Dict[keys]=Value
        List1.append(new_Dict)
        print(List1)
    elif user_input == 2:
        print("Performing Read Operation")
        for i in List1[0]:
            print(f"{i}:{List1[0][i]}")
    elif user_input == 3:
        print("Performing The Update Operation:")
        update_key,update_value = input("Enter The New Key and Value : ").split()
        List1[0][update_key]=update_value
        print(List1)
    elif user_input == 4:
        print("Performing The Deleting Operation:")
        deleting_item = input("Enter the Key of the item which you want to delete from the Dictionary:")
        del List1[0][deleting_item]
        print(List1)
    elif user_input == 5:
        break
    else:
        print("Invalid Input")