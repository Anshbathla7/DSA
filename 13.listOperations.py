list=[1,2,3,44]
print(list)
for i in range(len(list)):
    list[i]=list[i] +1
    print(list[i])

#try to traverse empty list
empty=[]
for i in empty:
    print("empty list") #--> So it does not show error but also it doesn't print anything