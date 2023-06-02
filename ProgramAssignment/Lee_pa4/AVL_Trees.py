###
# Title: AVL Trees (PA5)
# Author: Nam Jun Lee
# Version: 1.0
# Date: November 7th, 2021
#
# Description: Implement delete, remove and update_balance_delete implementations on AVL Trees and
# visualize the tree using visualize and visualize_helper methods within AVL Tree class and save the
# tree visualization to .pdf file.
###

# import modules
from graphviz import Graph


class BSTNode:
    """
    A class representing a BSTNode.
    BSTNode is a data structure that stores data.
    Refer to lecture slides.
    Using AVL Tree.
    """

    def __init__(self, key, val, left=None, right=None, parent=None):
        """
        Create properties for BSTNode Class.
        """
        self.key = key
        self.value = val
        self.left_child = left
        self.right_child = right
        self.parent = parent
        self.balance_factor = 0

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


class AVLTree:
    """
    A class representing a AVLTree.
    Refer to lecture slides.
    """

    def __init__(self):
        """
        Create properties for AVL Tree class.
        Returns nothing
        """
        self.root = None
        self.size = 0

    def length(self):
        """
        This shows that current tree length
        Returns: tree size (integer)
        """
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
        If there is not a root then put will create a new TreeNode and install it as the root of the tree. If a root
        node is already in place then put calls the private, recursive, helper function _put to search the tree
        """
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = BSTNode(key, val)
        self.size = self.size + 1

    def get(self, key):
        """
        Given a key, return the value stored in the map or None otherwise.
        Like a Search method.
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
        Like a get helper.
        """
        if not current_node:
            return None
        elif current_node.key == key:
            return current_node
        elif key < current_node.key:
            return self._get(key, current_node.left_child)
        else:
            return self._get(key, current_node.right_child)

    def _put(self, key, val, current_node):
        """
        _put is exactly the same as in simple binary search trees
        except for the additions of the calls to update_balance
        Like a put helper.
        """
        if key == current_node.key:
            current_node.value = val
        elif key < current_node.key:
            if current_node.has_left_child():
                self._put(key, val, current_node.left_child)
            else:
                current_node.left_child = BSTNode(key, val, parent=current_node)
                self.update_balance(current_node.left_child)
        else:
            if current_node.has_right_child():
                self._put(key, val, current_node.right_child)
            else:
                current_node.right_child = BSTNode(key, val, parent=current_node)
                self.update_balance(current_node.right_child)

    def update_balance(self, node):
        """
        two base cases for updating balance factors:
        1. The recursive call has reached the root of the tree.
        2. The balance factor of the parent has been adjusted to zero.
        first checks to see if the current node is out of balance enough to require rebalancing
        if that is the case then the rebalancing is done and no further updating to parents is required
        if the current node does not require rebalancing then the balance factor of the parent is adjusted
        if the balance factor of the parent is non-zero then the algorithm continues to work its way
        up the tree toward the root by recursively calling updateBalance on the parent.
        """
        if node.balance_factor > 1 or node.balance_factor < -1:
            self.rebalance(node)
            return
        if node.parent is not None:
            if node.is_left_child():
                node.parent.balance_factor += 1
            elif node.is_right_child():
                node.parent.balance_factor -= 1
            if node.parent.balance_factor != 0:
                self.update_balance(node.parent)

    def rebalance(self, node):
        """
        fix a height violation by performing rotations depending on the case
        four base cases for rebalance factors:
        CASE 1: Insert into the left subtree of the left child of k
        -->single right rotation
        CASE 2: Insert into the right subtree of the left child of k
        -->double rotation: single left then single right
        CASE 3: Insert into the left subtree of the right child of k
        -->double rotation: single right then single left
        CASE 4: Insert into the right subtree of the right child of k
        -->single left rotation
        """
        if node.balance_factor < 0:
            if node.right_child.balance_factor > 0:
                # CASE 3
                self.rotate_right(node.right_child)
                self.rotate_left(node)
            else:
                # CASE 4
                self.rotate_left(node)
        elif node.balance_factor > 0:
            if node.left_child.balance_factor < 0:
                # CASE 2
                self.rotate_left(node.left_child)
                self.rotate_right(node)
            else:
                # CASE 1
                self.rotate_right(node)

    def rotate_left(self, new):
        """
        new root of the subtree is the right child of previous root
        right child of root is replaced with the left child of the new root
        adjust the parent references.
        """
        new_roL = new.right_child
        new.right_child = new_roL.left_child
        if new_roL.left_child is not None:
            new_roL.left_child.parent = new
        new_roL.parent = new.parent
        if new.is_root():
            self.root = new_roL
        else:
            if new.is_left_child():
                new.parent.left_child = new_roL
            else:
                new.parent.right_child = new_roL
        new_roL.left_child = new
        new.parent = new_roL
        new.balance_factor = new.balance_factor + 1 - min(new_roL.balance_factor, 0)
        new_roL.balance_factor = new_roL.balance_factor + 1 + max(new.balance_factor, 0)

    def rotate_right(self, new):
        """
        new root of the subtree is the left child of previous root
        left child of root is replaced with the right child of the new root
        adjust the parent references.
        """
        new_roR = new.left_child
        new.left_child = new_roR.right_child
        if new_roR.right_child is not None:
            new_roR.right_child.parent = new
        new_roR.parent = new.parent
        if new.is_root():
            self.root = new_roR
        else:
            if new.is_right_child():
                new.parent.right_child = new_roR
            else:
                new.parent.left_child = new_roR
        new_roR.right_child = new
        new.parent = new_roR
        new.balance_factor = new.balance_factor - 1 - max(new_roR.balance_factor, 0)
        new_roR.balance_factor = new_roR.balance_factor - 1 + min(new.balance_factor, 0)

    def level_order_traversal(self):
        """
        Touring in the order of the tree's node level.
        """
        if self.size > 0:
            queue = ["{" + str(self.root.key) + ":" + str(self.root.value) + "(%d)" % self.root.balance_factor + "}",
                     "\n"]
            self.level_order_helper(self.root, queue)
            for data in queue:
                print(data, end="")
            print()
        else:
            print("Empty tree")

    def level_order_helper(self, node, queue):
        """
        help to level_order_traversal.
        """
        if node is not None:
            if node.left_child is not None:
                temp = node.left_child
                queue.append("{" + str(temp.key) + ":" + str(temp.value) + "(%d)" % temp.balance_factor + "}")
            if node.right_child is not None:
                temp = node.right_child
                queue.append("{" + str(temp.key) + ":" + str(temp.value) + "(%d)" % temp.balance_factor + "}")
            queue.append("\n")
            self.level_order_helper(node.left_child, queue)
            self.level_order_helper(node.right_child, queue)

    def delete(self, key):
        """
        After finding the tree node to be removed,
        make sure that the key of the root matches the key to be deleted,
        and then remove it.
        If the key is in the tree, returns True. If the key is not in the tree, False is returned.
        """
        if self.size > 1:
            node_to_remove = self._get(key, self.root)
            if node_to_remove:
                self.remove(node_to_remove)
                self.size = self.size - 1
            else:
                return False
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            return False

    def remove(self, current_node):
        """
        During the node removal operation, the update_balance_delete method is called within the remove method, and
        if the item is removed from the tree, then it help to the balance the tree.
        It help to delete methods.
        Refer to lecture slides.
        """
        if current_node.is_leaf():
            if current_node == current_node.parent.left_child:
                current_node.parent.left_child = None
                self.update_balance_delete(current_node.parent.right_child)
            else:
                current_node.parent.right_child = None
                self.update_balance_delete(current_node.parent.left_child)
        elif current_node.has_both_children():
            succ = current_node.find_successor()
            succ.splice_out()
            current_node.key = succ.key
            current_node.value = succ.value
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

    def update_balance_delete(self, node):
        """
        If the node has parent, then update parent's balance factor.
        If the parent node is unbalanced, then recursively call rebalance method
        If the parent's balance factor is not zero, then recursively call itself.
        """
        if node.balance_factor > 1 or node.balance_factor < -1:
            self.rebalance(node)
            self.update_balance_delete(node.parent.parent)
            return
        if node.parent is not None:
            if node.is_left_child():
                node.parent.balance_factor += 1
            elif node.is_right_child():
                node.parent.balance_factor -= 1
            if node.parent.balance_factor != 0:
                self.update_balance_delete(node.parent)

    def visualize_after(self, file):
        """
        Use the graph() constructor method to add the root node to the graph plot
        and invoke visual_helper(node) as an aggregate.
        It also renders tree visualizations to .pdf files.
        """
        a = Graph(file)
        if self.size > 0:
            queue = ["[" + str(self.root.key) + "] " + str(self.root.value) + "(%d)" % self.root.balance_factor]
            self.visualize_helper(self.root, queue)
            for data in queue:
                a.node(data)
            a.edge(queue[0], queue[1])
            a.edge(queue[0], queue[2])
            a.edge(queue[1], queue[3])
            a.edge(queue[1], queue[4])
            a.edge(queue[2], queue[6])
            a.edge(queue[4], queue[5])
            a.render(view=True)
            a.render(filename="After_delete_AVL_tree")
        else:
            print("Empty tree")

    def visualize_before(self, file):
        """
        Use the graph() constructor method to add the root node to the graph plot
        and invoke visual_helper(node) as an aggregate.
        It also renders tree visualizations to .pdf files.
        """
        a = Graph(file)
        if self.size > 0:
            queue = ["[" + str(self.root.key) + "] " + str(self.root.value) + "(%d)" % self.root.balance_factor]
            self.visualize_helper(self.root, queue)
            for data in queue:
                a.node(data)
            a.edge(queue[0], queue[1])
            a.edge(queue[0], queue[2])
            a.edge(queue[1], queue[3])
            a.edge(queue[1], queue[4])
            a.edge(queue[3], queue[5])
            a.edge(queue[3], queue[6])
            a.edge(queue[2], queue[7])
            a.edge(queue[2], queue[8])
            a.render(view=True)
            a.render(filename="Before_delete_AVL_tree")
        else:
            print("Empty tree")

    def visualize_helper(self, node, queue):
        """
        make a level order traversal to avl tree.
        help to visualize_before and visualize_after methods.
        """
        if node is not None:
            if node.left_child is not None:
                temp = node.left_child
                queue.append("[" + str(temp.key) + "] " + str(temp.value) + "(%d)" % temp.balance_factor)
            if node.right_child is not None:
                temp = node.right_child
                queue.append("[" + str(temp.key) + "] " + str(temp.value) + "(%d)" % temp.balance_factor)
            self.visualize_helper(node.left_child, queue)
            self.visualize_helper(node.right_child, queue)


def main():
    # instance method
    mytree = AVLTree()

    # adding items
    mytree[9] = "CptS_450"
    mytree[8] = "CptS_415"
    mytree[7] = "CptS_315"
    mytree[6] = "CptS_215"
    mytree[5] = "CptS_132"
    mytree[4] = "CptS_131"
    mytree[3] = "CptS_122"
    mytree[2] = "CptS_121"
    mytree[1] = "CptS_115"

    # print level order traversal mytree
    mytree.level_order_traversal()
    # show visualization level order traversal mytree
    mytree.visualize_before("Before_delete_AVL_tree")

    # delete items
    mytree.delete(5)
    mytree.delete(6)

    # print level order traversal mytree after deleting
    mytree.level_order_traversal()
    # show visualization level order traversal mytree after deleting
    mytree.visualize_after("After_delete_AVL_tree")


if __name__ == '__main__':
    main()
