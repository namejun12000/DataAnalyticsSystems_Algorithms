###
# Participation - BST
# Author: Nam Jun Lee
# Date: November 1st, 2021
# Description: Tested with the provided Python test script file
###

from BST_Complete import BinarySearchTree


def main():
    mytree = BinarySearchTree()
    mytree[215] = "Data Structures and Algorithms"
    mytree[122] = "C/C++ Data Structures"
    mytree[132] = "Java Data Structures"
    mytree[315] = "Intro to Data Mining"
    mytree[415] = "Big Data"
    mytree[111] = "Intro to Programming"
    mytree[121] = "C Program Design"
    mytree[131] = "Java Program Design"

    print("Original Tree using in-order traversal:")
    mytree.in_order_traversal()

    print("\nOriginal Tree using pre-order traversal:")
    mytree.pre_order_traversal()

    print("\nOriginal Tree using post-order traversal:")
    mytree.post_order_traversal()

    # check duplicate key handling
    mytree[111] = "Intro to Computer Programming"
    print("\nTree after addition/update of node '111' - in-order traversal:")
    mytree.in_order_traversal()

    # check delete
    del mytree[415]
    print("\nTree after deletion of node '415' - in-order traversal:")
    mytree.in_order_traversal()

    # use of __iter__()
    print("\nTree node keys using iterator:")
    for node in mytree:
        print(node, end=", ")
    print()


if __name__ == "__main__":
    main()
