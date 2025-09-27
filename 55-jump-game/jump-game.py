class Solution(object):
    def canJump(self, nums):
        if len(nums) == 1:
            return True
        jumps=0
        endindex=0
        maxindex=0
        for i in range (len(nums)):
            maxindex=max(maxindex,i+nums[i])
            if endindex == i:
                endindex=maxindex
                jumps+=1

        if endindex < len(nums)-1:
            return False
        if endindex >= len(nums)-1:
            return True