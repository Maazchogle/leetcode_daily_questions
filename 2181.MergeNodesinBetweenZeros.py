2181. Merge Nodes in Between Zeros
Medium
Topics
Companies
Hint
You are given the head of a linked list, which contains a series of integers separated by 0's. The beginning and end of the linked list will have Node.val == 0.

For every two consecutive 0's, merge all the nodes lying in between them into a single node whose value is the sum of all the merged nodes. The modified list should not contain any 0's.

Return the head of the modified linked list.

 

Example 1:


Input: head = [0,3,1,0,4,5,2,0]
Output: [4,11]
Explanation: 
The above figure represents the given linked list. The modified list contains
- The sum of the nodes marked in green: 3 + 1 = 4.
- The sum of the nodes marked in red: 4 + 5 + 2 = 11.
Example 2:


Input: head = [0,1,0,3,0,2,2,0]
Output: [1,3,4]
Explanation: 
The above figure represents the given linked list. The modified list contains
- The sum of the nodes marked in green: 1 = 1.
- The sum of the nodes marked in red: 3 = 3.
- The sum of the nodes marked in yellow: 2 + 2 = 4.
 

Constraints:

The number of nodes in the list is in the range [3, 2 * 105].
0 <= Node.val <= 1000
There are no two consecutive nodes with Node.val == 0.
The beginning and end of the linked list have Node.val == 0.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeNodes(self, head):
        dummy = ListNode()
        current = dummy
        sum_val = 0
        
        while head:
            if head.val == 0:
                if sum_val != 0:
                    current.next = ListNode(sum_val)
                    current = current.next
                    sum_val = 0
            else:
                sum_val += head.val
            head = head.next
        
        return dummy.next

# Helper function to create a linked list from a list
def create_linked_list(arr):
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print a linked list
def print_linked_list(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values

# Example 1
head1 = create_linked_list([0, 3, 1, 0, 4, 5, 2, 0])
merged_head1 = Solution().mergeNodes(head1)
print(print_linked_list(merged_head1))  # Output: [4, 11]

# Example 2
head2 = create_linked_list([0, 1, 0, 3, 0, 2, 2, 0])
merged_head2 = Solution().mergeNodes(head2)
print(print_linked_list(merged_head2))  # Output: [1, 3, 4]
