class Solution(object):
    def doesAliceWin(self, s):
        vowels=['a','e','i','o','u']
        count=0
        for ch in s:
            if ch in vowels:
                return True
        return False
        