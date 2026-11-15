"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        # q is old nodes left to check
        q = deque()

        # visited is {val : Node}, where node is the new node
        visited = {}
        q.append(node)
        visited[node.val] = Node(node.val)
        while q:
            for i in range(len(q)):
                cur_node = q.popleft()
                print(cur_node.val) 
                #visited[cur_node.val] = Node(cur_node.val)
                for neighbor in cur_node.neighbors:
                    print(neighbor.val)   
                    if neighbor.val not in visited:
                        visited[neighbor.val] = Node(neighbor.val)
                        q.append(neighbor)
                    visited[cur_node.val].neighbors.append(visited[neighbor.val])
        return visited[1]