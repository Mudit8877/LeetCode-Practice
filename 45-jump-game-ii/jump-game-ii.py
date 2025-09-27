class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps=0
        endindex=0
        maxindex=0
        if len(nums) == 1:
            return 0
        for i in range(len(nums)):
            maxindex=max(maxindex,i+nums[i])
            if endindex == i:
                endindex=maxindex
                jumps+=1
            if endindex >= len(nums)-1:
                break
        return jumps 