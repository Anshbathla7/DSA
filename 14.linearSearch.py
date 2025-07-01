Mylist=[2,3,4,2,4,5,3,9]
target=9

def linearSearch(list,targetValue):
    for i,value in enumerate(list): # --> here i tracks the element's index and value tracks the element
        if value==targetValue:
            return i 
    else:
        return -1
    
print(linearSearch(Mylist,target))
    