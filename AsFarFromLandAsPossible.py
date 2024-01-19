from typing import List
from collections import deque


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        res = [[-1] * n for i in range(n)]

        def bfs(x: int, y: int):
            queue, seen = deque(), set()
            queue.append((x, y))
            while len(queue) > 0:
                cur = queue.pop()
                seen.add((cur[0], cur[1]))
                dist = abs(x - cur[0]) + abs(y - cur[1])

                if res[cur[1]][cur[0]] == -1 or dist < res[cur[1]][cur[0]]:
                    res[cur[1]][cur[0]] = dist  # append the distance to this node

                dirs = [
                    (cur[0], cur[1] - 1),
                    (cur[0], cur[1] + 1),
                    (cur[0] - 1, cur[1]),
                    (cur[0] + 1, cur[1]),
                ]

                for node in dirs:
                    if (
                        0 <= node[0] < n
                        and 0 <= node[1] < n
                        and (node[0], node[1]) not in seen
                        and grid[node[1]][node[0]] == 0
                    ):
                        queue.append((node[0], node[1]))  # add this to our stack

        for y in range(n):
            for x in range(n):
                if grid[y][x] == 1:
                    bfs(x, y)

        curMax = -1
        for y in range(n):
            for x in range(n):
                if grid[y][x] == 0:
                    curMax = max(curMax, res[y][x])

        return curMax


a = Solution()
print(a.maxDistance([[1, 0, 0], [0, 0, 0], [0, 0, 0]]))
