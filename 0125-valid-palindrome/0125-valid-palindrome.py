class Solution(object):
    def isPalindrome(self, s):
        c=[]
        s1=s.lower()
        for i in range(len(s1)):
            if s==" ":
                return True
            if s1[i].isalnum():
                c.append(s1[i])
        reversed=c[::-1]
        if c==reversed:
            return True
        else:
            return False
        