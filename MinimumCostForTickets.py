from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        dp = {}

        def dfs(i):
            # return the minimum cost to get to day 0
            if i < 0:
                return 0
            if i in dp:
                return dp[i]

            dp[i] = float("inf")

            for (
                d,
                c,
            ) in zip([1, 7, 30], costs):
                j = i
                # we want to find the next day in the array that is less than days[i] - d
                while j >= 0 and days[j] > days[i] - d:
                    j -= 1

                # now we want to compute the dfs for this index
                dp[i] = min(dp[i], c + dfs(j))
                # this is done for each day so by the end of this loop
                # dp[i] will contain the minimum cost to go to day[0] from day[i]
                # then we return it

            return dp[i]

        dfs(n - 1)
        return dp[n - 1]


a = Solution()

print(a.mincostTickets([1, 4, 6, 7, 8, 20], [2, 7, 15]))
print(a.mincostTickets([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 7, 15]))
