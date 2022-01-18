 # Balveer singh(200220)

 #Write a python program to test following string operation.

College =" Govind Ballabh Pant Engineering College "

	# ------------------concatenation------------------
place =", Pauri-Garhwal "
FullName=College+place
print("Concatenation : ",FullName) 		# Add both Strings


	# ------------------Repetition------------------
print(FullName*4) 

	#------------------indexing------------------
print(FullName.index('Govind'))
print(FullName.index("College"))
print(FullName[23]) 				#Value at Index[23]


	#------------------(indexing from end)------------------
print(FullName[-5:-2])


	#------------------Slicing------------------
slice1= slice(4)
print(FullName[slice1])

slice2=slice(1,15,6)
print(FullName[slice2])

print(FullName[0:12:2])


# ------------------Comparison------------------
print("Govind"=="Govind")
print("Govind"=="Pant")
print("Govind"<"Pant") 


#----------------Size-----------------
counter = 0
for c in FullName: # traverse the string “FullName”
    counter+=1 #increment the counter
print (counter) # outputs the length (9) of the string “educative”

#----------------Using len()------------------
print("Length of FullName : ",len(FullName))

# ------------------ Search ------------------
search=FullName.find("Pauri")
print("Search at index : ",search)
