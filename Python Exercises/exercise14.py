num1 = int(input('Enter the first number:'))
num2 = int(input('Enter the second number:'))

for i in range(num1,num2+1):
    print('Table of '+str(i))
    for j in range(1,11):
        print(str(i) + ' x ' +str(j)+ ' = '+ str(i*j))