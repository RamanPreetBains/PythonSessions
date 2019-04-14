#To create GUI WE have tkinter
from tkinter import  *
from Session17 import  *

# onClick can be any name of your choice
def onClick():
    print("Button Clicked")
    name = entryName.get()
    phone = entryPhone.get()
    age = entryAge.get()
    address = entryAddress.get()

    print(name,"|",phone,"|",age,"|",address)

    # Create Customer Object
    cRef = Customer(0,name,int(phone),int(age),address,0)

    # Create DBHelper Object
    dbHelper = DBHelper()
    dbHelper.saveCustomerInDB(cRef)


window = Tk()

lblTitle = Label(window, text= "Add customer details below:")
lblTitle.pack() # Pack the lable in window

lblName = Label(window, text= "Enter Customer name:")
lblName.pack() # Pack the lable in window

entryName = Entry(window) # Rectangular text field where user will enter the data
entryName.pack()

lblPhone = Label(window, text= "Enter Customer Phone:")
lblPhone.pack() # Pack the lable in window

entryPhone = Entry(window) # Rectangular text field where user will enter the data
entryPhone.pack()

lblAge = Label(window, text= "Enter Customer name:")
lblAge.pack() # Pack the lable in window

entryAge = Entry(window) # Rectangular text field where user will enter the data
entryAge.pack() 

lblName = Label(window, text= "Enter Customer name:")
lblName.pack() # Pack the lable in window

entryName = Entry(window) # Rectangular text field where user will enter the data
entryName.pack()

btnAddCustomer = Button(window, text="Add Customer", command=onClick)
btnAddCustomer.pack()

# Keep on running the process
window.mainloop() 
