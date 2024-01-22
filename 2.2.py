def func(input_s):
    words=input_s.strip().split()
    new_s=' '.join(words[::-1]).capitalize()
    return new_s


if __name__=='__main__':
    s=input("Введите строку: ")
    print(func(s))
