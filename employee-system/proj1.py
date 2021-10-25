# This employee class gathers multiple user information to be used in subsequent functions
class Employee:
    def __init__(self, empID, firstName, lastName, deptCode, superName, linuxAccID, tempPass, connServer):
        #constructors
        self.empID = empID
        self.firstName = firstName
        self.lastName = lastName
        self.deptCode = deptCode
        self.superName = superName
        self.tempPass = tempPass
        self.connServer = connServer
        self.linuxAccID = linuxAccID

def displayReport(employeeDatabase):
    print("Summary Report of User Records")
    print("===================================")
    print(str(len(employeeDatabase)) + " record(s) created:")
    print("Department Code   Employee Count")
    print("===================================")
    for departmentCode, employeeCount in getDepartmentInfo(employeeDatabase).items():
        print("{}            {}".format(departmentCode, employeeCount))
    print("===================================")
    print("Servers Requested   Employee Count")
    print("***********************************")
    for serverName, employeeCount in getServerInfo(employeeDatabase).items():
        print("{}            {}".format(serverName, employeeCount))
    print("***********************************")
    print("Employee Details")
    print("===================================")
    for employee in employeeDatabase.values():
        print("Name: {} {}".format(employee.firstName, employee.lastName))
        print("Employee Id: {}".format(employee.empID))
        print("Department: {}".format(employee.deptCode))
        print("Supervisor: {}".format(employee.superName))
        print("Username: {}".format(employee.linuxAccID))
        print("")
        print("")
        
def getDepartmentInfo(employeeDatabase):
    departmentCounts = {}
    
    for employee in employeeDatabase.values():
        if employee.deptCode not in departmentCounts:
            departmentCounts[employee.deptCode] = 1
        else:
            departmentCounts[employee.deptCode] += 1
            
    return departmentCounts

def getServerInfo(employeeDatabase):
    serverCounts = {}
    
    for employee in employeeDatabase.values():
        if employee.connServer not in serverCounts:
            serverCounts[employee.connServer] = 1
        else:
            serverCounts[employee.connServer] += 1
            
    return serverCounts

    
def storeEmployee(newEmployee):
    # Validate employee by checking for duplicates
    if newEmployee.empID not in employeeDatabase:
        # Store employee in database
        employeeDatabase[newEmployee.empID] = newEmployee


shouldContinueProgram = True
questionsList = [
             "Enter the user's employee id:", 
             "Enter the user's first name:", 
             "Enter the user's last name:", 
             "Enter the user's department number:", 
             "Enter the user's supervisor (full name):", 
             "Enter the user's Linux account ID:", 
             "Enter the user's temporary password:", 
             "Enter the name of the server they’ve requested:", 
             "Would you like to create another record (type yes or Y to Continue)"
            ]
employeeDatabase = {}

while True:
    answersList = []
    
    for currentQuestion in questionsList:
        userInput = input(currentQuestion)
        answersList.append(userInput)
        
    newEmployee = Employee(answersList[0], 
                       answersList[1], 
                       answersList[2], 
                       answersList[3], 
                       answersList[4],
                       answersList[5],
                       answersList[6],
                       answersList[7],
                      )
    
    storeEmployee(newEmployee)
    
    if answersList[-1] == 'N' or answersList[-1] == 'no':
        break
        
displayReport(employeeDatabase)