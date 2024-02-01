


#Вариант 9. Функция:  (x − 5 )^2 * cos (x^2 − 7) при x принадлежит [0,5]
import numpy
import matplotlib.pyplot as plt
# Определение функции
def f(x):
    return (numpy.square((x - 5))) * (numpy.cos(numpy.square(x) - 7))
# Генерация значений для построения графика
x = numpy.linspace(0, 5, 1001)
y = f(x)
k=0
# Построение графика функции
plt.figure(1)
plt.plot(x, y)
plt.title('1) График функции')
plt.grid()

# Вычисление производных
first_derivative = numpy.gradient(y, x)  # Первая производная
second_derivative = numpy.gradient(first_derivative, x)  # Вторая производная

# Построение графиков производных
plt.figure(2)
plt.plot(x, first_derivative,)
plt.xlabel('x')
plt.ylabel("f'(x)")
plt.title('2) Первая производная ')
plt.grid()

plt.figure(3)
plt.plot(x, second_derivative,)
plt.xlabel('x')
plt.ylabel("f''(x)")
plt.title('3) Вторая производная')
plt.grid()

# Нахождение наибольшего и наименьшего значения функции на отрезке
max_f = x[numpy.argmax(y)]
min_f = x[numpy.argmin(y)]
plt.figure(1)
plt.plot(max_f, f(max_f), 'o', color='b') # Точка максимума
plt.plot(min_f, f(min_f), 'o', color='r') # Точка минимума



#3
x0 = int(input('Введите точку x0'))  #Вводим точку х0 и находим f(x0)
y0=f(x0)
first_derivative_in_x0 = first_derivative[200*x0] # так как у нас задано 1000 точек, а функция определена с 0 до 5, то на каждую нашу целую точку приходится 200 промежуточных значений
tangent_equation = f(x0) + (first_derivative_in_x0 * (x - x0))  # Уравнение касательной
normal= f(x0)-(1/first_derivative_in_x0)* (x - x0)# уравнение нормали
plt.figure(1)
plt.plot(x, tangent_equation)
plt.plot(x, normal)

#4
plt.figure(4)
plt.grid()
for x0 in x:
    first_derivative_in_x0 = first_derivative[k]
    tangent_equation = f(x0) + (first_derivative_in_x0 * (x - x0))  # Уравнение касательной
    plt.figure(4)
    plt.plot(x, tangent_equation,'g')
    k+=1
plt.plot(x, f(x))
plt.title('4) касательная к множеству точек кривой')#



#5
length = numpy.trapz((first_derivative**2+1)**0.5,x)
print('Длина кривой:',length)
# Отображение всех графиков
plt.show()




'''
x= numpy.linspace(0, 5, 500)
for i in x:
    x0 = i
    y0 = f(x0)
    first_derivative_in_x0 = first_derivative[x0_index]
    tangent_equation = f(x0) + (first_derivative_in_x0 * (x - x0))  # Уравнение касательной
    plt.figure(4)
    plt.plot(x, tangent_equation,'g')
'''
