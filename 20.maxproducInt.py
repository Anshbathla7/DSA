mylist=[1,25,6,2,5,6,2]
def max_product(arr):
    max1,max2=0,0
    for element in arr:
        if element>max1:
            max2=max1
            max1=element
        elif element>max2:
            max2=element

    return max1*max2
    
print(max_product(mylist))