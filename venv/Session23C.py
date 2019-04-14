import pandas as pd

nums = list(range(1, 21))
print(nums)

emp = {"eid": 101, "name": "john", "salary": 30000}

employees = [

    {"eid": 101, "name": "Mike", "salary": 40000},
    {"eid": 201, "name": "Leo", "salary": 50000},
    {"eid": 301, "name": "Fionna", "salary": 60000}

]

df3 = pd.DataFrame(employees,)
print(df3)

print(df3["eid"])
print(df3["eid"][1])

