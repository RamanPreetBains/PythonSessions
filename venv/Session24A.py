import numpy as np
import matplotlib.pyplot as plt

X1 =  np.random.randn(10,10)
print(X1)

X2 =  np.random.randn(100)
print(X2)



plt.hist(X2,100)
plt.show()