def check(string):#Функция для проверки корректности скобок
    str1 = []
    pairs = {"(": ")",
            "[": "]",
            "{": "}"
            }
    for i in string:
        if i in pairs.keys():
            str1.append(i)
        elif i in pairs.values():
            if not str1 or pairs[str1.pop()] != i:
                return False
    return len(str1) == 0


def longest_string(string):#Функция для нахождения самой длинной подстроки
    if check(string):
        return True
    else:
        str2 = ""
        n = 0
        for i in range(len(string)-1):
            for j in range(i+1, len(string)):
                if check(string[i:j]):
                    if n < len(string[i:j]):
                        n = len(string[i:j])
                        str2 = string[i:j]
        if str2:
            return str2
        else:
            return False

if __name__ == "__main__":
    s=input('Введите строку')
    print(longest_string(s))

