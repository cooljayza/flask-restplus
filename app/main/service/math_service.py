def closestToZero(numbers):
    numTuple = ((abs(num),num) for num in numbers)
    sortedTuple = sorted(numTuple,key=lambda tup: tup[0])
    
    firstTuple = sortedTuple[0]
    secondTuple = sortedTuple[1]
    ## if two numbers a equally close to zero
    if(firstTuple[0] == secondTuple[0]):
        if(firstTuple[1] > secondTuple[1]):
            return firstTuple[1]
        else:
            return secondTuple[1]
    
    return sortedTuple[0][1]


def sumOfNumbersWhileLoop(numbers):
    total = 0
    count = 0
    lenNumbers = len(numbers)
    while count < lenNumbers:
        total += numbers[count]
        count += 1
    return total

def sumOfNumbersForLoop(numbers):
    total = 0
    for a in range(len(numbers)):
        total += numbers[a]
    return total

def sumOfNumbersRecursion(numbers):
    if len(numbers)==0:
        return 0
    else:
        return numbers[0] + sumOfNumbersRecursion(numbers[1:]) 