import matplotlib.pyplot as plt
from scipy import stats
X = [1, 2, 3, 4, 5]
Y = [2, 4, 5, 4, 5]

data = stats.linregress(X,Y)
print(data[0]) #b1
print(data[1]) #b0

plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
