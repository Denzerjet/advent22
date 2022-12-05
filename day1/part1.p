def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        words = fileObj.read().splitlines() #puts the file into an array
        fileObj.close()
        return words

input = readFile("input.txt")

highestSum = 0
sumIterator = 0

for line in input:    
    if (line == ""):
        if(highestSum < sumIterator):
                highestSum = sumIterator
        sumIterator = 0
    else:
        sumIterator += int(line)

print(highestSum)
