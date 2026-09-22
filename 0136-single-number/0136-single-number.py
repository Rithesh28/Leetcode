class Solution(object):
    def singleNumber(self, nums):
        duplicate=[]
        for i in nums:
            if i not in duplicate:
                duplicate.append(i)
        for i in duplicate:
            count=0
            for j in nums:
                if i==j:
                    count+=1
            if count==1:
                return i         
        