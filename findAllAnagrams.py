from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m, n = len(s), len(p)
        if n > m:
            return []

        charCount = {}
        for char in p:
            if char not in charCount:
                charCount[char] = 1
            else:
                charCount[char] += 1

        res = []
        curCount = {}
        start, end, i = 0,  n - 1, 0
        while i < m and end < m:
            if s[i] not in charCount:
                # we want to skip ahead and reset the current count
                curCount = {}
                start = i + 1
                end = i + n
                i = start
                continue
            else:
                curCount[s[i]] = 1 if s[i] not in curCount else curCount[s[i]] + 1

            for char in curCount:
                if charCount[char] - curCount[char] < 0:  # we have an invalid char usage
                    curCount[s[start]] -= 1  # just shift the window forward
                    start += 1
                    end += 1

            if i == end:
                res.append(start)
                curCount[s[start]] -= 1
                start += 1
                end += 1

            i += 1

        print(res)
        return res


def main():
    a = Solution()
    # a.findAnagrams("cbaebabacd", "abc")
    # a.findAnagrams("abab", "ab")
    # a.findAnagrams("abaacbabc", "abc")  # 3, 4, 6
    a.findAnagrams("baa", "aa")


main()
