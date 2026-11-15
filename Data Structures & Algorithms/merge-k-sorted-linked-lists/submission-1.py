# Definition for singly-linked llists[i+1]ist.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def merge(self, l1, l2):
        dummy = ListNode()
        curr = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                curr = l1
                l1 = l1.next
            else:
                curr.next = l2
                curr = l2
                l2 = l2.next
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        while len(lists) > 1:
            new_lists = []
            for i in range(0,len(lists),2):
                list1 = lists[i]
                if i < len(lists) - 1:
                    list2 = lists[i+1]
                else:
                    list2 = None
                merged = self.merge(list1, list2)
                new_lists.append(merged)
            lists = new_lists
        return lists[0]
        

        