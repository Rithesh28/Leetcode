class Solution(object):
    def lengthOfLastWord(self, s):
        space=" "
        c=0
        for i in range(len(s)-1,-1,-1):
            if space in s[i] and c==0:
                continue
            if space in s[i] and c!=0:
                return c
            if space not in s[i]:
                c+=1
        return c

            
        