# This is a simple calculator.
# It can add, subtract, multiply, and divide two user inputs.


try:
	number1 =  int(input("Enter the first number: "))
	number2 =  int(input("Enter the second number: "))
except ValueError:
	print("Please enter a valid number")
	pass
else:
	operation = input("Enter the operation (+, -, *, /): ")
	# Perform addition operation
	if operation == "+":
		print(number1 + number2)
		
	# Perform subtraction operation
	if operation == "-":
		print(number1 - number2)
		
	#Perform multiplication operation
	if operation == "*":
		print(number1 * number2)

	# Perform division operation
	if operation == "/":
		div= round(number1 / number2, 2)
		print(div)






