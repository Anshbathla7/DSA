import array
#create and traverse array
arr=array.array('i',[1,3,2,4,5,3])
for i in arr:
    print(f"{i}")

# access array
print("step2")
print(f'{arr[0]}')

#append any value in an array
print("step3")
arr.append(9)
print(arr)

#insert a value in an array
print("step4")
arr.insert(4,11) # --> here first value is an index and second is the element
print(arr)

#extend an array
print("step5")
arr1=array.array('i',[12,13,14,15])
arr.extend(arr1)
print(arr)

#adding elements into an array from a list using fromlist() method
print("step6")
list=[20,21,22,23]
arr.fromlist(list)
print(arr)

#remove an element using remove() method
print("step7")
arr.remove(21)
print(arr)

#remove last element using pop() method
print("step8")
arr.pop()
print(arr)

#fetch any value using index() method
print("step9")
print(arr.index(20))

#reverse an array using reverse() method
print("step10")
arr.reverse()
print(arr)

#get array buffer information using buffer_info() method
print("step11")
print(arr.buffer_info())

#Check the number of occurence of elements in an array using count() method
print("step12")
print(arr.count(11))