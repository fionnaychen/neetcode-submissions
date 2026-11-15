# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) <= 0:
            return None
        root_val = preorder.pop(0)
        root_index = inorder.index(root_val)
        left = self.buildTree(preorder[:root_index], inorder[:root_index])
        right = self.buildTree(preorder[root_index:], inorder[root_index + 1:])
        root = TreeNode(root_val, left, right)
        return root
        