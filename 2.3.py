def check(string):
    str1 = []
    pairs = {
        ')': '(',
        '}': '{',
        ']': '['
            }
    for i in string:
        if i in '({[':
            str1.append(i)
        elif i in ')}]':
            if not str1 or str1[-1] != pairs[i]:
                return False
            str1.pop()
    return len(str1) == 0

def longest_string(string):
    str2 = []
    pairs = {
        ')': '(',
        '}': '{',
        ']': '['
        }
    longest_str2 = ""
    current_str2 = ""
    for i in string:
        if i in '({[':
            str2.append(i)
            current_str2 += i
        elif i in ')}]':
            if not str2 or str2[-1] != pairs[i]:
                str2 = []
                current_str2 = ""
            else:
                str2.pop()
                current_str2 += i
            if len(current_str2) > len(longest_str2):
                longest_str2 = current_str2
    if longest_str2 == "":
        return False
    return longest_str2
if __name__ == '__main__':
    s = input("Введите строку скобок: ")

    if check(s):
        print(True)
    else:
        max_string = longest_string(s)
        if max_string:
            print(max_string)
        else:
            print(False)
