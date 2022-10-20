# temp = 60
# if (temp > 30):
#     print('too hot')
#     print('aagh')
#     if (temp > 50):
#         print('AAH')
# else:
#     print('too cold') #fixed code using an else statement

temp = 40
if (temp > 30):
    print('too hot')
    print('aagh')
elif (temp < 0):
    print('too cold')
else:
    print('perfect')

#best to use an elif statement as it checks the conditions in order and will only execute one of the print statements
#if if else will run the first if statement and then will run the if else pair afterwards and you'll potentially print two outputs
#if if if could result in two outputs too as a temp above 0 and 30 will satisfy both of the conditionals

