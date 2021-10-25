def addNames():
    nameList = []
    shouldContinue = True

    while shouldContinue:

        userInput = input('What is the first name of the person?')

        if userInput == 'q' or userInput == 'Q':
            shouldContinue = False
        elif userInput == 'r' or userInput == 'R':
            userInput = input('What is the name you would like to remove?')
            if userInput in nameList:
                nameList.remove(userInput)
        else:
            firstName, lastName = userInput.split()
            name = {
                'firstName': firstName,
                'lastName': lastName
            }
            
            addToListUsingAppend(nameList, name)
            # addToListUsingInsert(nameList, name)
            # addToListUsingExtend(nameList, name)

    print('Names added to the list were:')
    print(nameList)

def addToListUsingAppend(myList, value):
    myList.append(value)

def addToListUsingInsert(myList, value):
    lastIndex = len(myList) - 1
    myList.insert(lastIndex, value)

def addToListUsingExtend(myList, value):
    myList.extend([value])

addNames()