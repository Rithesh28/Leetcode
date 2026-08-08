class Solution(object):
    def validSequence(self, word1, word2):
        n = len(word1)
        m = len(word2)

        last = [0] * m
        j = m - 1

        for i in range(n - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                last[j] = i
                j -= 1

        ans = [0] * m
        j = 0
        usedMatch = False

        for i in range(n):
            if j >= m:
                break

            if word1[i] == word2[j]:
                ans[j] = i
                j += 1

            elif not usedMatch and (j == m - 1 or i + 1 <= last[j + 1]):
                ans[j] = i
                j += 1
                usedMatch = True

        if j != m:
            return []

        return ans