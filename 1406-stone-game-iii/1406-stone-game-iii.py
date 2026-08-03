class Solution(object):
    def stoneGameIII(self,stoneValue):
        n = len(stoneValue)
        dp = [0] * (n + 1)  

        for i in range(n - 1, -1, -1):
            best = float('-inf')
            take_sum = 0
            for take in range(1, 4):
                if i + take - 1 >= n:
                    break
                take_sum += stoneValue[i + take - 1]
                best = max(best, take_sum - dp[i + take])
            dp[i] = best

        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"
            