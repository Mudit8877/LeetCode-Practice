class Solution(object):
    def isLongPressedName(self, name, typed):
        i=0
        j=0
        if len(typed)<len(name):
            return False
        while j<len(typed):
            if i < len(name) and name[i] == typed[j]:
                i+=1
            elif j==0 or typed[j]!=typed[j-1]:
                return False

            j+=1
        if i == len(name):
            return True
        else:
            return False
        