import numpy as np
arr=np.array([[1,2,3,4],[5,6,7,8],[2,3,45,56],[34,34,5,65]])
print(arr)

def accessElements(array,rowIndex,colIndex):
    if rowIndex>=len(array) or colIndex>=len(array[0]):
        print('incorrect index')
    else:
        print(array[rowIndex][colIndex])
        print(len(array))


accessElements(arr,4,2)