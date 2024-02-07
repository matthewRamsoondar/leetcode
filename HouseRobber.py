from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # we want to do a dfs of the choices at i
        # and then store the maximum outcome
        n = len(nums)
        memo = [-1] * n

        def dfs(i: int):
            if i >= n:
                return 0

            if memo[i] >= 0:
                return memo[i]

            memo[i] = max(nums[i] + dfs(i + 2), dfs(i + 1))
            return memo[i]

        for i in range(n - 1, -1, -1):
            # call dfs in reverse
            dfs(i)

        return memo[0]


a = Solution()
print(a.rob([1, 2, 3, 1]))
print(a.rob([2, 9, 13, 4, 3, 10]))
