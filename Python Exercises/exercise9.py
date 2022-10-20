from turtle import Turtle


a=1
while True:
    if a<=10:
        if a%2==0:
            b=1
            while True:
                if b<=a:
                    print(b)
                    b=b+1
                else:
                    break
        else:
            print(a)
        a = a+1
    else:
        break