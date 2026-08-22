class Solution {
    public boolean checkDivisibility(int n) {
        int temp=n;
        int sum=0;
        int product=1;
        while(n>0){
            int digit=n%10;
            sum+=digit;
            product*=digit;
            n=n/10;
        }
        int divisible=sum+product;
        return temp % divisible==0;
    }
}