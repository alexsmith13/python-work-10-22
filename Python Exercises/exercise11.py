a=1
object = []
while a<=10:
    object.append(str(a))
    string = ','.join(object)
    string = string + '.'
    print(string)
    a=a+1