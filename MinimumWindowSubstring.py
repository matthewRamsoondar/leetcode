class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        if n > m:
            return ""
        
        t_chars = {}
        for char in t:
            t_chars[char] = 1 if char not in t_chars else t_chars[char] + 1
        need = len(t_chars)

        l, r, window, have = 0, -1, {}, 0
        for char in t_chars:
            window[char] = 0

        res, rlen = (l, r), m
        while r < m:
            print(f"have: {have}, need: {need}, cur: {s[l:r + 1]}")
            if need == have: # shrink
                if s[l] in t_chars:
                    window[s[l]] -= 1
                    have = have - 1 if window[s[l]] < t_chars[s[l]] else have
                l += 1                
            elif have < need:
                if r == m - 1:
                    break # reached the end of the string and there is no substring possible
                r += 1
                if s[r] in t_chars:
                    window[s[r]] += 1
                    have = have + 1 if window[s[r]] == t_chars[s[r]] else have

            if need == have and r - l + 1 < rlen:
                res, rlen = (l, r), r - l + 1            

        return s[res[0]:res[1] + 1]
    
a = Solution()
print(a.minWindow("ADOBECODEBANC", "ABC"))