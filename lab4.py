# import numpy as np

# n = int(input("size: "))
# a = np.array([[int(input()) for i in range(n)] for j in range(n)])
# det = round(np.linalg.det(a),3)







# print(a)
# print(det)
import numpy as np

def seidel(A, b, eps):
    n = len(A)
    x = np.zeros(n)  # zero vector

    converge = False
    while not converge:
        x_new = np.copy(x)
        for i in range(n):
            s1 = sum(A[i][j] * x_new[j] for j in range(i))
            s2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (b[i] - s1 - s2) / A[i][i]

        converge = np.sqrt(sum((x_new[i] - x[i]) ** 2 for i in range(n))) <= eps
        x = x_new

    return x