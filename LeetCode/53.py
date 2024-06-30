class Solution(object):
    def maxSubArray(self, nums):
        curr_sum = 0
        max_sum = None
        for i in range (0, len(nums)):
            curr_sum += nums[i]
            if curr_sum > max_sum:
                max_sum = curr_sum
            
            if curr_sum < 0:
                curr_sum = 0
        return max_sum
