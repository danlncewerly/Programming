#Лабораторная работа №2, 9 вариант, фигура Алфил
import time

start=time.time()

global steps
s = []  #Создаем пустой список , в который будут добавляться стоящие фигуры.
def main():
    with open("input.txt", "r") as file: #Открываем файл Input.txt для чтения
        N, L, K = map(int, file.readline().split())
        solutions = set() #множество для решений
        for i in file.readlines():
            x, y = map(int, i.split())
            s.append((x, y))
    print("Размер доски: ", N,"Нужно поставить фигур: ", L, "Уже стоят фигуры: ", K, "\n","Доска:" )
    recursion(N,L,solutions,s,0)


    if solutions:
        print('Количество решений:', len(solutions))
        solutions_str = [" ".join(map(str, solution)) + "\n" for solution in solutions]
        with open("output.txt", "w") as output_file:
            output_file.writelines(solutions_str)
    else:
        print('No solutions')
        solutions_str="No solutions"
        with open("output.txt", "w") as output_file:
            output_file.writelines(solutions_str)
    finish=time.time()
    print('Время выполнения:', finish-start)


def alfil_steps(x, y): #функция принимает координаты фигуры и высчитывает все возможные шаги.
    steps = {(x-2,y+2), (x-1,y+1),(x+1,y+1), (x+2, y+2),(x-1,y-1), (x-2,y-2),(x+1,y-1), (x+2,y-2),}
    return steps



def matrix_board(N) : #функция создает матрицу N х N, заполненный нулями.
    return [['0' for x in range(N)] for x in range(N)]



def mark_solutions(x, y, matrix):# отмечает все возможные ходы фигуры вокруг этой позиции.
    possible_moves = [(x-2, y+2), (x-1, y+1),(x+1, y+1), (x+2, y+2),(x-1, y-1), (x-2, y-2),(x+1, y-1), (x+2, y-2),
    ]
    matrix[x][y] = "#"
    for i in possible_moves:
        if 0 <= i[0] < len(matrix) and 0 <= i[1] < len(matrix):
            matrix[i[0]][i[1]] = "*"

def create_matrix(matrix, posing): # cоздает и возвращает новую матрицу, копируя исходную матрицу и отмечая на ней позиции фигур.
    new_matrix = matrix.copy()
    for x, y in posing:
        mark_solutions(x, y, new_matrix)
    return new_matrix

def recursion(N,L,solutions,current_solution, current):
    if current == L: #Если текущее количество фигур равно нужному количеству L, то текущее решение добавляется в множество solutions.
        sorted_solution = tuple(sorted(current_solution))
        solutions.add(sorted_solution)
        if len(solutions)==1:

            for i in create_matrix(matrix_board(N), sorted_solution): #выводим доску на экран
                print(*i)
        return
    for i in range(N):
        for j in range(N):
            if (i, j) not in current_solution and not alfil_steps(i, j).intersection(current_solution): #Если фигуры еще нет в текущем решении и нет пересечения шагов с уже стоящими фигурами, то создается новое решение с добавлением этой фигуры и вызывается рекурсия с новым решением и увеличенным текущим количеством фигур на 1.
                new_solution = current_solution.copy()
                new_solution.append((i, j))
                recursion(N, L, solutions, new_solution, current + 1)


if __name__ == "__main__": # вызываем функцию main
    main()
