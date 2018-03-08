
def lengthOfLongestSubstring(s):
	"""
	:type s: str
	:rtype: int
	"""	
	input_list = list(s)
	if len(s) == 1:
		return 1
	
	max_length = 0
	current_length = 0
	previous_character = None
	longest_sub_string_list = []
	
	for outer_index, character in enumerate(input_list):
		if character in longest_sub_string_list:
			if max_length < current_length:
				max_length = current_length
			temp_string = list(longest_sub_string_list)
			for index,value in enumerate(longest_sub_string_list):                    
				removed_value = temp_string.pop(0)
				current_length = current_length - 1
				if character == removed_value:
					longest_sub_string_list = temp_string
					break

		longest_sub_string_list.append(character)
		current_length = current_length + 1
		
	if current_length > max_length:
		max_length = current_length
	
	return max_length
	
print(lengthOfLongestSubstring('pwaekew'))