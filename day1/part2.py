def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        words = fileObj.read().splitlines() #puts the file into an array
        fileObj.close()
        return words

input = readFile("input.txt")

highestSum = 0
sumIterator = 0
arr = []

for line in input:    
    if (line == ""):
        arr.append(sumIterator)
        sumIterator = 0
    else:
        sumIterator += int(line)

arr.sort()

sum = arr[len(arr) - 1] + arr[len(arr) - 2] + arr[len(arr) - 3]

print(sum)
