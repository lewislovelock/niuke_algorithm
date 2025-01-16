from typing import List

class Solution:
    def findLengthOfLCIS1(self, nums: List[int]) -> int:
        current_length = 1
        max_length = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                current_length += 1
                max_length = max(max_length, current_length)
            else:
                current_length = 1

        return max_length
    
    def findLengthOfLCIS2(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        max_length = 0
        start = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                start = i
            max_length = max(max_length, i - start + 1)
        
        return max_length
