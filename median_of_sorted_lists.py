class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        result = 0
        final_list = []
        total_length = len(nums1) + len(nums2)
        
        for index1,value1 in enumerate(nums1):
            for index2, value2 in enumerate(nums2):
                if(value1 < value2):
                    final_list.append(value1)
                else:
                    final_list.append(value2)
         
        if(total_length % 2 == 0):
            result = float((final_list.pop(total_length//2) + final_list.pop(total_length//2 - 1)) / 2)
        else: 
            result = float(final_list.pop(total_length//2))

        return result