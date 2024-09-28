print('_______________NEWTON METHOD_______________')
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 2*x**6 - 4*x**4 + x**2 - 1

def df(x):
    return 12*x**5 - 16*x**3 + 2*x

def d2f(x):
    return 60*x**4 - 48*x**2 + x

def newton(starting_point, num_iterations):
    x = starting_point
    history = []
    for _ in range(num_iterations):
        x -= df(x)/d2f(x)
        history.append(x)
    return x, history

starting_point = -1.5
num_iterations = 5

min, his = newton(starting_point, num_iterations)

print(f'Sau {num_iterations} lần lặp thì giá trị tại {min:.2f} là: {f(min):.2f}')

x = np.linspace(-2, 2, 500) # tạo mảng 500 giá trị đều nhau từ -12-12
y = f(x)    

plt.plot(x, y, label='f(x)') # Tạo biểu đồ đường
plt.ylim(-3, 5) # Giới hạn trục y
plt.scatter(his, [f(x) for x in his], color='red', label='Iterations')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend() # Hiển thị thêm chú thích kiểu đường màu xanh là biểu đồ của thằng....
plt.show()