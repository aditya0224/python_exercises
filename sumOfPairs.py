""" write a function to get the indices of the array which sum to the given number"""
def sumOfPairs():
	input_numbers = [2,4,9,6,3,2]
	sum = 10
	
	for firstNumberIndex, firstNumber in enumerate(input_numbers):
		for secondNumberIndex, secondNumber in enumerate(input_numbers):
			if secondNumber == sum - firstNumber:
				return [firstNumberIndex, secondNumberIndex]

result = sumOfPairs()
print("The two indices are {} and {} " .format(result[0], result[1]))


def sumOfPairsLinear():
	input_numbers = [2,4,9,6,3,2]
	sum = 10
	input_dictionary = {}

	for index, value in enumerate(input_numbers):
		input_dictionary[value] = index
		
	for index, value in enumerate(input_numbers):
		secondNumber = (sum-value)
		if secondNumber in input_dictionary and index != input_dictionary[secondNumber]:
			 return [index, input_dictionary[secondNumber]]
			
result = sumOfPairsLinear()
print("The two indices are {} and {} " .format(result[0], result[1]))

def sumOfPairsSingleScan():
	input_numbers = [2,4,9,6,3,2]
	sum = 10
	input_dictionary = {}
	
	for index, value in enumerate(input_numbers):
		if (sum-value) in input_dictionary:
			return [input_dictionary[(sum-value)], index]
		else:
			input_dictionary[value] = index

result = sumOfPairsSingleScan()
print("The two indices are {} and {} " .format(result[0], result[1]))