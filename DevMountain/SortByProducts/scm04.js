function sortByProduct(array) {
	return array
		.map((value, index) => ({ index, value })) // Map each value in the array to a pair containing both the value and the index
		.sort((a, b) => (a.index + 1) * a.value - (b.index + 1) * b.value) // Sort by the product of the value and the index
		.map(({ value }) => value) // Extract the value back out of the pair.
}

const tests = [
	[1, 2, 3, 4, 5, 6],
	[23, 2, 3, 4, 5],
	[1, 99, 3]
]
const expected = [
	[1, 2, 3, 4, 5, 6],
	[2, 3, 4, 23, 5],
	[1, 3, 99]
]
const results = tests.map(sortByProduct)

for (let i = 0; i < tests.length; i++) {
	const success = expected[i]
		.map((value, index) => value === results[i][index]) // Check if each value in the result is the expected value.
		.every(a => a) // Verify that every value in the resulting array is true (indicating that all values matched their expected value).
	console.log(
		`input: [${tests[i]}], expected: [${expected[i]}], result: [${results[i]}], success: ${success}`
	)
}
