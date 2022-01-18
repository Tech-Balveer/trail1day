# Write a program to perform selection sort.
# Selection sort in Python
# creating an empty list

lst = []

# number of elements as input
n = int(input("Enter number of elements : "))

# iterating till the range
for i in range(0, n):
	ele = int(input())

	lst.append(ele) # adding the element
	


for i in range (0,len(lst)):
    for j in range (i+1,len(lst)):
        if(lst[i]>lst[j]):
            temp=lst[i]
            lst[i]=lst[j]
            lst[j]=temp

print(lst)
    
