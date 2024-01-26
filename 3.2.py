def flip(matrix): #
    n = len(matrix)
    for i in range(n // 2): #цикл который проходит половину матрицы
        for j in range(i, n-i-1):
            x = matrix[i][j] # x запоминает текущее значение
            matrix[i][j] = matrix[n-1-j][i] # изменяем значение левого верхнего угла на значение левого нижнего
            matrix[n-j-1][i] = matrix[n-1-i][n-1-j] #изменяем значение левого нижнего на правый нижний
            matrix[n-i-1][n-j-1] = matrix[j][n-1-i] # изменяем значение правого нижнего на правый верхний
            matrix[j][n-i-1] = x # значение правого верхнего заменяем на текущее
    return matrix

if __name__ == '__main__':
    matrix1 = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]]
    matrix2 = [[5, 1, 9, 11],
               [2, 4, 8, 10],
               [13, 3, 6, 7],
               [15, 14, 12, 16]]
    print(flip(matrix1))
    print(flip(matrix2))
