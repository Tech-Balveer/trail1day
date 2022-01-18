# Balveer singh(200220)

# Write a program to check whether the year entered by the user is Leap year or not.

year = int(input("Year = "))
if((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
		print(year, " is a leap year")
else:
	print(year, " is not a leap year")
