def spiralka(matrix):
    result = []
    while matrix:
        result += matrix.pop(0)
        if matrix and matrix[0]:
            for i in matrix:
                result.append(i.pop())
        if matrix:
            result += matrix.pop()[::-1]
        if matrix and matrix[0]:
            for i in matrix[::-1]:
                result.append(i.pop(0))
    return result

if __name__=='__main__':
    matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
    print(spiralka(matrix1))
