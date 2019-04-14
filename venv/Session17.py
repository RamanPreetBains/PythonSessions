import mysql.connector
class Customer:
    def __init__(self, cid, name, phone, age, address):
        self.cid = cid
        self.name = name
        self.phone = phone
        self.age = age
        self.address = address

    def showCustomer(self):
        print("===",self.cid,"|", self.name, "===")
        print("Name", self.name)
        print("phone",self.phone)
        print("age", self.age)
        print("address", self.address)
        print("===================================")


    def saveCustomerInDb(self):
        sql = "insert into customer values(null, '{}', {}, {}, '{}')".format( self.name, self.phone, self.age, self.address)
        con  = mysql.connector.connect(user = 'root', password = "", host = "127.0.0.1", database="customer")
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        print(">>Data saved")

cid = int(input("Enter your cid:"))
name = input("Enter your name:")
phone = int(input("Enter your phone:"))
age = int(input("Enter your age:"))
address = input("Enter your address:")


#cRef = Customer(1, "John", "91 9646003749", 20, "redwood Shores")
cRef = Customer(cid, name, phone, age, address)
cRef.showCustomer()
cRef.saveCustomerInDb()
