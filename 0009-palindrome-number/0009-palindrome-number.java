class Solution {
    public boolean isPalindrome(int x) {
        int num=x;
        int rev=0;
        while(num>0){
            int n=num%10;
            rev=rev*10+n;
            num=num/10;
        }
        if(x==rev){
            return true;
        }
        else{
            return false;
        }
    }
}