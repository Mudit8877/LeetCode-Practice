class Solution(object):
    def vowelStrings(self, words, left, right):
        stack=['a','e','i','o','u']
        count=0
        for i in range(left,right+1):
            if words[i][0] in stack and words[i][-1] in stack:
                count+=1
        return count