# Coder: Woody Clermont
# Normal Probability Distribution Calculator
# This program was designed to eliminate the need for a Z Table

import math
from scipy.stats import norm

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

def calculator (zval): #this function performs the calculation
    p = norm.pdf(zval)
    return (p)

def zarea (zval): #this approximates the area under the curve extending from the mean in absolute terms
    cum = norm.cdf(zval)
    return(cum)

calc_cont = 0

while True: #this while statement is the main program
    print ('\nThis program can calculate the Probability Density Function and the area under the curve.')
    meanp = pmean()
    xval = xvalue()
    stdevs = stdev()
    z = (xval - meanp)/stdevs
    zpos = abs(z)
    answer = calculator(z)
    area = zarea(zpos)
    actarea = zarea(z)
    tails = int(((.5 - area) * 10000)+.5) / 10000.0
    print ('\nYour z score is going to be ', z, '.', sep='')
    print ('\n', 'P(', xval, ') = ', answer, '.' , sep='')
    print ('Moreover, the area extending from the left tail to ', xval, ' is ', actarea, '.\n', sep='')
    calc_cont = input('Do you want to end the calculator? (Type 1 to end the program, or else it will continue.)\n')
    if calc_cont == '1':
        break #if the user presses 1 the program terminates
    else:
        continue #else the calculator will ask for new input and keep going
    

