def pairSum(lst,target):
    result=[]
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i]+lst[j]==target:
                result.append(f"{lst[i]}+{lst[j]}")
        
    return result
    


mylist=[1,2,3,4,2,5,2,5,2,3,6,2,4]
print(pairSum(mylist,7))

