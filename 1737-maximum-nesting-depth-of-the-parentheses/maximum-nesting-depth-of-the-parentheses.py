class Solution(object):
    def maxDepth(self, s):
        count=0
        max_c=0
        for ch in s:
            if ch =='(':
                count+=1
                max_c=max(max_c,count)
            if ch == ')':
                count-=1
        return max_c

        

        