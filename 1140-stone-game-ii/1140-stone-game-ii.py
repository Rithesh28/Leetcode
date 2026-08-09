class Solution(object):
    def stoneGameII(self, piles):
        n = len(piles)

        # suffix[i] = sum of piles[i:]
        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        memo = {}

        def dp(i, M):
            if i >= n:
                return 0

            if (i, M) in memo:
                return memo[(i, M)]

            # Can take all remaining piles
            if i + 2 * M >= n:
                memo[(i, M)] = suffix[i]
                return suffix[i]

            best = 0

            # Try taking X piles
            for X in range(1, 2 * M + 1):
                # Current player gets all remaining stones
                # minus what the opponent can get
                opponent = dp(i + X, max(M, X))

                current = suffix[i] - opponent

                best = max(best, current)

            memo[(i, M)] = best
            return best

        return dp(0, 1)