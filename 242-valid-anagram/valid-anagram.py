class Solution(object):
    def isAnagram(self, s, t):
        s1 = list(s)
        t1 = list(t)
        s1.sort()
        t1.sort()
        if len(s) != len(t):
            return False

        return s1 == t1