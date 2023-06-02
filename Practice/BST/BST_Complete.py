###
# Participation - BST
# Author: Nam Jun Lee
# Date: November 1st, 2021
# Description: implementation code to the current BinarySearchTree class.
###

class BSTNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.value = val
        self.left_child = left
        self.right_child = right
        self.parent = parent

    def __iter__(self):
        """
        Yield freezes the state of the function so that the next time the function
        is called it continues executing from the exact point it left off earlier.
        """
        if self:
            if self.has_left_child():
                for elem in self.left_child:
                    yield elem
            yield self.key
            if self.has_right_child():
                for elem in self.right_child:
                    yield elem

    def has_left_child(self):
        return self.left_child

    def has_right_child(self):
        return self.right_child

    def is_left_child(self):
        return self.parent and self.parent.left_child == self

    def is_right_child(self):
        return self.parent and self.parent.right_child == self

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not (self.right_child or self.left_child)

    def has_any_children(self):
        return self.right_child or self.left_child

    def has_both_children(self):
        return self.right_child and self.left_child

    def replace_node_data(self, key, value, lc, rc):
        """
        Overwrite this node's information with new information in the parameters
        """
        self.key = key
        self.value = value
        self.left_child = lc
        self.right_child = rc
        if self.has_left_child():
            self.left_child.parent = self
        if self.has_right_child():
            self.right_child.parent = self

    def splice_out(self):
        """
        Go directly to the node we want to splice out and makes the right changes.
        Handles case 1 and 2 of delete()
        No need to search for node to delete (unlike delete())
        """
        if self.is_leaf():  # delete() case 1 (no children)
            if self.is_left_child():
                self.parent.left_child = None
            else:
                self.parent.right_child = None
        elif self.has_any_children():  # delete case 2 (exactly one child)
            if self.has_left_child():
                if self.is_left_child():
                    self.parent.left_child = self.left_child
                else:
                    self.parent.right_child = self.left_child
                self.left_child.parent = self.parent
            else:
                if self.is_left_child():
                    self.parent.left_child = self.right_child
                else:
                    self.parent.right_child = self.right_child
                self.right_child.parent = self.parent

    def find_successor(self):
        """
        3 cases when looking for the successor:

        1. If the node has a right child, then the successor is the smallest key in the right subtree.
        2. If the node has no right child and is the left child of its parent, then the parent is the successor.
        3. If the node is the right child of its parent, and itself has no right child,
        then the successor to this node is the successor of its parent, excluding this node.
        """
        succ = None
        if self.has_right_child():
            succ = self.right_child.find_min()
        else:
            if self.parent:
                if self.is_left_child():
                    succ = self.parent
                else:
                    self.parent.right_child = None
                    succ = self.parent.find_successor()
                    self.parent.right_child = self
        return succ

    def find_min(self):
        """
        Find the minimum key in a subtree.
        Left-most child in the subtree.
        """
        current = self
        while current.has_left_child():
            current = current.left_child
        return current


class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        """
        Return the number of key-value pairs stored in the map.
        """
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def __setitem__(self, k, v):
        self.put(k, v)

    def __getitem__(self, key):
        return self.get(key)

    def __delitem__(self, key):
        """
        Delete the key-value pair from the map using a statement of the form del map[key].
        """
        self.delete(key)

    def __contains__(self, key):
        """
        Return True for a statement of the form key in map, if the given key is in the map.
        """
        if self._get(key, self.root):
            return True
        else:
            return False

    def put(self, key, val):
        """
        Add a new key-value pair to the map.
        If the key is already in the map then replace the old value with the new value.

        If there is not a root then put will create a new BSTNode and install it as the root of the tree. If a root
        node is already in place then put calls the private, recursive, helper function _put to search the tree
        """
        # To Be Defined
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = BSTNode(key, val)
        self.size += 1

    def _put(self, key, val, current_node):
        """
        Starting at the root of the tree, search the binary tree comparing the new key
        to the key in the current node. If the new key is less than the current node,
        search the left subtree. If the new key is greater than the current node,
        search the right subtree.

        When there is no left (or right) child to search, we have found the position
        in the tree where the new node should be installed.

        To add a node to the tree, create a new BStNode object and insert the object
        at the point discovered in the previous step.
        """
        # To Be Defined
        if key == current_node.key:
            current_node.value = val
        elif key < current_node.key:
            if current_node.has_left_child():
                self._put(key, val, current_node.left_child)
            else:
                current_node.left_child = BSTNode(key, val, parent=current_node)
        else:
            if current_node.has_right_child():
                self._put(key, val, current_node.right_child)
            else:
                current_node.right_child = BSTNode(key, val, parent=current_node)

    def get(self, key):
        """
        Given a key, return the value stored in the map or None otherwise.
        """
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.value
            else:
                return None
        else:
            return None

    def _get(self, key, current_node):
        """
        searches the tree recursively until it gets to a non-matching leaf node or finds a matching key.
        When a matching key is found, the value stored in the payload of the node is returned.
        """
        if not current_node:
            return None
        elif current_node.key == key:
            return current_node
        elif key < current_node.key:
            return self._get(key, current_node.left_child)
        else:
            return self._get(key, current_node.right_child)

    def delete(self, key):
        """
        Find the node to delete by searching the tree using the
        _get method to find the BSTNode that needs to be removed.

        If the tree only has a single node, that means we are removing the root of the tree,
        but we still must check to make sure the key of the root matches the key that is to be deleted.
        """
        # To Be Completed
        if self.size > 1:
            node_remove = self._get(key, self.root)
            if node_remove:
                self.remove(node_remove)
                self.size -= 1

    @staticmethod
    def remove(current_node):
        """
        3 cases to consider:
        1. The node to be deleted has no children
        --->Delete the node and remove the reference to this node in the parent.
        2. The node to be deleted has only one child
        -->Promote the child to take the place of its parent.
        -->If the current node has no parent, it must be the root. Replace the key, value, left_child,
        and right_child data by calling the replace_node_data method on the root.
        3. The node to be deleted has two children
        -->Search the tree for a node (successor) that can be used to replace the one scheduled for deletion
        -->Remove the successor and put it in the tree in place of the node to be deleted.
        """
        # To Be Completed
        if current_node.is_leaf():
            if current_node == current_node.parent.left_child:
                current_node.parent.left_child = None
            else:
                current_node.parent.right_child = None
        elif current_node.has_both_children():
            s = current_node.find_successor()
            s.splice_out()
            current_node.key = s.key
            current_node.value = s.value
        else:
            if current_node.has_left_child():
                if current_node.is_left_child():
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.left_child
                elif current_node.is_right_child():
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.left_child
                else:
                    current_node.replace_node_data(current_node.left_child.key,
                                                   current_node.left_child.value,
                                                   current_node.left_child.left_child,
                                                   current_node.left_child.right_child)
            else:
                if current_node.is_left_child():
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.right_child
                elif current_node.is_right_child():
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.right_child
                else:
                    current_node.replace_node_data(current_node.right_child.key,
                                                   current_node.right_child.value,
                                                   current_node.right_child.left_child,
                                                   current_node.right_child.right_child)

    def in_order_traversal(self):
        if self.size > 0:
            self.in_order_helper(self.root)
            print()
        else:
            print("Empty tree")

    def in_order_helper(self, current_node):
        if current_node is not None:
            self.in_order_helper(current_node.left_child)
            print(str(current_node.key) + ":" + str(current_node.value), end=" ")
            self.in_order_helper(current_node.right_child)

    def pre_order_traversal(self):
        if self.size > 0:
            self.pre_order_helper(self.root)
            print()
        else:
            print("Empty Tree")

    def pre_order_helper(self, current_node):
        if current_node is not None:
            print(str(current_node.key) + ":" + str(current_node.value), end=", ")
            self.pre_order_helper(current_node.left_child)
            self.pre_order_helper(current_node.right_child)

    def post_order_traversal(self):
        if self.size > 0:
            self.post_order_helper(self.root)
            print()
        else:
            print("Empty Tree")

    def post_order_helper(self, current_node):
        if current_node is not None:
            self.post_order_helper(current_node.left_child)
            self.post_order_helper(current_node.right_child)
            print(str(current_node.key) + ":" + str(current_node.value), end=", ")
