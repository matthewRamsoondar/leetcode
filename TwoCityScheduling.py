from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # compute the differences as cost[1] - cost[0]
        # the more positve it is means it is more expensive
        # to go to city B
        # The more negative it is is the more expensive it is to go to city A
        n = len(costs)
        diffs = []

        for i, cost in enumerate(costs):
            diffs.append((cost[1] - cost[0], i))

        diffs.sort(key=lambda x: x[0])

        b_cost = sum([costs[e[1]][1] for e in diffs[: n // 2]])
        a_cost = sum(costs[e[1]][0] for e in diffs[n // 2 :])

        return b_cost + a_cost
