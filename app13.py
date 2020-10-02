import math

weight = input('Weight: ')
unit = input('(L)bs or (K)g: ')

if unit.upper() == "L":
    newWeight = int(weight) * 0.454
    print(f'You weigh {newWeight} Kilograms')
elif unit.upper() == "K":
    newWeight = int(weight) * 2.205
    print(f'You weigh {newWeight} Pounds')
else:
    print('Please select an appropriate unit')