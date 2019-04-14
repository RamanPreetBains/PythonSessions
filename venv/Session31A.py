import pandas as pd
from scipy import stats

data = pd.read_csv("advertising.csv")
# print(data)
# print(data["TV"])
# print(data["TV"].values)
# print(data["Sales"].values)

X = data["TV"].values
Y = data["Sales"].values

# print(X)
# print(Y)

##############
data = stats.linregress(X, Y)
print(data[0]) # b1
print(data[1]) # b0
"""
b0 = data[1]
b1 = data[0]

print("Manual b0 is:",b0)
print("Manual b1 is:",b1)

# Y = b0 + b1X
 
Y1 = []

for x in X:
    y = b0 + (b1*x)
    Y1.append(y)

print(Y1)
"""
"""
 Proceed Below
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.plot(X,Y, "^", X, Y1)
plt.show()
"""
"""
#Reshape 1-D List into 2-D List
X = X.reshape(len(X), 1)
Y = Y.reshape(len(Y), 1)

print(X)
print(Y)
#******************SCI-KIT****************
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

regression = LinearRegression()

regression.fit(X,Y)
Y2 = regression.predict(X)
mse = mean_squared_error(Y, Y2)
print(mse)
"""