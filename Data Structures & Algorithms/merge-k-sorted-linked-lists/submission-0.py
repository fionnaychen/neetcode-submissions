# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def insert(self, lst, node):
        if lst.val > node.val:
            node.next = lst
            return node
        pointer = lst
        while pointer.next and pointer.next.val <= node.val:
            pointer = pointer.next
        if pointer.next:
            tmp = pointer.next
            node.next = tmp
        else:
            node.next = None
        pointer.next = node
        return lst
         

    def merge(self, list1, list2):
        l1_prev = None
        l2_prev = None
        l1 = list1
        l2 = list2
        while l1 and l2:
            if l1.val <= l2.val:
                l1_prev = l1
                l1 = l1.next
            else:
                tmp = l2
                l2_prev = l2
                l2 = l2.next
                list1 = self.insert(list1, tmp)
        if l2:
            l1_prev.next = l2
        return list1


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        for i in range(len(lists)-1):
            lists[i+1] = self.merge(lists[i],lists[i+1])
        return lists[-1]
        
