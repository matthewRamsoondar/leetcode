class Solution:
    def countSubstrings(self, s: str) -> int:
        # sliding window at each length and then check the memo
        n = len(s)
        memo = set()
        res = 0

        def isPalindrome(start: int, stop: int):
            # return wether or not s[start:stop] is a palindrome
            if start == stop or abs(start - stop) == 1:
                return True

            return (start, stop) in memo

        for i in range(1, n + 1):
            # i is the length of the window
            l, r = 0, i

            while r <= n:  # r must touch the end of the string
                print(s[l:r], f"{l + 1}, {r - 1}")
                if s[l] == s[r - 1] and isPalindrome(l + 1, r - 1):
                    print(f"     ({l}, {r})")
                    memo.add((l, r))
                    res += 1

                l += 1
                r += 1

        return res


a = Solution()
print(a.countSubstrings("aaba"))
