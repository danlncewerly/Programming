def zigzag(string1, num_string):
    if num_string==1:
        print(string1)
    result=""
    len_str=2*num_string-2
    for i in range(num_string):
        j=0
        while i + j < len(string1):
            result += string1[i + j]
            if i != 0 and i != num_string - 1 and j+ len_str - i < len(string1):
                result += string1[j + len_str - i]
            j += len_str
    print(result)

if __name__ == '__main__':
    s=input('введите строку')
    n=int(input('введите число'))
    zigzag(s, n)
