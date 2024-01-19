from typing import List
import heapq


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        # first sort the events in terms of start date
        events.sort(key=lambda x: x[0])
        n, d, i, res = len(events), 1, 0, 0

        min_heap = []

        while d <= events[n - 1][1]:
            # if min_heap is empty then that means that there are no events to attend on day d
            if i < n and not min_heap:
                d = events[i][0]

            # add all new events that start at day d
            while i < n and events[i][0] <= d:
                heapq.heappush(min_heap, events[i][1])

            # remove events that have already ended from the heap
            while min_heap and min_heap[0] < d:
                heapq.heapopp(min_heap)

            # attend the event that will end the soonest
            if min_heap:
                heapq.heappop(min_heap)
                res += 1
            elif i >= n:
                break

            d += 1

        return res
