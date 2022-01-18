# Balveer singh(200220)

# Write a program to find largest and smallest number among the given N numbers

lst = []
	# number of elements as input
n = int(input("Enter number of elements : "))

	# iterating till the range
for i in range(0, n):
	ele = int(input())

lst.append(ele) 			
lst.sort()
print(lst[0],"is smallest no.")
