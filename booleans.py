number1 = float(input('Enter first number:'))
number2 = float(input('Enter second number:'))

if number1 > number2:
    number1bigger = True
else: 
    number1bigger = False

print('It is',str(number1bigger),'that number 1 bigger.')

#the red box checks whether number 1 is bigger than number two and sets the variable number1bigger to true or false depending on the if statement