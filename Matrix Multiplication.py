print('_______________NHÂN MA TRẬN__________________')
import numpy as np

# A a*n B n*b -> results a*b
A = np.array([[1, 5], [0, 9]])
B = np.array([[2, 0], [1, 1]])
results = np.zeros((len(A), len(B[0])))

# Hàng A nhân cột B
for i in range(len(A)):
    for j in range(len(B[0])):
        # cố định a, b rồi giờ cho thằng n chung chạy rồi cộng
        for k in range(len(B)):
            results[i][j] += A[i][k] * B[k][j]
print('Kết quả là:')
print(results) 

print('_______________MA TRẬN CHUYỂN VỊ_______________')
import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6]])
At = np.zeros((len(A[0]), len(A)))
for i in range(len(A)):
    for j in range(len(A[0])):
        At[j][i] = A[i][j]
print(f'Gốc:\n{A}')
print(f'Chuyển vị:\n{At}')

