from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, n = [], len(candidates)

        def dfs(i: int, cur: List[int], curSum: int):
            print(i, cur, curSum)
            if curSum == target:
                cur_sorted = sorted(cur)
                for e in res:
                    if e == cur_sorted:
                        return

                res.append(cur_sorted)
            elif curSum > target:
                return

            # compute the next combination
            for j in range(i + 1, n):
                cur.append(candidates[j])
                dfs(j, cur, curSum + candidates[j])
                cur.pop()

        dfs(0, [], 0)

        return res


a = Solution()
print(a.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
# print(a.combinationSum2([10, 1, 2, 2, 6, 1, 5], 5))
