from functools import reduce

# One-liner
def sortByProduct(arr):
    return list(map(lambda tuple: tuple[1], sorted([(ind, x) for (ind, x) in enumerate(arr)], key=lambda tuple: (tuple[0] + 1) * tuple[1])))

# How I would actually write this code in a production application to make it more readable/maintainable.
def sortByProduct2(arr):
	tuples = [tuple for tuple in enumerate(arr)] # enumerate(arr) returns a tuple of (index, value) for each value in the list
	sorted_tuples = sorted(tuples, key=lambda tuple: (tuple[0] + 1) * tuple[1])
	return list(map(lambda tuple: tuple[1], sorted_tuples))

# An alternative to sortByProduct2 where the tuples are sorted in place instead of creating a new list.
# I would probably choose this implementation over the others because it saves on storage used by the function.
def sortByProduct3(arr):
	tuples = [tuple for tuple in enumerate(arr)]
	tuples.sort(key=lambda tuple: (tuple[0] + 1) * tuple[1])
	return list(map(lambda tuple: tuple[1], tuples))

tests = [
    [1, 2, 3, 4, 5, 6],
    [23, 2, 3, 4, 5],
    [1, 99, 3]
]
expected = [
    [1, 2, 3, 4, 5, 6],
    [2, 3, 4, 23, 5],
    [1, 3, 99]
]
results = [sortByProduct(arr) for arr in tests]
results2 = [sortByProduct2(arr) for arr in tests]
results3 = [sortByProduct3(arr) for arr in tests]

for i in range(len(tests)):
    success = reduce(lambda a, b: a and b, [expected[i][j] == results[i][j] for j in range(len(expected[i]))], True)
    success2 = reduce(lambda a, b: a and b, [expected[i][j] == results2[i][j] for j in range(len(expected[i]))], True)
    success3 = reduce(lambda a, b: a and b, [expected[i][j] == results3[i][j] for j in range(len(expected[i]))], True)
    print("input:", str(tests[i]) + ",", "expected:", str(expected[i]) + ",", "result:", str(results[i]) + ",", "success:", str(success) + ",", "success2: ", str(success2) + ",", "success3:", success3)