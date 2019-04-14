def square(x):
    return x*x

lRef = lambda x :x*x
L1 = [10,20,30,40,50]
#result = map(square,L1)
result = map(lRef,L1)
print(result)
print(type(result))
print(list(result))   # Convert map into list

L2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

lm1 = lambda n: n%2 == 0
print("result:",lm1(7))

result = map(lm1, L2)
print(list(result))

result = filter(lm1,L2)
print(result)
print(type(result))
print(list(result))

X = [10, 20, 30, 40, 50, 67]
Y = [11, 22, 33, 44, 55]

lm2 = lambda P,Q: P +Q
print(lm2(10,20))

result = map(lm2, X, Y)
print(list(result7))

