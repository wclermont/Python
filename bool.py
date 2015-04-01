# Coder: Woody Clermont
# CS1101 Boolean Assignment

from prettytable import PrettyTable #imports Pretty Table so we can format our output

def compare(x,y): #This function returns 1 if x > y , 0 if x == y, and -1 if x < y
    if x > y:
        return (1)
    elif x < y:
        return (-1)
    else: #x == y
        return(0)

def validator(column,i): #Takes an input for either a or b, validates to ensure it is an integer
    while True:
        print ('\nEnter ', i, 'th row, input number ', column, sep='')
        try:
            value = int(input('Type a positive or negative whole number: '))
            return value
        except ValueError: #takes over if user enters a noninteger which triggers an error
            print ('Input number', column, 'must be an integer.')      
            continue

def operator(o): #Determines whether to use >, <, or =
    if o == 1:
        return ('>')
    elif o == -1:
        return ('<')
    else: #o == 0
        return('=')
    
a = [5, 2, 3] #creates an array with values for a(0), a(1) and a(2).
b = [2, 5, 3] #creates an array with values for b(0), b(1) and b(2).
c = [] #creates an empty array which we will use to contain numbers like 1, 0, -1
d = [] #creates an empty array which we will use to contain strings

for step in range(0,3): #code for 1st through 3rd rows (predetermined data)
    tempc = compare(a[step],b[step])
    c.append(tempc) #pushes a comparison result to the end of the array c
    tempd = str(a[step]) + ' ' + operator(tempc) + ' ' + str(b[step])
    d.append(tempd) #pushes a string corresponding to the comparison result to the end of the array d

for step in range(3,6): #code for 4th through 6th rows (user inputted data)
    print('\nThis is the input for the ', step+1, 'th row:', sep='')
    tempa = validator(1,step+1)
    a.append(tempa)
    tempb = validator(2,step+1)
    b.append(tempb)
    tempc = compare(a[step],b[step])
    c.append(tempc)
    tempd = str(a[step]) + ' ' + operator(tempc) + ' ' + str(b[step])
    d.append(tempd)

table = PrettyTable(['a','b','Result','Representation']) #make a nice looking table
table.align ['Result'] # align the results in the Result column
table.padding_width = 2 # Two spaces between column edges and contents 

for step in range(0,6):
    table.add_row([a[step],b[step],c[step],d[step]]) #add a, b, the result, and the representation row by row to the table

print('\nHere is the table with some previously generated data, and your inputted data...\n\nTable of Results\n', table, sep='')
    


