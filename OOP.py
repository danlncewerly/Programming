from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QVBoxLayout, QWidget, QLabel, QGridLayout
from PySide6.QtCore import QSize
from PySide6.QtGui import QColor


class InputWindow(QMainWindow): # окно ввода
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Окно ввода ") # устанавливаем заголовок окна 
         
        # соззаем поля для ввода и лейблы 
        self.N_label = QLabel("Размер доски: ", self)
        self.N_input = QLineEdit(self)
        self.L_label = QLabel("Нужно поставить фигур: ", self)
        self.L_input = QLineEdit(self)
        self.K_label = QLabel("Уже стоят фигуры: ", self)
        self.K_input = QLineEdit(self)
        self.coordinates_label = QLabel("Координаты фигур (x1,y1;x2,y2;...): ", self)
        self.coordinates_input = QLineEdit(self)
        # создаем кнопку 
        self.button = QPushButton('Решить', self)

        # создаем компоновщик и добавляем виджеты
        layout = QVBoxLayout()
        layout.addWidget(self.N_label)
        layout.addWidget(self.N_input)
        layout.addWidget(self.L_label)
        layout.addWidget(self.L_input)
        layout.addWidget(self.K_label)
        layout.addWidget(self.K_input)
        layout.addWidget(self.coordinates_label)
        layout.addWidget(self.coordinates_input)
        layout.addWidget(self.button)
        
        # создаем центральный виджет и вносим все элементы в него 
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.button.clicked.connect(self.on_button_clicked) # создаем сигнал на нажатие кнопки

    def on_button_clicked(self): # меод обработки нажатия кнопки
        # получаем данные из полей ввода
        N = int(self.N_input.text())
        L = int(self.L_input.text())
        K = int(self.K_input.text())
        coordinates = self.coordinates_input.text().split(';')
        s = [(int(x.split(',')[0]), int(x.split(',')[1])) for x in coordinates if x]
        # создаем объект класса ChessBoard и вызываем метод solve
        board = ChessBoard(N, L, K, s)
        first_solution_matrix = board.solve()
        if first_solution_matrix is not None:
            self.result_window = ResultWindow(first_solution_matrix)
        else:
            self.result_window = ResultWindow("Нет решений")
        self.result_window.show()

 # окно с шахматной доской
class ResultWindow(QMainWindow):
    def __init__(self, solutions):
        super().__init__()
        self.setWindowTitle("Найденное решение: ")
    

        # создаем центральный виджет 
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # создаем сетку для отображения шахматной доски 
        grid_layout = QGridLayout(central_widget)
        grid_layout.setSpacing(0)  # устанавливаем расстояние между кнопками 0, чтобы они сливались в одну доску

        # устанавливаем цвета для клеток
        colors = [QColor("white"), QColor("gray")]
       
        # если решения нет, то выводим текст, иначе отображаем доску
        if isinstance(solutions, str):
            label = QLabel(solutions)
            grid_layout.addWidget(label)
        else:
            for i, row in enumerate(solutions):
                for j, cell in enumerate(row):
                 # создаем кнопки для отображения клеток 
                    button = QPushButton()
                    button.setFixedSize(QSize(40, 40))  # устанавливаем фиксированный размер чтобы кнопки были квадратными
                    # устанавливаем цвета для клеток
                    if cell == "0":
                        color = colors[(i + j) % 2]
                        button.setStyleSheet(f"background-color: {color.name()};") #  устанавливаем цвет фона кнопки
                        button.setStyleSheet(f"background-color: {color.name()}; border: 1px solid black;") # устанавливаем цвет границы кнопки
                    
                    elif cell == "#":
                        button.setStyleSheet("background-color: red;")
                        button.setStyleSheet("background-color: red; border: 1px solid black;")
                    elif cell == "*":
                        button.setStyleSheet("background-color: green;")
                        button.setStyleSheet("background-color: green; border: 1px solid black;")
                    # добавляем кнопку в сетку
                    grid_layout.addWidget(button, j,i)

# класс для решения задачи
class ChessBoard:
    def __init__(self, N, L, K, s):
        self.N = N
        self.L = L
        self.K = K
        self.s = s
        self.solutions = set()


    # создаем пустую доску
    def matrix_board(self):
        return [['0' for _ in range(self.N)] for _ in range(self.N)]
    
    # отмечаем возможные ходы фигуры   
    def mark_solutions(self, x, y, matrix):
        possible_moves = [(x-2, y+2), (x-1, y+1),(x+1, y+1), (x+2, y+2),(x-1, y-1), (x-2, y-2),(x+1, y-1), (x+2, y-2)]
        matrix[x][y] = "#"
        for i in possible_moves:
            if 0 <= i[0] < len(matrix) and 0 <= i[1] < len(matrix):
                matrix[i[0]][i[1]] = "*"

    # создаем матрицу с решением
    def create_matrix(self, matrix, posing):
        new_matrix = matrix.copy()
        for x, y in posing:
            self.mark_solutions(x, y, new_matrix)
        return new_matrix
    # рекурсивный метод для поиска всевозможных решений
    def recursion(self, current_solution, current):
        # если количество фигур равно L, то добавляем решение в множество решений
        if current == self.L:
            sorted_solution = tuple(sorted(current_solution))
            self.solutions.add(sorted_solution)
            if len(self.solutions)==1:
                for i in self.create_matrix(self.matrix_board(), sorted_solution):
                    print(*i)
            return
        # перебираем все клетки доски
        for i in range(self.N):
            for j in range(self.N):
                if (i, j) not in current_solution and not Alfil.alfil_steps(i, j).intersection(current_solution):
                    new_solution = current_solution.copy()
                    new_solution.append((i, j))
                    self.recursion(new_solution, current + 1)
    # метод для записи решений 
    def solve(self):
        self.recursion(self.s, 0)
        first_solution_matrix = None
        # если решения есть, то выводим их в консоль и записываем в файл
        if self.solutions:
            print('Количество решений:', len(self.solutions))
            first_solution = list(self.solutions)[0]
            first_solution_matrix = self.create_matrix(self.matrix_board(), first_solution)
            solutions_str = [" ".join(map(str, solution)) + "\n" for solution in self.solutions]
            with open("output.txt", "w") as output_file:
                output_file.writelines(solutions_str)
        else:
            print('No solutions')
            with open("output.txt", "w") as output_file:
                output_file.writelines(solutions_str)
           
        return first_solution_matrix
       

# класс для хода альфиля
class Alfil:
    @staticmethod
    def alfil_steps(x, y):
        steps = {(x-2,y+2), (x-1,y+1),(x+1,y+1), (x+2, y+2),(x-1,y-1), (x-2,y-2),(x+1,y-1), (x+2,y-2),}
        return steps
    

if __name__=="__main__":
    app = QApplication([])
    window = InputWindow()
    window.show()
    app.exec()