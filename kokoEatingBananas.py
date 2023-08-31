class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        m = max(piles)
        l, r = 1, m

        def computeTime(k: int):
            total = 0
            for p in piles:
                total += math.ceil(p / k)
            return total

        k = m
        while (l <= r):
            med = (l + r) // 2
            time = computeTime(med)
            if time > h:
                l = med + 1
            else:
                k = min(k, med)
                r = med - 1

        return k