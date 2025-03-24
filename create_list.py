# Weekly coding challenge- week 2

#The program accepts user input to create a list of integers.

#The program then adds the integers in the list.

my_list = []

add_result= 0

while True:
    try:
        user_input = int(input("Enter a number: "))
        if user_input == 0:
            print("You entered 0. Exiting program.")
            break
        else:
            my_list.append(user_input)
            continue
    except ValueError:
        print("Please enter an integer...")
  
add_result += sum(my_list)
print(f"The sum of elements in the list {my_list} is: {add_result}")