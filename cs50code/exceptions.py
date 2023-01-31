import sys

try:
    x = int(input('x : '))
    y = int(input('y : '))
except ValueError:
    print('Error: Invalid input')

try: 
    result = x / y
except ZeroDivisionError: # detects if the user divides by the zero
    print('Error: Cannot divide by 0.')
    sys.exit(1) # exits the program

print(f'{x} / {y} = {result}')