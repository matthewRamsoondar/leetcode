class Solution:
    def numDecodings(self, s: str) -> int:
        n, memo = len(s), [-1] * len(s)

        def dfs(i: int):
            # check if this is allowed
            if i >= n:
                return 1

            if memo[i] >= 0:
                return memo[i]

            # now compute the number of way to decode this string
            if s[i] == "1":
                memo[i] = dfs(i + 2) + dfs(i + 1)
            elif s[i] == "2" and i + 1 < n and int(s[i + 1]) <= 6:
                memo[i] = dfs(i + 2) + dfs(i + 1)
            elif 2 <= int(s[i]) <= 9:
                memo[i] = dfs(i + 1)

            return memo[i]

        for i in range(n - 1, -1, -1):
            if dfs(i) == -1:
                return 0

        return memo[0]


a = Solution()
print(a.numDecodings("06"))
