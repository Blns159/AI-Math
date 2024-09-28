print('_______________GRADIENT DESCENT_______________')
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 2*x**6 - 4*x**4 + x**2 - 1

def df(x):
    return 12*x**5 - 16*x**3 + 2*x

def d2f(x):
    return 60*x**4 - 48*x**2 + x

def gd(starting_point, learning_rate, num_iterations):
    x = starting_point
    history = [x]

    for _ in range(num_iterations):
        grad = df(x)
        x = x - learning_rate*grad
        history.append(x)
    return x, history

starting_point = -1.5
learning_rate = 0.05
num_iterations = 500

min, his = gd(starting_point, learning_rate, num_iterations)

print(f'Sau {num_iterations} lần lặp thì giá trị tại {min} là: {f(min)}')

x = np.linspace(-2, 2, 500) # tạo mảng 500 giá trị đều nhau từ -12-12
y = f(x)    

plt.plot(x, y, label='f(x)') # Tạo biểu đồ đường
plt.ylim(-3, 5) # Giới hạn trục y
plt.scatter(his, [f(x) for x in his], color='red', label='Iterations')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend() # Hiển thị thêm chú thích kiểu đường màu xanh là biểu đồ của thằng....
plt.show()