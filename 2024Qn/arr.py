import numpy as np

arr =np.random.randint(1,100,10)
print(type(arr))
print(arr)

arr.sort()
print(f"Sorted array: {arr}")


arr[0] = 99
print(f"Edited: {arr}")

print(arr+10)
