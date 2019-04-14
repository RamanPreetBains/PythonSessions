file = open("Session16A.py","r")
data = file.read(15)
print(type(data))  #str
print(data)

data = file.read(10)
print(data)

file.close()
print("Is file closed",file.closed)