class BankingException(Exception):
    pass


print(">>Banking Started")
accBalance = 10000
minBalance = 2000
attempts = 0

def withdraw(amount):
    global accBalance
    global minBalance
    global attempts

    accBalance = accBalance - amount
    if accBalance>minBalance:
      print("Withdrawl Finished!!New Balance is \u20b9{}".format(accBalance))
    else:
        accBalance = accBalance+ amount
        print("Withdrawl Failed!!New Balance is Low \u20b9{}".format(accBalance))
        attempts = attempts+1

    # We are crashing the App ourselves !!
    if attempts==3:
      #  error = ZeroDivisionError("Illegle Attempts!!")
        error = BankingException("Illegle Attempts!!")
        raise error


for i in range(2):
    withdraw(2000)
print("Banking Finished")