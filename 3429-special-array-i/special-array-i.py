class Solution(object):
    def isArraySpecial(self, nums):
        for i in range(1,len(nums)):
            if nums[i-1]%2!=0 and nums[i]%2!=0 or nums[i-1]%2==0 and nums[i]%2==0:
                return False
        return True
        