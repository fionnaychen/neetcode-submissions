# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # define min val in da tree
        def min_tree(root):
            while root and root.left:
                root = root.left
            return root
        
        if not root:
            return root
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.right:
                return root.left
            elif not root.left:
                return root.right

            min_val = min_tree(root.right)
            root.val = min_val.val
            root.right = self.deleteNode(root.right, min_val.val)
        return root

