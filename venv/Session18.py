import mysql.connector
# Model : which will hold data
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

# DAO or Data Access Object : Used to perform DB Operations
# CRUD Operations -> Create Retrieve Update and Delete

class DBHelper:
    def saveCustomerInDb(self, cRef):
        sql = "insert into customer values(null, '{}', '{}', {}, '{}',10)".format( cRef.name, cRef.phone, cRef.age, cRef.address)
        con  = mysql.connector.connect(user = 'root', password = "", host = "127.0.0.1", database="customer")
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        print(">>Customer saved")

    def updateCustomerInDB(self, cRef):
        sql = "update customer set name = '{}', phone= '{}', age = {}, address = '{}' where cid = {} ".format(cRef.name, cRef.phone, cRef.age, cRef.address, cRef.cid)
        con = mysql.connector.connect(user = 'root', password = "", host = "127.0.0.1", database= "customer")
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        print(">>Customer updated")

    def deleteCustomerFromDB(self, cid):
        sql = "delete from customer where cid = {} ".format(cid)
        con = mysql.connector.connect(user='root', password="", host="127.0.0.1", database="customer")
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        print(">>Customer deleted")

    def FetchCustomerFromDB(self):
        sql = "Select * from customer"
        con = mysql.connector.connect(user='root', password="", host="127.0.0.1", database="customer")
        cursor = con.cursor()
        cursor.execute(sql)

        rows = cursor.fetchall()
        #print(rows)
        #print(type(rows))
        for row in rows:

      #print(row)
            cRef = Customer(row[0], row[1], row[2], row[3], row[4])
            cRef.showCustomer()
            print()


cid = int(input("Enter your cid:"))
name = input("Enter your name:")
phone = int(input("Enter your phone:"))
age = int(input("Enter your age:"))
address = input("Enter your address:")


cRef = Customer(cid,name,phone,age,address)
#cRef1 = Customer(3, "Nisha", 9645785274, 28, "country Homes")

#dbRef = DBHelper()
#dbRef.updateCustomerInDB(cRef1)

#cRef1 = Customer(0, "Ria", 9641505274, 21, "Windsor")
#cRef2 = Customer(16, "kim ", 964552639, 28, "northern clover")

dbhelper = DBHelper()
dbhelper.saveCustomerInDb(cRef)
#dbhelper.saveCustomerInDb(cRef2)

#dbhelper.updateCustomerInDB(cRef2)
#dbhelper.deleteCustomerFromDB(2)
#dbhelper.FetchCustomerFromDB()


