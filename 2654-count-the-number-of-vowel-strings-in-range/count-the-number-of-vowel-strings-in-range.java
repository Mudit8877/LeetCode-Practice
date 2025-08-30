class Solution {
    public int vowelStrings(String[] words, int left, int right) {
        int count=0;
        for(int i=left;i<=right;i++){
            char s = words[i].charAt(0);
            char s1=words[i].charAt(words[i].length()-1);
            if(s == 'a' || s == 'e' || s == 'i'|| s == 'o' || s == 'u'){
                if(s1 == 'a' || s1 == 'e' || s1 == 'i'|| s1 == 'o' || s1 == 'u'){
                    count++;
                }
            }
        }
        return count;   
    }
}