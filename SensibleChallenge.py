numArray = []
goodLoop = "untouched"
#only considered perfectly sorted if no out of order numbers caused the variable to be touched
arraySize = 10
import random

while goodLoop != "true":
    #print("while restarted")
    numArray.clear()
    for i in range (arraySize):
        numArray.append(random.randint(1,100))        
    goodLoop = "untouched"
    
    for j in range (arraySize-1):
        if numArray[j] < numArray[j+1]:
            goodLoop = "false"
            #print(j)
            
        else:
            if goodLoop == "untouched":
                goodLoop = "true"

numArray.append(101)
#doing this so that it can check for duplicates properly
print("Sorted!")
for i in range (arraySize):
    if numArray[i] != numArray[i+1]:
        print(numArray[i])
