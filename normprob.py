# Coder: Woody Clermont
# Normal Probability Distribution Calculator

import math

def stdev (): #this function validates the input
    while True:
        print ('\nEnter the standard deviation')
        try:
            y = float(input('Type a positive or negative rational number: '))
            break
        except ValueError:
            print ('The standard deviation must be a real number.')      
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

calc_cont = 0

while True: #this while statement is the main program
    meanp = pmean()
    xval = xvalue()
    stdevs = stdev()
    answer = calculator(meanp,xval,stdevs)
    print ('\n', 'P(', xval, ') =', answer, '\n')
    calc_cont = input('Do you want to end the calculator? (Type 1 to end the program, or else it will continue.)\n')
    if calc_cont == '1':
        break #if the user presses 1 the program terminates
    else:
        continue #else the calculator will ask for new input and keep going
    

