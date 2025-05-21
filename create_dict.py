# Weekly code challenge - Week 3

# The program creates a dictionary from  user input

# If only one dict is created, print the dictionary

# If > 1 dict is created, print a list of dictionaries


my_list = []


while True:
    name = input("Enter a name: ")
    age = int(input("Enter an age: "))
    favorite_color = input("Enter a favorite color: ")
    my_dict = {"name": name, "age": age, "favorite_color": favorite_color}
    my_list.append(my_dict)
    Exit_program = input("Do you want to exit the program? (yes/no): ")
    if Exit_program == "yes":
        if len(my_list) == 1:
            print(my_dict)
        elif len(my_list) > 1:
            print(my_list)
        break
    else:
        print("Please enter the next set of values", end="\n")
        continue
