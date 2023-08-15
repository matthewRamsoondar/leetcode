from typing import *

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {}
        for i in range(numCourses):
            preMap[i] = []

        for i in range(len(prerequisites)):
            course = prerequisites[i][0]
            prereq = prerequisites[i][1]
            preMap[course].append(prereq)

        for course in preMap:
            seen = {}
            if not self.canTake(preMap, course, seen):
                return False

        return True

    def canTake(self, preMap: Dict[int, List[int]], course: int, seen: Dict[int, bool]) -> bool:
        seen[course] = True

        if preMap[course] == []:
            return True

        for prereq in preMap[course]:
            if (prereq in seen) or not self.canTake(preMap, prereq, seen.copy()):
                return False

        return True

a = Solution()

a.canFinish(2, [[1,0],[0,1]])


b = set()
