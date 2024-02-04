from collections import deque
import math


# 0 <= poured <= 10^9
# 0 <= query_glass <= query_row < 100
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        queue = deque()
        queue.append((0, 0, poured))

        while queue:
            x, y, amt = queue.popleft()
            print(x, y, amt)

            if y == query_row - query_glass and x == query_glass:
                return min(amt, 1)

            # if amt > 1:
            # only append left nodes to the queue if this is a left node
            if x == 0:
                queue.append((x, y + 1, max(0, (amt - 1) / 2)))
            else:
                # add to the previously added right node
                _x, _y, _amt = queue.pop()
                queue.append((_x, _y, _amt + max(0, (amt - 1) / 2)))

            queue.append((x + 1, y, max(0, (amt - 1) / 2)))

        return 0


a = Solution()
print(a.champagneTower(25, 6, 1))
