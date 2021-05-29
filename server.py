import json

# Read the database through opening the json file
with open('database.json') as db:
    jsonFile = json.load(db)
    data = jsonFile['employees']


def getEmployees():
    # Has to be a json file vs json.load()
    return data


def findEmployee(id):
    global data
    for employee in data:
        if employee["id"] == id:
            return employee
    return None


def getMaxID(db):
    maxID = 0
    for employee in db:
        if employee["id"] > maxID:
            maxID = employee['id']
    return maxID


def addEmployee(obj: dict):
    global data
    newEmployee = obj
    # The <= operator for sets tests for whether the set on the left is a subset of the set on the right.
    if {'email', 'age', 'name'} <= newEmployee.keys():
        newEmployee['id'] = getMaxID(data) + 1
        data.append(newEmployee)

        # Update database.json
        with open('database.json', 'w') as db:
            newJson = {'employees': data}
            json.dump(newJson, db)
    else:
        raise TypeError("Required keys missing in obj")


def removeEmployee(id):
    global data
    newEmployees = []
    exists = False
    for employee in data:
        if employee['id'] != id:
            newEmployees.append(employee)

    if data == newEmployees:
        raise ValueError("Nothing was removed")
    else:
        data = newEmployees

    # Update database.json
    with open('database.json', 'w') as db:
        newJson = {'employees': data}
        json.dump(newJson, db)


def updateEmployee(id, obj: dict):
    global data
    if 'id' in obj:
        raise ValueError('You cannot modify employee ID')

    updated = {}
    for employee in data:
        if employee['id'] == id:
            updated = employee

    if not updated:
        raise ValueError('Employee does not exist, please use add_employee')

    updated.update(obj)
    if type(updated['age']) is str:
        updated['age'] = int(updated['age'])
    # Remove old employee obj
    removeEmployee(id)
    # Created a new employee obj
    addEmployee(updated)