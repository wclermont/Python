# Coder: Woody Clermont
# Simple Python Calculator

def validator (x,z): #this function validates the input of the first or second number
    while True:
        print ('\nEnter input number', x)
        try:
            y = float(input('Type a positive or negative rational number: '))
        except ValueError:
            print ('Input number', x, 'must be a real number.')      
            continue
        if z=='4' and y == 0: #this condition prevents division by 0
            print ('Division by 0 not permitted, type a different number.')
            continue
        else:
            break
    return (y)

def calculator (x,y,z): #this function performs the calculation
    global operator
    if z == '1':
        operator = '+'
        a = x + y
    elif z == '2':
        operator = '-'
        a = x - y
    elif z == '3':
        operator = '×'
        a = x * y
    else:
        operator = '÷'
        a = x / y
    return (a)

def operation(): #this function validates that a proper operator has been selected
    while True:
        b = input('What is the operator? (1-add (+), 2-subtract(-), 3-multiply (×), 4-divide (÷))\n')
        if b == '1' or b == '2' or b == '3' or b == '4':
            return (b)
        else:
            print('You can only choose 1-4 as options.')
            continue

calc_cont = 0

while True: #this while statement is the main program
    oper = '0'
    first_number = validator(1,oper)
    oper = operation()
    second_number = validator(2,oper)       
    answer = calculator(first_number,second_number,oper)
    print ('\n', first_number, operator, second_number, '=', answer, '\n')
    calc_cont = input('Do you want to end the calculator? (Type 1 to end the program, or else it will continue.)\n')
    if calc_cont == '1':
        break #if the user presses 1 the program terminates
    else:
        continue #else the calculator will ask for new input and keep going
    

