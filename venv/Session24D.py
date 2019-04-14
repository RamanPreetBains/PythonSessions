import matplotlib.pyplot as plt
import  numpy as np

X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Y = [11, 7, 8, 12, 33, 22, 13, 18, 27, 17]

plt.scatter(X, Y)
plt.show()

X1 =  np.random.randn(20)
Y2 =  np.random.randn(20)
print(X1)
print(Y2)

plt.scatter(X1, Y2)
plt.show()