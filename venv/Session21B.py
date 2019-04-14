#import numpy Library
import numpy as np

arr1 = np.arange(10, 31)
print("arr1 is", arr1)
print()

arr3 = np.zeros((3,3,3))
print("arr3 is", arr3)
print()
arr3[0][2] = 1
print(arr3)

arr4 = np.asarray(arr3)
print(arr4)