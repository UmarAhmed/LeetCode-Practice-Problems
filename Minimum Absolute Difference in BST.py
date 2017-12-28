# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root):
        lst = self.inorder(root)
        return min([abs(lst[i] - lst[i + 1]) for i in range(len(lst) - 1)])

    def inorder(self, root): #flattens the given bst
        return self.inorder(root.left) + [root.val] + self.inorder(root.right) if root else []