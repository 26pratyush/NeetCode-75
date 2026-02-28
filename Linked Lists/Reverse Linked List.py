# Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.
# Example 1: Input: head = [0,1,2,3]
# Output: [3,2,1,0]

#Solution (Brute-force): Put into array, reverse the array, convert back to linked list
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    current = head
    arr = []

    while current:                            # Collect values
        arr.append(current.val)
        current = current.next

    print(arr)

    rev = []                                  # Reverse values into new list
    for i in range(len(arr) - 1, -1, -1):
        rev.append(arr[i])

    print(rev)

    current = head                            # Write reversed values back into linked list
    for num in rev:
        current.val = num
        current = current.next

    return head
