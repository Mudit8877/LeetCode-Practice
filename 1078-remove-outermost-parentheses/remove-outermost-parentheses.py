class Solution(object):
    def removeOuterParentheses(self, s):
        counter=0
        ans=[]
        for i in range(len(s)):
            if s[i]==')':
                counter-=1
            if counter!=0:
                ans.append(s[i])
            if s[i]=='(':
                counter+=1

        return ''.join(ans)
        