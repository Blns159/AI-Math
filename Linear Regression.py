import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
# Note: 100 * 1 ở đây đại diện cho 100 giá trị X_1, X_2, X_3,... và tương tự với y
X = 2*np.random.rand(100, 1)
y = 5 + 3*X
# Hàm mất mát MSE
def compute_cost(w, b, X, y):
    m = len(X)
    cost = (1/m) * np.sum((y - w*X + b)**2)
    return cost

# Gradient Descent
def gradient_descent_LR(X, y, learning_rate=0.1, num_interations=1000):
    m = len(X)
    w = 0
    b = 0
    cost_history = []

    for _ in range(num_interations):
        y_pred = w * X + b
        error = y_pred - y
        cost = compute_cost(w, b, X, y)
        cost_history.append(cost)

        # Tính gradient
        dw = (2/m) * np.sum(X * error)
        db = (2/m) * np.sum(error)

        # Cập nhật tham số
        w = w - learning_rate * dw
        b = b - learning_rate * db

    return w, b, cost_history

# Chạy
w_opt, b_opt, cost_history = gradient_descent_LR(X, y)
print(f'Tham số tối ưu là: b = {b_opt}, w = {w_opt}')

plt.scatter(X, y, color = 'blue', label = 'Dữ liệu')
plt.plot(X, w_opt * X + b_opt, color = 'red', label = 'Đường hồi quy')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()

# Đồ thị hàm mục tiêu
plt.plot(range(len(cost_history)), cost_history)
plt.title('Hàm MSE qua các vòng lặp')
plt.xlabel('Số lần lặp')
plt.ylabel('MSE')
plt.show()