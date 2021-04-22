print('Simple calculator!')
first_number = input('First number? ')
operation = input('Operation? ')
second_number = input('Second number? ')

# perform gate test on numeric inputs
if (first_number.isnumeric() == False or second_number.isnumeric() == False):
    print('Enter numbers only')
    exit()

first_number = int(first_number)
second_number = int(second_number)
result = 0

# perform gate test on operation input and calculate corresponding result
if (operation == '+'):
    result = first_number + second_number
    label = 'sum'
elif (operation == '-'):
    result = first_number - second_number
    label = 'difference'
elif (operation == '*'):
    result = first_number * second_number
    label = 'product'
elif (operation == '/'):
    result = first_number / second_number
    label = 'quotient'
elif (operation == '**'):
    result = first_number ** second_number
    label = 'exponent'
elif (operation == '%'):
    result = first_number % second_number
    label = 'modulus'
else:
    print('Operation can only be +, -, *, /, **, or %')
    exit()

print(f'{label} of {str(first_number)} {operation} {str(second_number)} equals {str(result)}')
