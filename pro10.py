# Balveer singh(200220)

# Write a program to find out the factorial of a given number.

def Factorial(n):
    if(n==1):
      return 1
    else:
      return Factorial(n-1)*n

take = (input("Enter a Number :"))
print(Factorial(int(take)))
