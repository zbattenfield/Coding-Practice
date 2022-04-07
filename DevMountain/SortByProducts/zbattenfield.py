def sortByProduct(startArray):
    productArray = []

    for x in range(len(startArray)):
        productArray.append(startArray[x]*(x+1))


    sortedArray = [x for _,x in sorted(zip(productArray, startArray))] #list comprehension to sort zipped object by the values of the product array and  only extract values  from original array
    return sortedArray


testArray1 = [1,2,3,4,5,6]
testArray2 = [23,2,3,4,5]
testArray3 = [1,99,3]

arrayGroup = [testArray1, testArray2, testArray3]

for array in arrayGroup:
    print(sortByProduct(array))

