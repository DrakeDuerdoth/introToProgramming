
##Assignment One



##Question 1

def firstLastHigher(lstNumbers):
    'Returns the higher number of the first and last element in lstNumbers'
    if lstNumbers[0] > lstNumbers[-1]:
        return lstNumbers[0]
    else:
        return lstNumbers[-1]


###Question 2

import math

def circleGeometry(diameter):
    'Returns the area of the circle after inserting diameter'
    radius = diameter/2
    areaCircle = str(((math.pi)*(radius**2)))
    return (('The area is '+ areaCircle + '.'))
            

###Question 3

def isStringLengthEven(string):
    'Returns True if string length is even and False if odd.'
    if len(string)%2 == 0:
        return True
    else:
        return False
    

###Question 4

def checkStringLength(numCharacters,lst):
    'Returns True if numCharacters < # of characters in each string of lst, False if numCharacters >='
    if numCharacters < len(min(lst)):
        return True
    else:
        return False
