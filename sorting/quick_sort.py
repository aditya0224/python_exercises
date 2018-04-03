def quick_sort(input_list, low, high):
	
	if low < high:
		pi = paritition(input_list, low, high)
		
		quick_sort(input_list, low, pi-1)
		quick_sort(input_list, pi + 1, high)

		
def paritition(input_list, low, high):
	i = low -1
	pivot = input_list[high]
	
	for j in range(low, high):
		if input_list[j] < pivot:
			i = i+1
			input_list[i], input_list[j] = input_list[j], input_list[i]
	
	input_list[i+1], input_list[high] = input_list[high], input_list[i+1]
	
	return i+1
	

input_list = [1,2,7,4,9,2,8]
quick_sort(input_list, 0, 6)
print(input_list)