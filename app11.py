has_high_income = True
has_good_credit = False

if has_good_credit and has_high_income:
    print('Eligible for loan')
else:
    print('Not eligible for laon')

has_high_income = True
has_good_credit = False

if has_good_credit or has_high_income:
    print('Eligible for loan')
else:
    print('Not eligible for laon')

has_high_income = True
has_criminal_record = False

if has_high_income and not has_criminal_record:
    print('Eligible for loan')
else:
    print('Not eligible for laon')

has_high_income = True
has_criminal_record = True

if has_high_income and not has_criminal_record:
    print('Eligible for loan')
else:
    print('Not eligible for laon')