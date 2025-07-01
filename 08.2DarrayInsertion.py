import numpy as np
arr=np.array([[1,2,2,4],[4,2,4,2],[3,35,2,5],[25,7,3,6]])
print(arr)

new_arr=np.insert(arr,0,[[9,4,5,5]],axis=1) #--> Here axis=0 means row, axis=1 means column
print(new_arr)