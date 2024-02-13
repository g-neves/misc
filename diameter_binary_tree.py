import unittest



class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right 

def calculate_diameter(root):
    if root is None:
        return 0

    left_height = calculate_height(root.left)
    right_height = calculate_height(root.right)

    left_diameter = calculate_diameter(root.left)
    right_diameter = calculate_diameter(root.right)

    return max(left_height + right_height, max(left_diameter, right_diameter))

def calculate_height(node):
    if node is None:
        return 0

    return 1 + max(calculate_height(node.left), calculate_height(node.right))


class TestBinaryTreeFunctions(unittest.TestCase):

    def test_calculate_diameter_and_height(self):
        # Creating a sample binary tree for testing
        #       1
        #      / \
        #     2   3
        #    / \
        #   4   5
        root = Node(1, Node(2, Node(4), Node(5)), Node(3))

        # Expected diameter: 3 (Path: 4 -> 2 -> 1 -> 3)
        # Expected height of left subtree: 2 (Path: 4 -> 2 -> 1)
        # Expected height of right subtree: 1 (Path: 3 -> 1)
        self.assertEqual(calculate_diameter(root), 3)
        self.assertEqual(calculate_height(root.left), 2)
        self.assertEqual(calculate_height(root.right), 1)

    def test_empty_tree(self):
        root = None
        self.assertEqual(calculate_diameter(root), 0)
        self.assertEqual(calculate_height(root), 0)

if __name__ == '__main__':
    unittest.main()

