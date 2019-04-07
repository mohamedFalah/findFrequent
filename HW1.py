import math


class GetFrequentList: 
    items = [['A','B'],['B','C','D'],['A','C','D','E'],['A','D','E'],['A','B','C'],['A','B','C','D'],\
            ['B','C'], ['A','B','C'],['A','B','D'],['B','C','E']]



class FindFrequent: 
    

    #list of the avaliable value
    valueSet = [] 
    valueSetJoin = []

    #dictionary of frequent
    frequent = {}

    #thrshold
    thrshold = 0

    #find the values 
    def getTheItemList():
        for item in items:
            for value in item:
                if value not in valueSet:
                    valueSet.append(value)


    #find the frequent of the value  
    def findTheFrequentOfItems():
        for value in valueSet:
            count = 0
            for item in items:
                if value in item:
                    count = count + 1
            frequent[value] = count


    #get the thrshold
    def findTheThrshold(valueSet):
        sizeOfList = len(valueSet)
        number = sizeOfList / 2.0
        thrshold = int(math.ceil(number))
        return thrshold


    #check with dictionary frequent
    def deleteNonFrequentItems():
        #empty valueSet
        valueSet = []
        for key in frequent:
            if frequent[key] != thrshold:
                valueSet.append(key)

        print(valueSet)

    # a b c d
    #ab ac ad  bc bd cd 
    #get the join of frequent
    def joinItems():
        newValue = []
        for value in valueSet:
            for value2 in valueSet:
                if(value != value2):
                    newValue = [value, value2]
                    valueSetJoin.append(newValue)


    #filter the join set to remove similar sets joins
    def clearSimilarItems():
        for values in valueSetJoin:
            for values2 in valueSetJoin:
                if values != values2:
                if set(values) == set(values2):
                    valueSetJoin.remove(values2)

 

    


