def merge_sort(input_list):
	length_of_the_list = len(input_list)
	
	if length_of_the_list == 1:
		return input_list;
	
	left_list = input_list[0 : length_of_the_list // 2]
	right_list = input_list[ length_of_the_list // 2 : length_of_the_list]
	
	o1 = merge_sort(left_list)
	o2 = merge_sort(right_list)
		
	return merge(o1, o2)
	
def merge(left_list, right_list):
	result_list = []
	index = 0
	output_list = []
	lenght_1 = len(left_list)
	length_2 = len(right_list)
	
	i = 0
	j = 0
	while i < lenght_1 and j < length_2:
		if left_list[i] < right_list[j]:
			output_list.append(left_list[i])
			i = i + 1
		else:
			output_list.append(right_list[j])
			j = j + 1
			
	for index in range(i, len(left_list)):
		output_list.append(left_list[index])
		
	for index in range(j, len(right_list)):
		output_list.append(right_list[index])
		
	return output_list
	
input_list = [9,7,6,1,8,3,11,14]
print(merge_sort(input_list))