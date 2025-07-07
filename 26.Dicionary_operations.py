# There are two ways to create dictionary
#1st way using dict constructor

Mydict=dict(apple='fruit',ladyfinger='vegetable',almone='dry fruit')
print(Mydict)
# 2nd is using curly braces
dict1={'apple':'fruit',
       'ladyfinger':'vegetable',
       'almoned':'dryfruit'}
print(dict1)

#3rd is using tuples
dict3=[('apple','fruit'),('ladyfinger','vegetable'),('almoned','dryfruit')]
convert_to_dict=dict(dict3)
print(convert_to_dict) 

#traverse through dictionary
def traverseDictionary(dictionary):
    for key in Mydict:
        print(key,Mydict[key])

traverseDictionary(Mydict)
#searchig element in the dictionary

def SearchElement(dictionary,value):
    for key in Mydict:
        if Mydict[key]==value:
            return key,value
    return 'this value does not existed'

print(SearchElement(dict1,'fruit'))

#Deleting the elements in the dictionart
del_icon={'name':'ansh','class':'12th','rollno':'1','address':'tejvihar,meerut'}
del del_icon['address']
print(del_icon)
secondMethod=del_icon.pop('rollno') # we can delete any index from pop method to pass a key in it.
print(del_icon)
ThirdMethod=del_icon.popitem() #popitem method takes no argument and it removes the last item for dictionary.
print(del_icon)
