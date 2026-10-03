# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def height(node):
            if not node:
                return 0

            left = height(node.left)
            right = height(node.right)

            return 1 + max(left, right)

        def diameter(node):
            if not node:
                return 0

            left_height = height(node.left)
            right_height = height(node.right)

            curr_dia = left_height + right_height

            left_dia = diameter(node.left)
            right_dia = diameter(node.right)

            return max(curr_dia, left_dia, right_dia)

        return diameter(root)
        