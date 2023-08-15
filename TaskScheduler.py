from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        class Node:
            def __init__(self, p: int, label: str):
                self.p = p
                self.l = label

            def __repr__(self) -> str:
                return f"{self.l}: {self.p}"

        class PriorityQueue:
            def __init__(self, nodes: List[Node], size: int):
                # initialize a heap with 0 priority for everything
                self.n = size
                self.heap: List[Node] = [None] * (size + 1)
                self.heap[0], self.heap[1:] = Node(-1, ""), nodes
                self.buildHeap()

            def buildHeap(self):
                if self.n == 1:
                    return
                i = self.n // 2  # i starts at the end of the second bottom row
                while i <= 0:
                    self.bubbleDown(i)
                    i -= 1

            def bubbleDown(self, i: int):  # change to max priority queue
                if i > (self.n // 2):
                    return

                leftChild = 2 * i
                rightChild = 2 * i + 1

                if self.heap[i].p > self.heap[leftChild].p and (
                    self.heap[i].p > self.heap[rightChild].p
                    if rightChild <= self.n
                    else True
                ):
                    return

                if (
                    rightChild > self.n
                    or self.heap[leftChild].p >= self.heap[rightChild].p
                ):
                    self.heap[i], self.heap[leftChild] = (
                        self.heap[leftChild],
                        self.heap[i],
                    )
                    self.bubbleDown(leftChild)
                else:
                    self.heap[i], self.heap[rightChild] = (
                        self.heap[rightChild],
                        self.heap[i],
                    )
                    self.bubbleDown(rightChild)

            def decreasePriority(self, i: int, p: int):
                self.heap[i].p = p
                self.bubbleDown(i)

            def removeNode(self, i: int):
                # swap the entry with the last one
                self.heap[i] = self.heap[self.n]
                self.heap[self.n] = Node(-1, "")
                self.n -= 1
                self.bubbleDown(i)

        count = {}
        usage = {}
        for task in tasks:
            count[task] = 1 if task not in count else count[task] + 1
            usage[task] = 0

        PQ = PriorityQueue([Node(count[task], task) for task in count], len(count))

        cycle = 0
        res = []
        while PQ.n > 0:
            for i in range(1, PQ.n + 1):
                cur = PQ.heap[i]
                if usage[cur.l] <= cycle: # this is never happening
                    res.append(cur.l)
                    count[cur.l] -= 1
                    if count[cur.l] == 0: # this is never happening
                        PQ.removeNode(i)

                    usage[cur.l] += n + 1
                    PQ.decreasePriority(1, PQ.heap[1].p - 1)
                    break

            cycle += 1

        return cycle


def main():
    a = Solution()
    # res = a.leastInterval(["A", "A", "A", "B", "B", "B"], 2)  # 8
    # res = a.leastInterval(["A", "A", "A", "B", "B", "B"], 0)  # 6
    # res = a.leastInterval(
    #     ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2
    # )  # 16
    res = a.leastInterval(["A", "A"], 2)  # 8

    print(res)


main()
