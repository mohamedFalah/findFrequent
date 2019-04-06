import math



#find the frequent item set
#list of the items
items = [['A','B'],['B','C','D'],['A','C','D','E'],['A','D','E'],['A','B','C'],['A','B','C','D'],\
        ['B','C'], ['A','B','C'],['A','B','D'],['B','C','E']]

#list of the avaliable value
valueSet = [] 

#dictionary of frequent
frequent = {}

#find the values 
for item in items:
    for value in item:
        if value not in valueSet:
            valueSet.append(value)
#print the values 
print(valueSet)

#find the frequent of the value individually 
for value in valueSet:
    count = 0
    for item in items:
        if value in item:
            count = count + 1
    frequent[value] = count
 
print('the frequent dictionary')
print(frequent)


#check if the frequent less than or equal ceiling of (number of values/ 2 )
sizeOfList = len(valueSet)
number = sizeOfList / 2.0
thrshold = int(math.ceil(number))
print(thrshold)

#check with dictionary frequent
#empty valueSet
valueSet = []
for key in frequent:
    if frequent[key] != thrshold:
        valueSet.append(key)

print(valueSet)

