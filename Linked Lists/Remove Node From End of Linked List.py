# You are given the beginning of a linked list head, and an integer n.
# Remove the nth node from the end of the list and return the beginning of the list.

# Example 1: Input: head = [1,2,3,4], n = 2
# Output: [1,2,4]

# Example 2: Input: head = [5], n = 1
# Output: []

#Solution: Brute-force: Convert to array -> Remove nth ele from end -> Convert back to linked list with one node less
current = head
arr = []

while current:                  #Convert to array
    arr.append(current.val)
    current = current.next

arr.pop(len(arr) - n)           #Remove the n'th ele from end

if not arr:                     #If array now empty
    return None

current = head
for i in range(len(arr)):      #Overwrite the og LL wih one node less
    current.val = arr[i]
    if i == len(arr) - 1:
        current.next = None
    current = current.next

return head
