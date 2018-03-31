def merge_sort(input_list):
	if len(input_list) == 1:
		return;
	left_list = input_list[0, len(input_list / 2]
	right_list = input_list[len(input_list) / 2 + 1, len(input_list - 1)]
	merge_sort(left_list)
	merge_sort(right_list)
	
	merge(left_list, right_list)

def merge(left_list, right_list):
	result_list = []
	
	index = 0
	while(len(left_list) > 0 && len(right_list) > 0):
		if(left_list)