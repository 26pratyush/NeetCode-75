# Given the roots of two binary trees p and q, return true if the trees are equivalent, otherwise return false.
# Two binary trees are considered equivalent if they share the exact same structure and the nodes have the same values.

#Solution:
def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not p and not q:
        return True
        
    if not p or not q or p.val != q.val:
        return False
        
    return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
