# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        def traverse(node):
            if not node:
                return None
            left = traverse(node.left)
            right = traverse(node.right)
            subtree = (node.val, left, right)
            subtree_id = subtree_ids.get(subtree)
            if subtree_id is None:
                subtree_id = len(subtrees)
                subtrees.append(subtree)
                subtree_ids[subtree] = subtree_id
            subtree_counts[subtree_id] += 1
            if subtree_counts[subtree_id] == 2:
                duplicates.append(node)
            return subtree_id

        subtrees = []
        subtree_ids = {}
        subtree_counts = defaultdict(int)
        duplicates = []
        traverse(root)
        return duplicates

        