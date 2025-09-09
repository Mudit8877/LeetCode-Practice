class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        total=0
        for i in range(0,len(nums)+1):
            total += i
        actual=sum(nums)
        return total-actual
