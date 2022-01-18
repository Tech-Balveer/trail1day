 # Balveer singh(200220)

 # Write a program to find the largest number among the given three number

	# take inputs
num1 = float(input("Enter First Number : "))
num2 = float(input("Enter Second Number : "))
num3 = float(input("Enter Third Number : "))


	# find largest numbers
if (num1 >= num2) and (num1 >= num3):
		largest = num1
elif (num2 >= num1) and (num2 >= num3):
		largest = num2
else:
	largest = num3


	# display result
print('The largest number = ', largest)



