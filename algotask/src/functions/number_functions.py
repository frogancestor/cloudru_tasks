def getEvenNumbers(listOfNumbers: list) -> list[int]:
    result = []
    for number in listOfNumbers:
        if type(number) is int and number % 2 == 0:
            result.append(number)
    return result

def getMax(listOfNumbers: list) -> int | float:
    if len(listOfNumbers) == 0:
        raise ValueError('Empty list error')
    maximum = listOfNumbers[0]
    for i in range(1, len(listOfNumbers)):
        if listOfNumbers[i] > maximum:
            maximum = listOfNumbers[i]
    return maximum

def getMin(listOfNumbers: list) -> int | float:
    if len(listOfNumbers) == 0:
        raise ValueError('Empty list error')
    minimum = listOfNumbers[0]
    for i in range(1, len(listOfNumbers)):
        if listOfNumbers[i] < minimum:
            minimum = listOfNumbers[i]
    return minimum

def quickSort(listOfNumbers: list) -> list:
    left = []
    middle = []
    right = []
    if len(listOfNumbers) > 1:
        pivot = listOfNumbers[0]
        for number in listOfNumbers:
            if number < pivot:
                left.append(number)
            elif number == pivot:
                middle.append(number)
            elif number > pivot:
                right.append(number)
        return quickSort(left) + middle + quickSort(right)
    else:
        return listOfNumbers