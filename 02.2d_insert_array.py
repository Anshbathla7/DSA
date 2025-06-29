import array
arr=array.array('i',[1,2,3,4,5,6])
arr.insert(2, 10)  # Insert 10 at index 2
print(arr)  # Output: [ 1  2 10  3  4  5  6]