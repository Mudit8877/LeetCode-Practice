class Solution(object):
    def findClosestNumber(self, nums):
        close=nums[0]
        for i in nums:
            if abs(i) < abs(close):
                close=i
        if close < 0  and abs(close) in nums:
            return abs(close)
        else:
            return close

        