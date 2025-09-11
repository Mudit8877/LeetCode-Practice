class Solution(object):
    def isAnagram(self, s, t):
        s1=list(s)
        t1=list(t)
        s1.sort()
        t1.sort()
        count=0
        n=len(s)
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            if s1[i] == t1[i]:
                count+=1
            if count == n:
                return True
        return False
        