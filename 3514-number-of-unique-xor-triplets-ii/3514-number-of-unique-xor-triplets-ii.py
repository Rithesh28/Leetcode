class Solution:
    def uniqueXorTriplets(self, nums):
        nums = list(set(nums))          # duplicates don't matter

        if len(nums) < 3:
            return len(nums)

        MAX = 2048

        dp = [False] * MAX
        dp[0] = True

        for _ in range(3):
            nxt = [False] * MAX
            for x in range(MAX):
                if dp[x]:
                    for num in nums:
                        nxt[x ^ num] = True
            dp = nxt

        return sum(dp)