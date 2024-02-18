from typing import List


class INumArray:
    sum: int

    def update(self, index: int, val: int) -> None:
        raise NotImplementedError()

    def sumRange(self, left: int, right: int) -> int:
        raise NotImplementedError()


class NumArray(INumArray):
    sum: int
    L: int  # Left index this node holds
    R: int  # Right index this node holds
    left: INumArray
    Right: INumArray
    nums: List[int]

    def __init__(self, nums: List[int], L: int = None, R: int = None):
        self.sum = 0
        n = len(nums)
        self.nums = nums
        self.L = L if (L is not None) else 0
        self.R = R if (R is not None) else n - 1
        self.left = None
        self.right = None

        if self.L == self.R:
            self.sum = nums[self.L]
            return

        M = (self.L + self.R) // 2
        self.left = NumArray(nums, L=self.L, R=M)
        self.right = NumArray(nums, L=M + 1, R=self.R)

        self.sum = self.left.sum + self.right.sum

    def update(self, index: int, val: int) -> None:
        if self.L == index == self.R:
            self.sum = val
            return

        M = (self.L + self.R) // 2
        if index <= M:
            self.left.update(index, val)
        else:
            self.right.update(index, val)

        self.sum = self.left.sum + self.right.sum

    def sumRange(self, left: int, right: int) -> int:
        if self.L == left and self.R == right:
            return self.sum

        M = (self.L + self.R) // 2
        if right <= M:
            return self.left.sumRange(left, right)
        elif left > M:
            return self.right.sumRange(left, right)
        else:
            return self.left.sumRange(left, M) + self.right.sumRange(M + 1, right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
