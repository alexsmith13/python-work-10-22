mark = int(input('Please enter a mark:'))
if mark >= 70:
    print('Distinction')
elif 70 > mark >= 60:
    print('Merit')
elif 60 > mark >= 50:
    print('Pass')
else:
    print('Fail')