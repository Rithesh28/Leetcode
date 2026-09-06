class Solution(object):
    def romanToInt(self, s):
        res,prev=0,0
        roman_dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        for i in s[::-1]:
            if roman_dict[i]>=prev:
                res+=roman_dict[i]
            else:
                res-=roman_dict[i]
            prev=roman_dict[i]
        return res
        