def имя1(x, y):
    return x+y

print(имя1(2, 3))

print(имя1('1 a ', 'в тесте'))

def имя2(a, b, c=2, d=5):
    return a+b+c+d

print(имя2(1, 2, 3, 4))

print(имя2(2, 6))

def имя2(a, b, c, d):
    return a + ' ' + b + ' ' + c + ' ' + d

print(имя2('1', '2', '3', '4'))

print(имя2('1', '2', d='3', c='4'))