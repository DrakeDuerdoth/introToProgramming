
#Assignment Three

#Problem One

def createStudentDict():
    '''Turns file into a dictionary'''
    try:
        infile = open ('students.csv','r')
    except (IOError):
        print('Sorry, cannot find file.')
    dctStudents = {}
    for idNumber in infile:
        idNumber = idNumber.replace('\n','')
        idNumber = idNumber.split(',')
        idNumber[2] = int(idNumber[2])
        dctStudents[idNumber[0]] = idNumber[1:4]
    infile.close()
    return(dctStudents)

#Pseudocode for Problem One
'''
Create function to open students spreadsheet, read only
Create empty dictionary
Create for loop to replace '\n' with ''
    Split lines by commas (.split())
    Turn ages into integers
    Make ID number the key and the rest of the line the values
    Close file
    Return dictionary
'''

#Problem Two

def searchStudentDictionary(dctStudents):
    '''Returns list of ID numbers. Enter ID number
    to receive more information about the student'''
    print('Here is a list of keys in your dictionary:')
    while True:
        for keys in dctStudents.keys():
            print(keys, end = '\t')
        try:
            userKey = input('\n\nChoose a key: ')
            (dctStudents[userKey])
        except (KeyError):
            print('That student is not in the class.\n'
                  'Please choose from the following: ')
        if userKey in dctStudents:
            print('Name: {}' '\n' 'Age: {}' '\n' 'Occupation: {}'
                  .format(dctStudents[userKey][0],
                          dctStudents[userKey][1],
                          dctStudents[userKey][2]))
            return










    
