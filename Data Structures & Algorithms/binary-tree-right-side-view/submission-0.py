# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:  
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        big_lst = []
        q = deque()
        if root:
            q.append(root)
        while len(q) > 0:
            rightest = len(q)
            for i in range(len(q)):
                node = q.popleft()
                if i == rightest - 1:
                    big_lst.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return big_lst