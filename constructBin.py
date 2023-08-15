# given an array, construct a binary tree from the input

# Ex. input = [3, 9, 2, 1, 4, 5]
# output:
#       3
#    /    \
#   9      2
#  / \    /
# 1   4  5

from typing import List


class TreeNode:
    val: int

    def __init__(self, val=None) -> None:
        self.val = val
        self.left = None
        self.right = None


def constructTree(input: List[int]) -> TreeNode:
    root = TreeNode(input[0])

    def appendChildren(root: TreeNode, root_index: TreeNode, input: List[int]):
        left_num = None
        right_num = None

        if 2*root_index + 1 < len(input):
            left_num = input[2*root_index + 1]

        if 2*root_index + 2 < len(input):
            right_num = input[2*root_index + 2]

        if left_num is not None:
            root.left = TreeNode(left_num)
            appendChildren(root.left, 2*root_index + 1, input=input)
        if right_num is not None:
            root.right = TreeNode(right_num)
            appendChildren(root.right, 2*root_index + 2, input=input)

    appendChildren(root, 0, input)
    return root


a = constructTree([3, 9, 2, 1, 4, 5])

print(a.val)  # 3
print(a.left.val)  # 9
print(a.right.val)  # 2
print(a.left.left.val)  # 1
print(a.left.right.val)  # 4
print(a.right.left.val)  # 5
