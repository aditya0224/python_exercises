def boxStacks(x,y):
	result = x * (x+1) // 2
	
	index = 1
	while index < y:
		result += x
		x += 1
		index = index + 1

	return result;

result = boxStacks(2,4)
print(result)