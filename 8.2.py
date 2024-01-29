#Вариант 9. Функция:  (x − 5 )^2* cos (x^2 − 7) при x принадлежит [0,5]
import numpy
import matplotlib.pyplot as plt

# Определение функции
def f(x):
    return (numpy.square((x - 5))) * (numpy.cos(numpy.square(x) - 7))

# Генерация значений для построения графика
x = numpy.linspace(0, 5, 1000)
y = f(x)

# Построение графика функции
plt.figure(1)
plt.plot(x, y)
plt.title('1) График функции')

# Вычисление производных
first_derivative = numpy.gradient(y, x)  # Первая производная
second_derivative = numpy.gradient(first_derivative, x)  # Вторая производная

# Построение графиков производных
plt.figure(2)
plt.plot(x, first_derivative,)
plt.xlabel('x')
plt.ylabel("f'(x)")
plt.title('2) Первая производная ')

plt.figure(3)
plt.plot(x, second_derivative,)
plt.xlabel('x')
plt.ylabel("f''(x)")
plt.title('3) Вторая производная')

# Нахождение наибольшего и наименьшего значения функции на отрезке
max_f = x[numpy.argmax(y)]
min_f = x[numpy.argmin(y)]
plt.figure(1)
plt.plot(max_f, f(max_f), 'o', color='b')
plt.plot(min_f, f(min_f), 'o', color='r')

#3
x0 = int(input('Введите точку x0'))  #Вводим точку х0 и находим f(x0)
y0 = f(x0)
x0_index = numpy.abs(x - x0).argmin()
first_derivative_in_x0 = first_derivative[x0_index]

tangent_equation = f(x0) + (first_derivative_in_x0 * (x - x0))  # Уравнение касательной
normal= f(x0)-(1/first_derivative_in_x0)* (x - x0)# уравнение нормали
plt.figure(1)
plt.plot(x, tangent_equation)
plt.plot(x, normal)
#4
x = numpy.linspace(0, 5, 500)
for i in x:
    x0 = i
    y0 = f(x0)
    x0_index = numpy.abs(x - x0).argmin()
    first_derivative_in_x0 = first_derivative[x0_index]
    tangent_equation = f(x0) + (first_derivative_in_x0 * (x - x0))  # Уравнение касательной
    plt.figure(4)
    plt.plot(x, tangent_equation,'g')
plt.figure(4)
plt.plot(x, f(x))
plt.title('4) касательная к множеству точек кривой')#




#5


length = numpy.trapz(f(x),x)
print('Длина кривой: ',length)





# Отображение всех графиков
plt.show()
