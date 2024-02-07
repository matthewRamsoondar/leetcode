class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [-1] * n
        if n == 1:
            return nums[0]

        def dfs(i: int):
            if i >= n:
                return 0

            if memo[i] >= 0:
                return memo[i]

            memo[i] = max(nums[i] + dfs(i + 2), dfs(i + 1))
            return memo[i]

        # find max while including the last house
        for i in range(n - 1, 0, -1):
            dfs(i)

        include_last = memo[1]
        memo = [-1] * n
        n -= 1

        # find max while including the first house
        for i in range(n - 1, -1, -1):
            dfs(i)

        return max(include_last, memo[0])
