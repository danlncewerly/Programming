def func(s):
    roman_numb = {'I': 1,
                  'V': 5,
                  'X': 10,
                  'L': 50,
                  'C': 100,
                  'D': 500,
                  'M': 1000}
    result = roman_numb[s[-1]]  # Инициализируем результат последней цифры
    for i in range(len(s) - 2, -1, -1):  # Идем с предпоследней цифры до первой (в обратном порядке)
        if roman_numb[s[i]] < roman_numb[s[i + 1]]:
            result -= roman_numb[s[i]]  # Если предыдущая цифра меньше текущей, вычитаем ее
        else:
            result += roman_numb[s[i]]  # Иначе, прибавляем ее
    return print(result)

if __name__ == '__main__':
    s=input('Введите римское число')
    func(s)
