# Function with a single expression
# Function can have default arguments/inputs
def areaOfCircle(radius = 2):
    area = 3.14 * radius * radius
    return area
result = areaOfCircle(3)
print("Result is:",result)
print("Result is:",areaOfCircle(5.33))
print("Result is:",areaOfCircle())
print("Result is:",areaOfCircle(radius= 4))

#Reference Copy
area = areaOfCircle
print("Result is:",area(6))

#Lambda: is a function like a regular function
#        but it is single expression
#         it has no name , we just use the reference to the lambda function as a name

lRef = lambda radius=1: 3.14*radius*radius
lRef1 = lambda length=10, breath= 20: length*breath
print("Result with lambda is: ",lRef(5.33))
print("Result with lambda is: ",lRef())
print("Area of Rectangle is: ",lRef1())
print("Area of Rectangle is: ",lRef1(11,11))




