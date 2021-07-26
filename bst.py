class Node:
    """
        Class representing the node in the binary tree.
        "left" and "right" represent the left and right branches of that node.
        "value" is thee value of the node.
    """

    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key


def insert(root, key):
    """
        Function to insert a new node in the BST.
        root - Root node of the tree
        key - Value for the node.
    """
    if root is None:
        return Node(key)
    else:
        if root.value == key:
            return root
        elif root.value < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root


"""
    Time Complexity: 
        Worst Case - O(h)
        h = height of the BST
"""


def inorder(root):
    """
        Function for inorder traversal(left - root - right) of the given tree.
    """
    if root:
        inorder(root.left)
        print(root.value)
        inorder(root.right)


def preorder(root):
    """
        Function for preorder traversal(root - left - right)
    """
    if root:
        print(root.value)
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    """
        Function for postorder traversal(left - right - root)
    """
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.value)

# Time complexity: O(n) or Θ(n) (theta n)


def delete(root, key):
    """
        Function to delete a node in the BST.
        root - Root node
        key - Value to be deleted
    """
    if root == None:
        return root

    if key < root:
        root.left = delete(root.left, key)
        return root
    elif key > root:
        root.right = delete(root.right, key)
        return root

    # If root node is the leaf node
    if root.left == None and root.right == None:
        return None

    if root.left == None:
        temp = root.right
        root = None
        return temp

    if root.right == None:
        temp = root.left
        root = None
        return temp

    # If both children exist
    succParent = root
    succ = root.right
 
    while succ.left != None:
        succParent = succ
        succ = succ.left
 
    if succParent != root:
        succParent.left = succ.right
    else:
        succParent.right = succ.right
 
    root.key = succ.key

    return root

"""
    Time Complexity: 
        Worst Case - O(h)
        h = height of the BST
"""