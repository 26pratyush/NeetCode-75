# Given the beginning of a linked list head, return true if there is a cycle in the linked list. Otherwise, return false.
# There is a cycle in a linked list if at least one node in the list can be visited again by following the next pointer.

# Example: Input: head = [1,2,3,4], index = 1
# Output: true

def hasCycle(self, head: Optional[ListNode]) -> bool:
  fast, slow = head, head
        
  while fast and fast.next:
      fast = fast.next.next
      slow = slow.next
      if fast == slow:
          return True
                
  return False
