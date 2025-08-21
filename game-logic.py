# set [1,2,3,'*','-','x2']
#
# limit: ^2 and x16

x1 = -64
x2 = 'x16'

result = []

if type(x1) == str and type(x2) == str:
    if x1 == '*' and x2 == '*':
        result = '^2'
        print(result)
    elif x1.startswith('x') and x2.startswith('x'):
        a = int(x1[1:])
        b = int(x2[1:])

        #if (a*b) > 16 or (a*b) < -16:
        if (a*b) < 0 or (a*b) > 16:
            print("multipler out of range: 0 to 16")

        result = a*b
        print(result)
    else:
        print("illegal operation")
elif type(x1) == int and type(x2) == str:
    if x2.startswith('x'):
        a = int(x2[1:])
        result = a*x1
        print(result)
    if x2 == '*':
        #if x1 > 16 or x1 < -16:
        if x1 < 0 or x1 > 16:
            print("multipler out of range: 0 to 16")

        result = str(x1)
        print(result)
    if x2 == '^2':
        result = x1*x1
        print(result)
    if x2 == '-':
        result = -x1
        print(result)
elif type(x1) == str and type(x2) == int:
    if x1.startswith('x'):
        a = int(x1[1:])
        result = a*x2
        print(result)
    if x1 == '*':
        #if x2 > 16 or x2 < -16:
        if x2 < 0 or x2 > 16:
            print("multipler out of range: 0 to 16")

        result = str(x2)
        print(result)
    if x1 == '^2':
        result = x2*x2
        print(result)
    if x1 == '-':
        result = -x2
        print(result)
else:
    result = x1+x2
    print(result)
