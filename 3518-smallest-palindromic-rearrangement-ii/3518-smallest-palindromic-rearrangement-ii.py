import math
from collections import Counter
class Solution(object):
    def smallestPalindrome(self, s, k):
        CAP = 10**6
        cnt = Counter(s)
        center = ''
        half_counts = {}
        for c, v in cnt.items():
            if v % 2 == 1:
                center = c
            if v // 2 > 0:
                half_counts[c] = v // 2

        letters = sorted(half_counts.keys())
        half_len = sum(half_counts.values())

        def comb(n, r):
            if r < 0 or r > n:
                return 0
            r = min(r, n - r)
            result = 1
            for i in range(r):
                result = result * (n - i) // (i + 1)
            return result

        def arrangements(counts_list, remaining_total):
            result = 1
            remaining = remaining_total
            for c in counts_list:
                if c == 0:
                    continue
                if result > CAP:
                    return CAP + 1
                result *= comb(remaining, c)
                remaining -= c
            return min(result, CAP + 1)

        total = arrangements([half_counts[c] for c in letters], half_len)
        if total < k:
            return ""

        half_result = []
        counts = dict(half_counts)
        remaining_len = half_len

        for _ in range(half_len):
            for c in letters:
                if counts.get(c, 0) == 0:
                    continue
                counts[c] -= 1
                remaining_len -= 1
                cnt_list = [counts[x] for x in letters]
                arr = arrangements(cnt_list, remaining_len)
                if arr >= k:
                    half_result.append(c)
                    break
                else:
                    k -= arr
                    counts[c] += 1
                    remaining_len += 1

        half_str = ''.join(half_result)
        return half_str + center + half_str[::-1]
        