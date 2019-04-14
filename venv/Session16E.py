class Order:
    def __init__(self, oid, restaurant, price):
        self.oid = oid
        self.restaurant = restaurant
        self.price = price

    def ordertoCSV(self):
        return "{},{},{}\n".format(self.oid, self.restaurant,self.price)

#Objects created below are temporary as they are in RAM
o1 = Order(1, "Basant", 1000)
o2 = Order(2, "Bistro", 1200)
o3 = Order(3, "Rishi", 700)

print(o1.ordertoCSV())
print(o2.ordertoCSV())
print(o3.ordertoCSV())

file = open("orders.csv","a")
file.write(o1.ordertoCSV())
file.write(o2.ordertoCSV())
file.write(o3.ordertoCSV())

file.close()


print("Orders saved in file")
