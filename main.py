import string

print("Enter something (i will give you the acronym)")
name = input()
nameArray = []
nameArray = name.split(" ")
arrayLen = len(nameArray)
iteration = 0
arrayFistLetter = []
for i in range(arrayLen):
    firstLetter = nameArray[iteration][:1]
    arrayFistLetter.append(firstLetter)
    print(arrayFistLetter[iteration].upper(), end=".")
    iteration = iteration + 1


