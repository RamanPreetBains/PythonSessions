print(">>App Started")

try:
   numbers = [10,20,30,40,50]
   print("numbers[10",numbers[10])
   num1 = int(input("Enter num1"))
   num2 = int(input("Enter num2"))
   num3 = num1/num2
   print("Division is :",num3)
#except ZeroDivisionError as ref:
 #   print("Error Occured",ref)
#except IndexError as ref:
 #   print("Error Occured",ref)

except Exception as eRef:
    print("Error Occured",eRef)

finally:
    print("This must be executed")

print(">>App Finished")

# In python we have error which occur onle at runtime!!
#Runtime error is also known as Exception!!
#When error comes, program is terminated abnormally, App never Finishes!!
#App has Creshed!!
# So , as remedy we can use try and except keywords!!
