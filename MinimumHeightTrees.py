from typing import List


class Solution:
    # this is also a correct solution: DFS and then track the subtrees of the DFS tree and then go through each node in DFS order and then find the largest list possible by combining paths
    def findMinHeightTrees2(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 0:
            return []
        # build an adjacency list for this graph
        adj = [[] for _ in range(n)]
        for edge in edges:  # populate the adjacency list
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        visited = [0 for _ in range(n)]
        parents = [-1 for _ in range(n)]
        trees = [[] for _ in range(n)]
        treeLens = [0 for _ in range(n)]

        def dfsVisit(p: int, cur: int):
            # we want to return the list and then the length of the list
            parents[cur] = p
            visited[cur] = 1
            path = [cur]
            pathLen = 1
            for edge in adj[cur]:
                if (visited[edge] == 1):
                    continue
                else:
                    res, resLen = dfsVisit(cur, edge)
                    # resLen = len(res)
                    if resLen + 1 > pathLen:
                        path = res + [cur]
                        pathLen = resLen + 1

            trees[cur] = path
            treeLens[cur] = pathLen
            return path, pathLen

        longestPath = []
        longestPathLen = 0
        dfsVisit(-1, 0)
        for node in range(n):
            p1, p2 = [], []
            p1len, p2len = 0, 0
            for edge in adj[node]:
                if edge == parents[node]:
                    continue

                if treeLens[edge] > p1len:
                    p1, p2 = trees[edge], p1
                    p1len, p2len = treeLens[edge], p1len
                elif treeLens[edge] > p2len:
                    p2 = trees[edge]
                    p2len = treeLens[edge]

            # note that p2 must be p2[::-1] to preserve the correct order
            path = p1 + [node] + p2
            # print(f"node: {node}, p1: {p1}, p2: {p2}, path: {path}")
            pathLen = p1len + p2len + 1
            #print(f"node: {node} p1: {p1}, p2: {p2}")
            if pathLen > longestPathLen:
                # print(path)
                longestPath = path
                longestPathLen = pathLen

        print(f"longest path: {longestPath}")

        n = longestPathLen
        if n & 1 == 0:
            return [longestPath[(n // 2) - 1], longestPath[n // 2]]
        else:
            return [longestPath[(n-1) // 2]]

    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 0:
            return []
        # initialize adjacency lists
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        seen = [0 for _ in range(n)]

        def dfs(p: int, cur: int) -> List[int]:
            seen[cur] = 1
            path, pathLen = [cur], 1
            for edge in adj[cur]:
                if seen[edge] == 1:
                    continue
                else:
                    res, resLen = dfs(cur, edge)
                    if resLen + 1 > pathLen:
                        path, pathLen = res + [cur], resLen + 1

            seen[cur] = 0
            return path, pathLen

        leaf = dfs(-1, 0)[0][0]
        longestPath, longestPathLen = dfs(-1, leaf)

        if longestPathLen & 1 == 1:
            return [longestPath[(longestPathLen - 1) // 2]]
        else:
            return [longestPath[(longestPathLen // 2) - 1], longestPath[longestPathLen // 2]]


def main():
    a = Solution()
    # res = a.findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]])
    # res = a.findMinHeightTrees(6, [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]])
    # res = a.findMinHeightTrees(3, [[0, 1], [0, 2]])
    res = a.findMinHeightTrees(
        7, [[0, 1], [0, 3], [1, 2], [1, 4], [1, 5], [4, 6]])
    # res = a.findMinHeightTrees(5, [[0, 1], [0, 2], [0, 3], [3, 4]])
    # res = a.findMinHeightTrees(
    #     7, [[0, 1], [1, 2], [1, 3], [2, 4], [3, 5], [4, 6]])
    # res = a.findMinHeightTrees(10, [[0, 1], [0, 2], [0, 3], [2, 4], [
    #                            0, 5], [5, 6], [6, 7], [2, 8], [7, 9]])

    print(res)


main()
