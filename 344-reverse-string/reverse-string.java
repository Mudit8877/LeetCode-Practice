class Solution {
    public void reverseString(char[] s) {
        StringBuilder rev= new StringBuilder(new String(s)).reverse(); 
        for(int i=0 ; i<s.length;i++){
            s[i]=rev.charAt(i);
        }
    }
}