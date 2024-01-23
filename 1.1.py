def palindrome(x):
    if x < 0:
        return False
    x1 = x
    x2 = 0
    while x > 0:
        x2 = x2 * 10 + x % 10
        x = x // 10
    return x1 == x2

if __name__ == '__main__':
    s=int(input('Введите число'))
    print(palindrome(s))
