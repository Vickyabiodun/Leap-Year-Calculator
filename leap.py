"""Receives user input"""
year = int(input('which year do you want to check?'))

"""A leap year is said to be divisble by 4 with no remainder and divisble by 100 with remainder 
or divisible by 400 with no remainder and divisble by 100 with remainder

"""
if year % 4 == 0 and year % 100 != 0:
    print('this is a leap year')
elif year % 100 !=0 and year % 400 == 0:
    print('this is a leap year')
else:
    print('this is not a leap year') 