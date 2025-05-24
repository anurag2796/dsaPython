"""
Problem: Diameter of Binary Tree

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
This path may or may not pass through the root. The length of a path is the number of edges between nodes.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        """
        Binary Tree Node definition.
        :param val: Value of the node
        :param left: Left child (TreeNode or None)
        :param right: Right child (TreeNode or None)
        """
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        """
        Computes the diameter (longest path between any two nodes) in a binary tree.

        :param root: TreeNode - root of the binary tree
        :return: int - the diameter (number of edges in longest path)
        """
        self.max_diameter = 0

        def dfs(node):
            if not node:
                return 0

            left_height = dfs(node.left)
            right_height = dfs(node.right)

            # Update diameter if path through this node is longer
            self.max_diameter = max(self.max_diameter, left_height + right_height)

            # Return height of current node
            return 1 + max(left_height, right_height)

        dfs(root)
        return self.max_diameter


def main():
    """
    Builds a sample binary tree and prints the diameter.
    Tree structure:
            1
           / \
          2   3
         / \
        4   5

    Expected diameter: 3 (path = 4 → 2 → 1 → 3)
    """
    # Build the tree in one line
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))

    sol = Solution()
    result = sol.diameterOfBinaryTree(root)
    print("Diameter of the tree:", result)


if __name__ == "__main__":
    main()
