// Tests
const tests = [
	"00:00",
	"12:00",
	"01:00",
	"06:01",
	"06:10",
	"06:18",
	"06:30",
	"10:34",
	"00:12",
	"12:09",
	"23:23"
]
const expected = [
	"midnight",
	"noon",
	"one o'clock am",
	"six oh one am",
	"six ten am",
	"six eighteen am",
	"six thirty am",
	"ten thirty four am",
	"twelve twelve am",
	"twelve oh nine pm",
	"eleven twenty three pm"
]
const results = tests.map(timeWord)
let output = []
for (let i = 0; i < expected.length; i++) {
	const success = expected[i] === results[i]
	output.push({
		input: tests[i],
		"expected result": expected[i],
		result: results[i],
		success
	})
}
console.table(output)

// Solution
function timeWord(time) {
	const [hours, minutes] = time.split(":").map(value => parseInt(value))
	if (hours === 0 && minutes === 0) return "midnight"
	if (hours === 12 && minutes === 0) return "noon"
	return `${hoursToWord(hours)} ${minutesToWord(minutes)} ${hours < 12 ? "am" : "pm"}`
}

function hoursToWord(hours) {
	hours %= 12
	// When given a time in the range 0-23, 0 and 12 are 12 midnight and 12 noon, but the hours have
	// been converted to the range 0-11, so both midnight and noon are represented by the hour 0 now.
	if (hours === 0) return "twelve"
	return numberToWord(hours)
}

function minutesToWord(minutes) {
	if (minutes === 0) return "o'clock"
	if (minutes >= 50)
		return `fifty${minutes > 50 ? ` ${numberToWord(minutes - 50)}` : ""}`
	if (minutes >= 40)
		return `forty${minutes > 40 ? ` ${numberToWord(minutes - 40)}` : ""}`
	if (minutes >= 30)
		return `thirty${minutes > 30 ? ` ${numberToWord(minutes - 30)}` : ""}`
	if (minutes >= 20)
		return `twenty${minutes > 20 ? ` ${numberToWord(minutes - 20)}` : ""}`
	if (minutes >= 10) return numberToWord(minutes)
	return `oh ${numberToWord(minutes)}`
}

function numberToWord(number) {
	switch (number) {
		case 1:
			return "one"
		case 2:
			return "two"
		case 3:
			return "three"
		case 4:
			return "four"
		case 5:
			return "five"
		case 6:
			return "six"
		case 7:
			return "seven"
		case 8:
			return "eight"
		case 9:
			return "nine"
		case 10:
			return "ten"
		case 11:
			return "eleven"
		case 12:
			return "twelve"
		case 13:
			return "thirteen"
		case 14:
			return "fourteen"
		case 15:
			return "fifteen"
		case 16:
			return "sixteen"
		case 17:
			return "seventeen"
		case 18:
			return "eighteen"
		case 19:
			return "nineteen"
	}
}
