import numpy as np
arr=np.array([[1,2,3,4],[5,6,7,8],[2,3,45,56],[34,34,5,65]])
print(arr)

def TraverseArray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])


TraverseArray(arr)
