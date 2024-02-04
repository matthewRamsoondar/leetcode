from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n, seen = len(nums), [0 for _ in range(len(nums))]
        res = []

        def dfs(cur: int, num_jumps: int, seen: List[int]):
            if cur == n - 1:
                res.append(num_jumps)

            seen[cur] = 1
            for i in range(nums[cur]):
                new_index = cur + i
                if new_index < n and not seen[new_index]:
                    dfs(new_index, num_jumps + 1, seen)

        dfs(0, 0, seen)
        return min(res)


a = Solution()
print(a.jump([2, 3, 1, 1, 4]))  # 2
print(a.jump([0]))  #
print(a.jump([1, 2]))  # 1
print(a.jump([2, 1]))  # 1
