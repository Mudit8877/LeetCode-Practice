class Solution(object):
    def doesAliceWin(self, s):
        vowels=['a','e','i','o','u']
        count=0
        for ch in s:
            if ch in vowels:
                count+=1
        if count==0:
            return False
        if count%2!=0:
            return True
        if count%2==0:
            return True
        # return count
        