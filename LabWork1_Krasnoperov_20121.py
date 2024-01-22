# Функция для нахождения наших решений
def find_solution(numbers, total_sum):
    n = input_data[0]
#создаем рекурсию где i - индекс текущего числа, current_sum - текущая сумма, а - текущее выражение
    def recursion(i,current_sum,a):
        if i==n:
            if current_sum==total_sum: #проверка на равенство сумм после прохода
                return a
        else:
            #  Если не прошли по всем числам, то добавляем плюс
            for_plus=recursion(i+1,current_sum+numbers[i],a+f"+{numbers[i]}")
            if for_plus:
                return for_plus
            # добавляем минус
            for_minus=recursion(i+1,current_sum-numbers[i],a+f"-{numbers[i]}")
            if for_minus:
                return for_minus

    final_result=recursion(1,numbers[0],str(numbers[0])) # запускаем рекурсию и ищем решение, если его нет, то выводим "no solutuon"
    print(final_result)
    if final_result:
        return final_result
    else:
        return "no solution"
if __name__ == '__main__':
    # Прочитаем файл Input.txt c веденными данными и запишем в список input_data
    input_file=open('input.txt')
    input_data = list(map(int,input_file.readline().split()))
    # Создаем файл output.txt, записываем в него наше решение
    result= open('output.txt', 'w')
    result.write(find_solution(input_data[1:-1], input_data[-1]))
