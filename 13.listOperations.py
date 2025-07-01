list=[1,2,3,44]
print(list)
for i in range(len(list)):
    list[i]=list[i] +1
    print(list[i])

#try to traverse empty list
empty=[]
for i in empty:
    print("empty list") #--> So it does not show error but also it doesn't print anything


#insert and update the list
Mylist=[2,3,4,2,4,5,3]
Mylist.insert(4,34) #--> we can add elements to the any index with insert method
print(Mylist)
Mylist.append(34) #--> append method is used to add element at the end of the list
print(Mylist)
extendedList=[33,33,44,5,55,99]
Mylist.extend(extendedList)
print(Mylist)

#update list through slice method
Mylist1=['a','b','c','d','e']
Mylist1[0:3]=['x','y','z']
print(Mylist1)

#deletion operations in the list

Mylist1.pop(2)
print(Mylist1)
del Mylist1[0:2]
print(Mylist1)
Mylist1.remove('e')
print(Mylist1)

#searching through list

searchList=[1,2,3,44,55,34,5,2,4,23]
target=55
if target in searchList:
    print(f"the {target} is present in the list")
else:
     print(f"the {target} is not present in the list")