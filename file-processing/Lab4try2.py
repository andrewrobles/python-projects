#!/usr/bin/python3

import csv
def readFile(filename):
    header = []
    row = [,,,]
    with open("logins.csv", "r") as newFile:
       name = csv.reader(newFile, delimiter=';')
        header = next(name)

        for lines in name:
            if (int(line[2] >= 200)):
                row.append([line[0], line[1], line[2] #stored
                print(line[0], line[1], line[2])

        newFile.close()
        return row,header


def createNewFile(row,header):
    #to r,w,a???
    #variable name / csv.writer
    #header
    #row
    #close
    #make a suspicousfile to write to

def writeFile(suspiciousFile):
    file = open('suspicousFile.txt', 'w')


#have to print 2 functions
#1) ,=
2) function()
def main():

    userInformation = readFile("employee_login.cvs")

    suspiciousFile = []