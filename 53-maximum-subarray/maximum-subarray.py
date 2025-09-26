class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        count=0
        max_ele=float("-inf")
        for i in range (len(nums)):
            count+=nums[i]
            max_ele=max(count,max_ele)
            if count < 0:
                count=0
                
        return max_ele