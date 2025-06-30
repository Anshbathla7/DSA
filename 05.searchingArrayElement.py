import array
arr=array.array('i', [1, 4, 4, 5, 3, 5, 6])
element=int(input("Enter the element to search: "))
def searchElement(array,element):
    for i in range(len(array)):
       if array[i] == element:
            print(f"Element {element} found at index {i}")
    if array[i]> element:
        print(f"Element {element} not found in the array")
    else:
         print(f"not found")

searchElement(arr, element)