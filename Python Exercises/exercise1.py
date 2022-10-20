pm = int(input('Physics Marks:'))
cm = int(input('Chemistry Marks:'))
mm = int(input('Maths Marks:'))

total = pm + cm + mm
percent = total / 450 * 100
if percent >= 60:
    print('pass')
else:
    print('fail')
    
