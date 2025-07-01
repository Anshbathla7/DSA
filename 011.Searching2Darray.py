import numpy as np
arr=np.array([[1,2,3,4],[5,6,7,8],[2,3,45,56],[34,34,5,65]])
print(arr)

def SearchElement(array,value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j]==value:
                return f'the value is present in the array at the index of {i}{j}'
            
    return 'the value is not present in the array'
             

print(SearchElement(arr,65))

