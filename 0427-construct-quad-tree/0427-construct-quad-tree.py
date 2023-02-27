"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def construct_range(top, left, l):
            """
            Construct a node representing the subgrid with
            top left corner at (top, left) and side length l
            """
            if l == 1:
                return Node(grid[top][left], True)
            topLeft = construct_range(top, left, l // 2)
            topRight = construct_range(top, left + l // 2, l // 2)
            botLeft = construct_range(top + l // 2, left, l // 2)
            botRight = construct_range(top + l // 2, left + l // 2, l // 2)

            children = [topLeft, topRight, botLeft, botRight]
            # Check if all subgrids have the same value
            if all(child.isLeaf and child.val == topLeft.val for child in children):
                return Node(topLeft.val, True)
            
            return Node(0, False, topLeft, topRight, botLeft, botRight)
        
        return construct_range(0, 0, len(grid))
        