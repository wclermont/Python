from scipy.stats import t

def stdevf (): #this function validates the input
    while True:
        print ('\nEnter the sample standard deviation')
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

def meanf (): #this function validates the input
    while True:
        print ('\nEnter the population mean')
        try:
            y = float(input('Type a positive or negative rational number: '))
            break
        except ValueError:
            print ('The mean must be a real number.')      
            continue
    return (y)

def xvalf (): #this function validates the input
    while True:
        print ('\nEnter the x value')
        try:
            y = float(input('Type a positive or negative rational number: '))
            break
        except ValueError:
            print ('The mean must be a real number.')      
            continue
    return (y)

def ssize (): #this function validates the input
    while True:
        print ('\nEnter the sample size')
        try:
            y = int(input('Type a positive integer: '))
            if y == 0 or y < 0:
                print ('The sample size must be a positive integer.')
                continue
            else:
                break
        except ValueError:
            print ('The sample must be a positive integer.')      
            continue
    return (y)

def alphaf (): #this function validates the input
    while True:
        print ('\nEnter the alpha value between 0 and 1 which corresponds to a tail')
        try:
            y = float(input('Type a positive decimal between 0 and 1: '))
            if y == 0 or y < 0 or y > 1:
                print ('The alpha value must be a positive decimal.')
                continue
            else:
                break
        except ValueError:
            print ('The alpha value must be a positive decimal between 0 and 1.')      
            continue
    return (y)

def tailchoice(): #this function validates that a proper operator has been selected
    while True:
        b = input('\nWhat is the tail? (1-upper, 2-lower, 3-both).\n')
        if b == '1' or b == '2' or b == '3':
            return (b)
        else:
            print('You can only choose 1-3 as options.')
            continue

def tailrev(tail,alpha):
    if tail == '3': #both
        y = alpha/2
    elif tail == '2': #lower
        y = alpha
    else: #upper
        y = alpha
    return (y)

while True: #this while statement is the main program
    print ('\nThis program can calculate the t score, the t critical value and p value for a tail.')
    print ('This program will also conduct a basic one sample hypothesis test about the population mean, population standard deviation unknown.')
    alpha = alphaf()
    tails = tailchoice()
    revalpha = tailrev(tails,alpha)
    sampsize = ssize()
    df = sampsize - 1
    xval = xvalf()
    mean = meanf()
    stdev = stdevf()
    
    critval = t.isf(revalpha, df)

    print ('\nThe critical value corresponding to an alpha level of ', alpha, ' in a single tail is ', critval, '.\n', sep='')

    if tails == '3':
        print ('There is another tail at ', critval*-1, '\n', sep='')
        
    tval = (xval - mean)/(stdev/sampsize**0.5)
    
    if tails == '1':
        pval = t.sf(tval, df)
    elif tails == '2':
        pval = 1.0000 - t.sf(tval, df)
    else:
        pval = t.sf(tval, df)
        pval2 = 1.0000 - t.sf(tval, df)
        
    print ('The calculated t stat for hypothesis tests about a population mean, population standard deviation unknown is ', tval, '.', sep = '')
    print ('And its corresponding p value is ', pval, '.\n', sep='')

    if tails == '1' or tails == '2':   
        if pval < revalpha:
            print (pval, ' < ', revalpha, ' therefore, we can reject the null hypothesis and accept the alternative hypothesis.\n', sep='')
        elif pval == revalpha:
            print (pval, ' = ', revalpha, ' therefore, we can reject the null hypothesis and accept the alternative hypothesis.\n', sep='')
        else:
            print (pval, ' > ', revalpha, ' therefore, we fail to reject the null hypothesis and have insufficient evidence.\n', sep='')
    else:
        if pval < revalpha or pval2 < revalpha:
            print ('Either ', pval, ' or ', pval2, ' < ', revalpha, ' therefore, we can reject the null hypothesis and accept the alternative hypothesis.\n', sep='')
        elif pval == revalpha or pval2 == revalpha:
            print ('Either ', pval, ' or ', pval2, ' = ', revalpha, ' therefore, we can reject the null hypothesis and accept the alternative hypothesis.\n', sep='')
        else:
            print ('Either ', pval, ' or ', pval2, ' > ', revalpha, ' therefore, we fail to reject the null hypothesis and have insufficient evidence.\n', sep='')
            
    if tails == '1':
        if tval > critval:
            print (tval, ' > ', critval, ' therefore, we can reject the null hypothesis and accept the alternative hypothesis.\n', sep='')
        elif tval == critval:
            print (tval, ' = ', critval, ' therefore, we can reject the null hypothesis and accept the alternative hypothesis.\n', sep='')
        else:
            print (tval, ' < ', critval, ' therefore, we fail to reject the null hypothesis and have insufficient evidence.\n', sep='')

    if tails == '2':
        tval2 = abs(tval)
        critval2 = abs(critval)
        if tval2 > critval2:
            print ('The absolute value of ', tval, ' > ', critval, ' therefore, we can reject the null hypothesis and accept the alternative hypothesis.\n', sep='')
        elif tval2 == critval2:
            print ('The absolute value of ', tval, ' = ', critval, ' therefore, we can reject the null hypothesis and accept the alternative hypothesis.\n', sep='')
        else:
            print ('The absolute value of ', tval, ' > ', critval, ' therefore, we fail to reject the null hypothesis and have insufficient evidence.\n', sep='')

    if tails == '3':
        tval2 = abs(tval)
        critval2 = abs(critval)
        if tval2 > critval2:
            print ('The absolute value of ', tval, ' > ', critval, ' therefore, we can reject the null hypothesis and accept the alternative hypothesis.\n', sep='')
        elif tval2 == alpha2:
            print ('The absolute value of ', tval, ' = ', critval, ' therefore, we can reject the null hypothesis and accept the alternative hypothesis.\n', sep='')
        else:
            print ('The absolute value of ', tval, ' < ', critval, ' therefore, we fail to reject the null hypothesis and have insufficient evidence.\n', sep='')

    calc_cont = input('Do you want to end the calculator? (Type 1 to end the program, or else it will continue.)\n')    

    if calc_cont == '1':
        break #if the user presses 1 the program terminates
    else:
        continue #else the calculator will ask for new input and keep going
