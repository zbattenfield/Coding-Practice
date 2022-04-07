#from https://ed.devmountain.com/materials/f20/exercises/chal-sort-product/

# Sort by Product

# Difficulty: Medium
# Concepts: Loops, Math

# Your task is to sort an array of integer numbers by the product (multiplication) of the value and the index.
# For sorting the index starts at 1, NOT at 0!
# The sorting has to be ascending.
# The array will never be null and will always contain numbers.

# Example:
# INPUT: 23, 2, 3, 4, 5
# Product of value and index:
# 23 => 23 * 1 = 23 -> Output-Pos 4
# 2 => 2 * 2 = 4 -> Output-Pos 1
# 3 => 3 * 3 = 9 -> Output-Pos 2
# 4 => 4 * 4 = 16 -> Output-Pos 3
# 5 => 5 * 5 = 25 -> Output-Pos 5
# OUTPUT: 2, 3, 4, 23, 5

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

