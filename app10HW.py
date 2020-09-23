import math

good_credit = True
cost = 1000000

print('The house costs $' + str(cost))
if good_credit:
    down_payment = cost / 10
else:
    down_payment = cost / 5
print(f'Your downpayment is ${math.ceil(down_payment)}')

good_credit = False

print('The house costs $' + str(cost))
if good_credit:
    down_payment = cost / 10
else:
    down_payment = cost / 5
print(f'Your downpayment is ${math.ceil(down_payment)}')