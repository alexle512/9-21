names = ["Alex", "John","Mary","Steve","John","Steve"]

#Assignment: Write a program which will remove duplicates from the array. 
finalnames = []
for item in names:
    if item not in finalnames: finalnames.append(item)
print(finalnames)


#Assignment: Write a program which finds the largest element in the array 
print(max(names, key=len))


#Assigmment: Write a program which finds the smallest element in the array
print(min(names, key=len))