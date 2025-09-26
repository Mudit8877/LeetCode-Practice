class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        final=[]
        i=0
        j=0
        while i < len(word1) and j < len(word2):
            final.append(word1[i])
            final.append(word2[j])
            i+=1
            j+=1
        final.append(word1[i:])
        final.append(word2[j:])
        return "".join(final)
        