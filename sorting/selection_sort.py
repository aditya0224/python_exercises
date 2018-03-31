def selection_sort(input_list):
	for i in range(len(input_list)):
		min_index = i
		for j in range(i+1, len(input_list)):
			if input_list[min_index] > input_list[j]:
				min_index = j
		
		input_list[i], input_list[min_index] = input_list[min_index], input_list[i]
	
	for i in input_list:
		print(i)
		

		
input_list = [9,7,5,9,4,7,2]
selection_sort(input_list)