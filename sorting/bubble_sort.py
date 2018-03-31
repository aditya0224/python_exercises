def bubble_sort(input_list):
	
	sort_complete = False
	for j in range(len(input_list)):
		for i in range(len(input_list) - 1):
			sort_complete = True
			if input_list[i] > input_list[i+1]:
				input_list[i], input_list[i+1] = input_list[i + 1], input_list[i]
				sort_complete = False;
		
		if sort_complete:
				break
				
	for element in input_list:
		print(element)
	
	
input_list = [1,9,5,4,7,9]
bubble_sort(input_list)