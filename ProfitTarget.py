from typing import List


def stockPairs(stocksProfit: List[int], target: int):
    stocksProfit.sort()
    n = len(stocksProfit)
    l, r = 0, n - 1
    res = 0

    while l < r:
        cur_sum = stocksProfit[l] + stocksProfit[r]
        print(cur_sum, l, r)
        if cur_sum <= target:
            if cur_sum == target:
                res += 1

            prev = stocksProfit[l]
            while stocksProfit[l] == prev:
                l += 1
        else:
            prev = stocksProfit[r]
            while stocksProfit[r] == prev:
                r -= 1

    return res


print(stockPairs([5, 7, 9, 13, 11, 6, 6, 3, 3], 12))
