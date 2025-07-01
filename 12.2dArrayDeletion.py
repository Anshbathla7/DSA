import numpy as np
arr=np.array([[1,2,3,4],[13,5,66,7],[2,35,6,77],[23,5,44,56]])
newarray=np.delete(arr,0,axis=1) #--> axis=0 means row and 1 means column
print(newarray)