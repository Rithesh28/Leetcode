class Solution(object):
    def countAsterisks(self, s):
        num=0
        a="*"
        b="|"
        bars=0
        for i in range(0,len(s)):
            if s[i] in b:
                bars+=1
            if bars%2==0 and s[i] in a:
                num+=1
        return num
        