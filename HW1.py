import math



class FindFrequent: 
   

    #find the values 
    def getTheItemList(self,items):
        valueSet = []
        for item in items:
            for value in item:
                if value not in valueSet:
                    valueSet.append(value)
        return valueSet

    #find the frequent of the value individual   
    def findTheFrequentOfItems(self, valueSet,items):
        frequent = {}
        for value in valueSet:
            count = 0
            for item in items:
                if value in item:
                    count = count + 1
            frequent[value] = count
        return frequent

    #find the frequent of the value more than 1  
    def findTheFrequentOfJoinItems(self, valueSet,items):
            frequent = {}
            
            there = []

            for value in valueSet: 
                count = 0
                hashableValue = ""
                for item in items: 
                    hashableValue = ""
                    valueExists = []
                    for v in value:
                        if v in item:
                            valueExists.append("true")
                        else:
                            valueExists.append("false")
                        hashableValue = hashableValue + v

                    if "false" not in valueExists:
                        count = count + 1
                frequent[hashableValue] = count

              
            return frequent


    #get the thrshold
    def findTheThrshold(self, sizeOfList):
        number = sizeOfList / 2.0
        thrshold = int(math.ceil(number))
        return thrshold


    #check with dictionary frequent
    def deleteNonFrequentItems(self, frequent, thrshold):
        #empty valueSet
        valueSet = []
        for key in frequent:
            if frequent[key] > thrshold:
                valueSet.append(key)
        return valueSet

    # a b c d
    #ab ac ad  bc bd cd 
    #get the join of frequent
    def joinItems(self, valueSet):
        newValueSet = []
        for value in valueSet:
            for value2 in valueSet:
                if(value != value2):
                    newValue = [value,value2]
                    newValueSet.append(newValue)
        return newValueSet

    #filter the join set to remove similar sets joins
    def clearSimilarItems(self, valueSet):
        for values in valueSet:
            for values2 in valueSet:
                if values != values2:
                    if set(values) == set(values2):
                     valueSet.remove(values2)

        return valueSet

    


items = [['A','B'],['B','C','D'],['A','C','D','E'],['A','D','E'],['A','B','C'],['A','B','C','D'],\
            ['B','C'], ['A','B','C'],['A','B','D'],['B','C','E']]

#frequent dictionary
frequent = {}
frequentList = []
findfrequent =  FindFrequent()

#stop condition
getLengthOfValue = 0

#print the minimum support 
print("assuming that the minimum support is 4 so 3 and less will be dicarded")

#get the items 
valueSet = findfrequent.getTheItemList(items)
#find the frequent individual 
frequent = findfrequent.findTheFrequentOfItems(valueSet,items)

#remove the less than thrshold frequent 
thrshold = findfrequent.findTheThrshold(len(valueSet))
valueSet = findfrequent.deleteNonFrequentItems(frequent, thrshold)
OriginalItems = valueSet
frequentList.append(valueSet)
print(frequentList)
print(valueSet)
i = 0
while i <=  len(OriginalItems):
    print("value set size")
    print(len(OriginalItems))
    print(valueSet)
    print(i)
    print(len(valueSet))
    #join the two of the freqeunt togather
    valueSet = findfrequent.joinItems(valueSet)
    valueSet = findfrequent.clearSimilarItems(valueSet)

    #find the frequent of the items 
    frequent = findfrequent.findTheFrequentOfJoinItems(valueSet,items)
    print(frequent)
    

    if(len(freqeunt[]) == len(OriginalItems)):
        getLengthOfValue = len(valueSet[0])
    print(getLengthOfValue)

    valueSet = findfrequent.deleteNonFrequentItems(frequent, thrshold)
    frequentList.append(valueSet)
    print('list of frequence items')
    print(frequentList)

    if(getLengthOfValue == len(OriginalItems)):
       break
    i = i + 1
    if len(valueSet) > 20:
        break





