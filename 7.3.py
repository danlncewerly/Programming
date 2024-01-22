def get_password(x):
    sosednie = {
        '0': ['0', '8'],
        '1': ['1', '2', '4'],
        '2': ['1', '2', '3', '5'],
        '3': ['2', '3', '6'],
        '4': ['1', '4', '5', '7'],
        '5': ['2', '4', '5', '6', '8'],
        '6': ['3', '5', '6', '9'],
        '7': ['4', '7', '8'],
        '8': ['5', '7', '8', '9', '0'],
        '9': ['6', '8', '9']
    }

    passwords = ['']
    for i in x:
        passwords = [p + sosedniy for p in passwords for sosedniy in sosednie[i]]
    return passwords


if __name__ == '__main__':
    s = input("Введите предполагаемый PIN-код: ")
print(get_password(s))
