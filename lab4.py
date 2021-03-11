import numpy as np

n = int(input("size: "))
a = np.array([[int(input()) for i in range(n)] for j in range(n)])
det = round(np.linalg.det(a),3)

print(a)
print(det)