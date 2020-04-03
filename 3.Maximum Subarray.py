'''
Also Known as kadanes algorithm
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        length = len(nums)
        current_sum = 0
        
        for num in nums:
            current_sum += num
            if (num > current_sum):
                current_sum = num       
            if (current_sum > max_sum):
                max_sum = current_sum
                
        return max_sum
            