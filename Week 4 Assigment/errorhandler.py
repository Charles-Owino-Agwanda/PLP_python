# Task 2
# The program asks user for a file name
# Opens the file if available (try block) and prints data
# If file not available (except block) the user is notified

try:
    file = input("Enter name of file to open: ").lower()   #check file name
    with open(file, "r") as f:
        data = f.read()
        print(data)
        
except FileNotFoundError:                        #If file not found inform user. 
    print("The file does no not exits")
    