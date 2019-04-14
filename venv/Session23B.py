import pandas as pd

nums = [10, 20, 30, 40, 50]
s1= pd.Series(nums)

ages = {"john":20, "jennie":22, "jim":24, "jack":26, "joe":28}
s2= pd.Series(ages)

print(s1)
print()
print(s2)

print(s1[0])
print(s2["jim"])