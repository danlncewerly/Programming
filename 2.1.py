def longest(x):
    long=""
    current=""
    for i in x:
        if i in current:
            current=current[current.index(i) + 1:]
        current += i
        if len(current) > len(long):
            long=current
    return long


if __name__ == '__main__':
    s=input('Введите строку')
    print(longest(s))
