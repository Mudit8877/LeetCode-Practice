class Solution(object):
    def sortVowels(self, s):
        vowels = set("aeiouAEIOU") 
        ve = [ch for ch in s if ch in vowels]  
        ve.sort()  

        result = []
        vowel_idx = 0
        for char in s:
            if char in vowels:     
                result.append(ve[vowel_idx])
                vowel_idx += 1
            else:              
                result.append(char)

        return "".join(result)
