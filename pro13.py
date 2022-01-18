#Write a program to perform binary search operation.

def binary_search(list1, n):  
    low = 0  
    high = len(list1) - 1  
    mid = 0  
  
    while low <= high:  
        # for get integer result   
        mid = (high + low) // 2  
  
        # Check if n is present at mid   
        if list1[mid] < n:  
            low = mid + 1  
  
        # If n is greater, compare to the right of mid   
        elif list1[mid] > n:  
            high = mid - 1  
  
        # If n is smaller, compared to the left of mid  
        else:  
            return mid  
  
            # element was not present in the list, return -1  
    return -1  

# Initial list1  
list1 = [22, 27, 32, 39, 44, 54, 59]  
n = 39
  
# Function call   
result = binary_search(list1, n)  
  
if result != -1:  
    print("Element is present at index", str(result))  
else:  
    print("Element is not present in list1")  