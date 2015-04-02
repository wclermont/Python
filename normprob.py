# Coder: Woody Clermont
# Normal Probability Distribution Calculator
# This program was designed to eliminate the need for a Z Table

import math

def stdev (): #this function validates the input
    while True:
        print ('\nEnter the standard deviation')
        try:
            y = float(input('Type a positive rational number: '))
            if y == 0 or y < 0:
                print ('The standard deviation must be a positive real number.')
                continue
            else:
                break
        except ValueError:
            print ('The standard deviation must be a positive real number.')      
            continue
    return (y)

def xvalue (): #this function validates the input
    while True:
        print ('\nEnter the x value')
        try:
            y = float(input('Type a positive or negative rational number: '))
            break
        except ValueError:
            print ('The x value must be a real number.')      
            continue
    return (y)

def pmean (): #this function validates the input
    while True:
        print ('\nEnter the population mean')
        try:
            y = float(input('Type a positive or negative rational number: '))
            break
        except ValueError:
            print ('The population mean must be a real number.')      
            continue
    return (y)

def calculator (x,y,z): #this function performs the calculation
    b = 1 /((2 * math.pi)**0.5)
    c = -1 * ((y - x)**2 / (2 * z**2))
    d = math.e**c
    p = b * d
    return (p)

def zarea (zval): #this approximates the area under the curve extending from the mean in absolute terms
    cum = 0
    count = 0
    point = 0
    for step in range(0,2000000):
        point = step/2000000
        z = zval*point
        chunk = calculator(0,z,1)
        area = (zval/2000000) * chunk
        cum += area
    if cum > 0.4999999999999999:
        cum = 0.4999999999999999
    return(cum)

def subarea(z,area): #this approximates the area from the left tail
    if z < 0:
        remain = .5 - area
    elif z > 0:
        remain = .5 + area
    else:
        remain = 0
    return(remain)

calc_cont = 0

while True: #this while statement is the main program
    print ('\nThis program can calculate the Probability Density Function and the area under the curve.')
    meanp = pmean()
    xval = xvalue()
    stdevs = stdev()
    z = (xval - meanp)/stdevs
    zpos = abs(z)
    answer = calculator(meanp,xval,stdevs)
    area = zarea(zpos)
    actarea = subarea(z,area)
    print ('\nYour z score is going to be ', z, '.', sep='')
    print ('\n', 'P(', xval, ') = ', answer, '. And additionally the area from the mean of ', meanp, ' to ', xval, ' should be ', area, '.\n', sep='')
    print ('Moreover, the area extending from the left tail to ', xval, ' is ', actarea, '.\n', sep='')
    calc_cont = input('Do you want to end the calculator? (Type 1 to end the program, or else it will continue.)\n')
    if calc_cont == '1':
        break #if the user presses 1 the program terminates
    else:
        continue #else the calculator will ask for new input and keep going
    

