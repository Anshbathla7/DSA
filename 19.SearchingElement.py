import numpy as np
arr=np.array([1,2,3,3,5,2,5,2,5,10])
def findElement(array,target):
    for i in range(len(array)):
        if array[i]==target:
            print(f"{target} is in the array")
            return True
    return False
         
        
a=findElement(arr,10)

print(a)