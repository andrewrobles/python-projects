#!/usr/bin/python3

# reading the file function
def readFile(filename):
    file = open(filename, 'r')
    lines = [x.split('\n')[0].split(';') for x in file.readlines()]
    file.close()
    return lines


# writing to the file function
def writeFile(suspicious):
    # writing the list of suspicious users to a file
    file = open('suspicious.txt', 'w')
    for i in suspicious:
        # writing to the file
        file.write('{};{};{}\n'.format(i[0], i[1], i[3]))
    # closing the file
    file.close()


# main method
def main():
    # reading the files and getting a list of lists of user details
    userDetails = readFile("employee_logins.csv")

    # list to store the userDetails of suspiscious users
    suspicious = []

    # Parse the data so we have access to all of the fields 
    userDetails = [line[0] for line in userDetails]
    userDetails = [line.split(',') for line in userDetails]
    userDetails = userDetails[1:]


    # Adding attempts greater than 50 to suspicious list
    for line in userDetails:
        numAttempts = int(line[3])

        if numAttempts >= 50:
            suspicious.append(line)

    # calling the write function
    writeFile(suspicious)

    # printing the first and last name of the suspicious users
    print('Suspicious users:')
    print('First name---Last name---Login attempts')
    for i in suspicious:
        print('{} {} {}'.format(i[0], i[1], i[3]))

    # Printing number of suspicious employees
    print('Number of suspicious employees: {}'.format(len(suspicious)))


# calling the main method
main()

'''
firstname---lastname---loginattempts---
Andrew      Robles     23
'''