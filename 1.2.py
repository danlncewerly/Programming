def reverse(x):
    b = False
    if x< 0:
        b = True
        x = -x
    b = 0
    while x > 0:
        a = x % 10
        b = b * 10 + a
        x = x // 10
    if b:
        b = -b
    if b > 127 or b < -128:
        return "no solution"
    return b

if __name__ == '__main__':
    s=int(input('Введите число'))
    print(reverse(s))
