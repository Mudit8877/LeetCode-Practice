class Solution(object):
    def reverseWords(self, s):
        s=s.strip()
        words=s.split()
        w=words[-1::-1]
        return ' '.join(w)
        