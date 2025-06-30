from array import *
arr=array('i',[1,4,4,5,3,5,6])
def accessElements(array,index):
    if index >= len(array):
        print("there is no element in the array")
    else:
        print(array[index])

accessElements(arr, 9)