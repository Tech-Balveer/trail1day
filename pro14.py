# write a program to perform insertion sort.


lst = []

# number of elements as input
n = int(input("Enter number of elements : "))

# iterating till the range
for i in range(0, n):
	ele = int(input())

	lst.append(ele) # adding the element
	

for i in range (1,n):
    temp = lst[i]
    j=i-1
    while(j>=0 and lst[j]>temp):
        lst[j+1]=lst[j]
        j=j-1
    lst[j+1]=temp    

print(lst)   