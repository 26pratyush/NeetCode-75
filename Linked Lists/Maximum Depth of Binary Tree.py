# Given the root of a binary tree, return its depth.
# The depth of a binary tree is defined as the number of nodes along the longest path from the root node down to the farthest leaf node.

def maxDepth(self, root: Optional[TreeNode]) -> int:
    if root is None:
        return 0

    ld = self.maxDepth(root.left)
    rd = self.maxDepth(root.right)

    return 1 + max(ld, rd)
