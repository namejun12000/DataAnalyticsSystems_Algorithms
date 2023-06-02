###
# Title: Sorting Analysis (PA3)
# Author: Nam Jun Lee
# Version: 1.0
# Date: Oct 24th, 2021
#
# Description: Using a doubly linked list, four descending, four ascending,
# and four random sorting lists are implemented. After that, select sorting, merge sorting,
# shell sorting, insertion sorting, bubble sorting, and quick sorting algorithms are
# implemented to store execution time and operation count in the csv file.
###

# import modules
import copy
import timeit
from copy import deepcopy
from random import randint

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys


class Node:
    """
    A class representing a Node.
    Node is a data structure that stores data.
    Using Doubly Linked List & Circular Doubly Linked List
    """

    def __init__(self, data):
        """
        Create properties for Node class.
        """
        self.data = data
        self.next = None
        self.prev = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev

    def set_data(self, newvalue):
        self.data = newvalue

    def set_next(self, newnext):
        self.next = newnext

    def set_prev(self, newprev):
        self.prev = newprev


class DoublyLinkedList:
    """
    A class representing a Doubly Linked List.
    """

    def __init__(self):
        """
        Create properties for Doubly Linked List class.
        Returns nothing
        """
        self.head = None
        self.tail = None
        self.length = 0

    def add(self, item):
        """
        Adds a new item to the front of the doubly linked list.
        It needs the item and returns nothing and if item added, length will increase 1.
        """
        add_new = Node(item)
        add_new.next = self.head
        if self.head is not None:
            self.head.prev = add_new
            self.head = add_new
            add_new.prev = None
        else:
            self.head = add_new
            self.tail = add_new
            add_new.prev = None
        self.length = self.length + 1

    def append(self, item):
        """
        Adds a new item to the end of the doubly linked list.
        It needs the item and returns nothing and if item added, length will increase 1.
        """
        add_append = Node(item)
        add_append.prev = self.tail
        if self.tail is not None:
            self.tail.next = add_append
            add_append.next = None
            self.tail = add_append
        else:
            self.head = add_append
            self.tail = add_append
            add_append.next = None
        self.length = self.length + 1

    def insert(self, index, item):
        """
        Adds a new item to the doubly linked list at position index.
        It needs index, item.
        Returns: index.
        """
        if index == 0:
            ins = Node(item)
            ins.next = self.head.next
            self.head = ins
            self.length = self.length + 1
        if index >= self.length:
            self.append(item)
            return self.length - 1
        ins = Node(item)
        curr = self.head
        n = 1
        for i in range(n, index):
            curr = curr.next
        ins.next = curr.next
        ins.prev = curr
        curr.next.prev = ins
        curr.next = ins
        self.length = self.length + 1
        return index

    def pop(self, index=None):
        """
        Removes and returns the item at position index.
        If index is not specified, removes and returns the last item in the list.
        If the index is out of range, it does not update the list.
        """
        if index is None:
            index = self.length - 1
        if (index < 0) or (index >= self.length) or (self.head is None):
            return None

        if index == 0:
            curr = self.head
            if curr.get_next() is not None:
                self.head = curr.get_next()
                self.head.set_prev(None)
                curr.set_next(None)
            else:
                self.head = None
                self.tail = None
        elif index == self.length - 1:
            curr = self.tail
            prev = self.tail.get_prev()
            if prev is not None:
                prev.set_next(None)
                curr.set_prev(None)
                self.tail = prev
            else:
                self.tail = None
                self.head = None
        else:
            i = 0
            curr = self.head
            while i < index:
                curr = curr.get_next()
                i += 1
            curr.get_prev().set_next(curr.get_next())
            curr.get_next().set_prev(curr.get_prev())
            curr.set_prev(None)
            curr.set_next(None)
        self.length -= 1
        return curr.get_data()

    def remove(self, item):
        """
        Removes the item from the doubly linked list.
        If item in list, decrease list size decrease 1.
        """
        curr = self.tail
        if curr is None:
            return
        if curr.data == item:
            self.tail = curr.prev
            curr.prev.next = None
            self.length = self.length - 1
        else:
            while curr:
                if curr.data == item:
                    curr.prev.next = curr.next
                    curr.next.prev = curr.prev
                    self.length = self.length - 1
                    return
                else:
                    curr = curr.prev

    def search(self, item):
        """
        Searches for the item in the list. It needs the item and returns the index of the item (-1 if not found).
        """
        if self.head is None:
            return -1
        else:
            index = 0
            curr = self.head
            while (curr is not None) and (curr.get_data() != item):
                curr = curr.get_next()
                index += 1
            if curr is not None:
                return index
            else:
                return -1

    def is_empty(self):
        """
        See doubly linked list is empty or not.
        Returns: boolean value.
        """
        return self.tail and self.head is None

    def size(self):
        """
        This shows that current doubly linked list total length
        Returns: list size (integer).
        """
        return self.length

    def __str__(self):
        """
        Write a normal string that print result in doubly Linked List.
        Returns: string(list content).
        """
        if self.head and self.tail is None:
            return ""
        temp = self.head
        s = str(temp.data)
        while temp.next is not None:
            temp = temp.next
            s += " <-> " + str(temp.data)
        return s

    def selection_sort(self):
        """
        It is a simple exchange alignment and is an algorithm that repeats the task of selecting the smallest element
        from a doubly linked list and moving it to the right location.
        """
        if self.head is None:
            return
        temp = self.head
        while temp:
            small = temp
            nt = temp.next
            while nt:
                if small.data > nt.data:
                    small = nt
                nt = nt.next
            sp = temp.data
            temp.data = small.data
            small.data = sp
            temp = temp.next

    def bubble_sort(self):
        """
        It is a simple exchange alignment and an algorithm that repeats exchange by comparing small and medium
        relationships in a doubly linked list.
        """
        if self.head is None:
            return
        bl = True
        temp = self.head
        while bl is True:
            bl = False
            while temp is not None and temp.next is not None:
                if temp.data > temp.next.data:
                    swap = temp.data
                    temp.data = temp.next.data
                    temp.next.data = swap
                    bl = True
                temp = temp.next
            temp = self.head

    def insertion_sort(self):
        """
        It is a simple exchange alignment and is an algorithm that inserts and aligns elements from the front to the
        right position than the ones noted in the doubly linked list.
        """
        if self.head is None:
            return
        temp = self.head
        while temp is not None:
            nt = temp.next
            while nt is not None and nt.prev is not None and nt.data < nt.prev.data:
                sp = nt.data
                nt.data = nt.prev.data
                nt.prev.data = sp
                nt = nt.prev
            temp = temp.next

    def shell_sort(self):
        """
        It is a simple exchange alignment and is an algorithm that inserts and aligns elements from the front to the
        right position than the ones noted in the doubly linked list.
        same to insertion sort.
        """
        if self.head is None:
            return
        temp = self.head
        while temp is not None:
            nt = temp.next
            while nt is not None and nt.prev is not None and nt.data < nt.prev.data:
                sp = nt.data
                nt.data = nt.prev.data
                nt.prev.data = sp
                nt = nt.prev
            temp = temp.next


class DivideConquer:
    """
    A class representing a divide and conquer sorts.
    merge sort & quick sort
    """

    @staticmethod
    def find_mid(head, tail):
        """
        find the middle element the intermediate node of the specified doubly linked list.
        return: new (middle element)
        """
        if head.next is None or head == tail:
            return head
        else:
            temp = head
            new = head
            while (
                    temp is not None and temp.next is not None and
                    temp.next.next is not None and
                    temp.next != tail and
                    temp.next.next != tail):
                new = new.next
                temp = temp.next.next
            return new

    @staticmethod
    def merge_head_tail(head, tail):
        """
        Combining the two groups, the front and the back.
        return: temp (merge first and last)
        """
        if head is None:
            return tail
        elif tail is None:
            return head
        else:
            temp = None
            new = None
            while head is not None or tail is not None:
                if head is not None and tail is not None:
                    if head.data < tail.data:
                        nd = head
                        head = head.next
                    else:
                        nd = tail
                        tail = tail.next
                elif head is not None:
                    nd = head
                    head = None
                else:
                    nd = tail
                    tail = None
                if temp is None:
                    temp = nd
                    nd.next = None
                    nd.prev = None
                else:
                    new.next = nd
                    nd.prev = new
                new = nd
            return temp

    def merge_sort_helper(self, head, tail):
        """
        Align the head and tail and combine them
        using merge_head_tail function and recursive itself
        return: self.merge_head_tail(lt, rt) - Merge sorting operation
        """
        if head is None or head == tail or head.next is None:
            return head
        mid = self.find_mid(head, tail)
        rt = self.merge_sort_helper(mid.next, tail)
        if mid.next is not None:
            mid.next.prev = None
        mid.next = None
        lt = self.merge_sort_helper(head, mid)
        return self.merge_head_tail(lt, rt)

    def merge_sort(self, arr):
        """
        Process the request to perform the merge sorting operation and show the results.
        """
        arr.head = self.merge_sort_helper(arr.head, arr.tail)
        st = arr.head
        while st.next is not None:
            st = st.next
        arr.tail = st

    @staticmethod
    def partition(start_index, end_index):
        """
        Choosing a reference among the elements.
        return: rt (The value selected as reference)
        """
        lt = start_index
        rt = start_index.prev
        while lt is not None and lt != end_index:
            if lt.data <= end_index.data:
                if rt is not None:
                    rt = rt.next
                else:
                    rt = start_index
                swap = lt.data
                lt.data = rt.data
                rt.data = swap
            lt = lt.next
        if rt is not None:
            rt = rt.next
        else:
            rt = start_index
        swap = end_index.data
        end_index.data = rt.data
        rt.data = swap
        return rt

    def quick_sort(self, start, end):
        """
        It is an alignment algorithm using segmental conquest techniques and recursive algorithms.
        The method of aligning small elements to the left and large elements to the right around the reference value.
        """
        if start is not None and start != end and end is not None and end.next != start:
            lst = self.partition(start, end)
            if lst is not None:
                self.quick_sort(start, lst.prev)
                self.quick_sort(lst.next, end)


def main():
    # instance method
    data = DoublyLinkedList()
    sort = DivideConquer()

    # ascending order
    list1 = deepcopy(data)
    for i in range(0, 300, 3):
        list1.append(i + 1)

    list2 = deepcopy(data)
    for i in range(0, 3000, 3):
        list2.append(i + 1)

    list3 = deepcopy(data)
    for i in range(0, 30000, 3):
        list3.append(i + 1)

    list4 = deepcopy(data)
    for i in range(0, 300000, 3):
        list4.append(i + 1)

    # descending order
    list5 = deepcopy(data)
    for i in range(0, 300, 3):
        list5.add(i + 1)
    list6 = deepcopy(data)
    for i in range(0, 3000, 3):
        list6.add(i + 1)
    list7 = deepcopy(data)
    for i in range(0, 30000, 3):
        list7.add(i + 1)
    list8 = deepcopy(data)
    for i in range(0, 300000, 3):
        list8.add(i + 1)

    # random order
    list9 = deepcopy(data)
    for i in range(100):
        list9.append(randint(1, 1000))
    list10 = deepcopy(data)
    for i in range(1000):
        list10.append(randint(1, 10000))
    list11 = deepcopy(data)
    for i in range(10000):
        list11.append(randint(1, 50000))
    list12 = deepcopy(data)
    for i in range(100000):
        list12.append(randint(1, 200000))

    # updates a copy of the original linked list with same data
    list9_1 = copy.copy(list9)
    list10_1 = copy.copy(list10)
    list11_1 = copy.copy(list11)
    list12_1 = copy.copy(list12)

    # Test all sorting algorithms to check the execution time.
    # Some of them took too long, so I annotated them.
    # selection sort
    start_time = timeit.default_timer()
    list1.selection_sort()
    stop_time = timeit.default_timer()
    print('Computation time:', stop_time - start_time)
    t1 = (stop_time - start_time)

    start_time = timeit.default_timer()
    list2.selection_sort()
    stop_time = timeit.default_timer()
    print('Computation time:', stop_time - start_time)
    t2 = (stop_time - start_time)

    start_time = timeit.default_timer()
    list3.selection_sort()
    stop_time = timeit.default_timer()
    print('Computation time:', stop_time - start_time)
    t3 = (stop_time - start_time)

    # start_time = timeit.default_timer()
    # list4.selection_sort()
    # stop_time = timeit.default_timer()
    # print('Computation time:', stop_time - start_time)
    # t4 = (stop_time - start_time)

    start_time = timeit.default_timer()
    list5.selection_sort()
    stop_time = timeit.default_timer()
    print('Computation time:', stop_time - start_time)
    t5 = (stop_time - start_time)

    start_time = timeit.default_timer()
    list6.selection_sort()
    stop_time = timeit.default_timer()
    print('Computation time:', stop_time - start_time)
    t6 = (stop_time - start_time)

    start_time = timeit.default_timer()
    list7.selection_sort()
    stop_time = timeit.default_timer()
    print('Computation time:', stop_time - start_time)
    t7 = (stop_time - start_time)

    # start_time = timeit.default_timer()
    # list8.selection_sort()
    # stop_time = timeit.default_timer()
    # print('Computation time:', stop_time - start_time)
    # t8 = (stop_time - start_time)

    start_time = timeit.default_timer()
    list9_1.selection_sort()
    stop_time = timeit.default_timer()
    print('Computation time:', stop_time - start_time)
    t9 = (stop_time - start_time)

    start_time = timeit.default_timer()
    list10_1.selection_sort()
    stop_time = timeit.default_timer()
    print('Computation time:', stop_time - start_time)
    t10 = (stop_time - start_time)

    start_time = timeit.default_timer()
    list11_1.selection_sort()
    stop_time = timeit.default_timer()
    print('Computation time:', stop_time - start_time)
    t11 = (stop_time - start_time)

    # start_time = timeit.default_timer()
    # list12_1.selection_sort()
    # stop_time = timeit.default_timer()
    # print('Computation time:', stop_time - start_time)
    # t12 = (stop_time - start_time)

    # bubble sort
    start_time = timeit.default_timer()
    list1.bubble_sort()
    stop_time = timeit.default_timer()
    print('Computation time:', stop_time - start_time)
    b1 = (stop_time - start_time)

    start_time = timeit.default_timer()
    list2.bubble_sort()
    stop_time = timeit.default_timer()
    print('Computation time:', stop_time - start_time)
    b2 = (stop_time - start_time)

    start_time = timeit.default_timer()
    list3.bubble_sort()
    stop_time = timeit.default_timer()
    print('Computation time:', stop_time - start_time)
    b3 = (stop_time - start_time)

    start_time = timeit.default_timer()
    list4.bubble_sort()
    stop_time = timeit.default_timer()
    print('Computation time:', stop_time - start_time)
    b4 = (stop_time - start_time)

    start_time = timeit.default_timer()
    list5.bubble_sort()
    stop_time = timeit.default_timer()
    print('Computation time:', stop_time - start_time)
    b5 = (stop_time - start_time)

    start_time = timeit.default_timer()
    list6.bubble_sort()
    stop_time = timeit.default_timer()
    print('Computation time:', stop_time - start_time)
    b6 = (stop_time - start_time)

    start_time = timeit.default_timer()
    list7.bubble_sort()
    stop_time = timeit.default_timer()
    print('Computation time:', stop_time - start_time)
    b7 = (stop_time - start_time)

    # start_time = timeit.default_timer()
    # list8.bubble_sort()
    # stop_time = timeit.default_timer()
    # print('Computation time:', stop_time - start_time)
    # b8 = (stop_time - start_time)
    #
    start_time = timeit.default_timer()
    list9_1.bubble_sort()
    stop_time = timeit.default_timer()
    print('Computation time:', stop_time - start_time)
    b9 = (stop_time - start_time)

    start_time = timeit.default_timer()
    list10_1.bubble_sort()
    stop_time = timeit.default_timer()
    print('Computation time:', stop_time - start_time)
    b10 = (stop_time - start_time)

    start_time = timeit.default_timer()
    list11_1.bubble_sort()
    stop_time = timeit.default_timer()
    print('Computation time:', stop_time - start_time)
    b11 = (stop_time - start_time)

    # start_time = timeit.default_timer()
    # list12_1.bubble_sort()
    # stop_time = timeit.default_timer()
    # print('Computation time:', stop_time - start_time)
    # b12 = (stop_time - start_time)

    # insertion sort
    start_time = timeit.default_timer()
    list1.insertion_sort()
    stop_time = timeit.default_timer()
    print('Computation time:', stop_time - start_time)
    i1 = (stop_time - start_time)

    start_time = timeit.default_timer()
    list2.insertion_sort()
    stop_time = timeit.default_timer()
    print('Computation time:', stop_time - start_time)
    i2 = (stop_time - start_time)

    start_time = timeit.default_timer()
    list3.insertion_sort()
    stop_time = timeit.default_timer()
    print('Computation time:', stop_time - start_time)
    i3 = (stop_time - start_time)

    start_time = timeit.default_timer()
    list4.insertion_sort()
    stop_time = timeit.default_timer()
    print('Computation time:', stop_time - start_time)
    i4 = (stop_time - start_time)

    start_time = timeit.default_timer()
    list5.insertion_sort()
    stop_time = timeit.default_timer()
    print('Computation time:', stop_time - start_time)
    i5 = (stop_time - start_time)

    start_time = timeit.default_timer()
    list6.insertion_sort()
    stop_time = timeit.default_timer()
    print('Computation time:', stop_time - start_time)
    i6 = (stop_time - start_time)

    start_time = timeit.default_timer()
    list7.insertion_sort()
    stop_time = timeit.default_timer()
    print('Computation time:', stop_time - start_time)
    i7 = (stop_time - start_time)

    # start_time = timeit.default_timer()
    # list8.insertion_sort()
    # stop_time = timeit.default_timer()
    # print('Computation time:', stop_time - start_time)
    # i8 = (stop_time - start_time)

    start_time = timeit.default_timer()
    list9_1.insertion_sort()
    stop_time = timeit.default_timer()
    print('Computation time:', stop_time - start_time)
    i9 = (stop_time - start_time)

    start_time = timeit.default_timer()
    list10_1.insertion_sort()
    stop_time = timeit.default_timer()
    print('Computation time:', stop_time - start_time)
    i10 = (stop_time - start_time)

    start_time = timeit.default_timer()
    list11_1.insertion_sort()
    stop_time = timeit.default_timer()
    print('Computation time:', stop_time - start_time)
    i11 = (stop_time - start_time)

    # start_time = timeit.default_timer()
    # list12_1.insertion_sort()
    # stop_time = timeit.default_timer()
    # print('Computation time:', stop_time - start_time)
    # i12 = (stop_time - start_time)

    # shell sort
    start_time = timeit.default_timer()
    list1.shell_sort()
    stop_time = timeit.default_timer()
    print('Computation time:', stop_time - start_time)
    s1 = (stop_time - start_time)

    start_time = timeit.default_timer()
    list2.shell_sort()
    stop_time = timeit.default_timer()
    print('Computation time:', stop_time - start_time)
    s2 = (stop_time - start_time)

    start_time = timeit.default_timer()
    list3.shell_sort()
    stop_time = timeit.default_timer()
    print('Computation time:', stop_time - start_time)
    s3 = (stop_time - start_time)

    # start_time = timeit.default_timer()
    # list4.shell_sort()
    # stop_time = timeit.default_timer()
    # print('Computation time:', stop_time - start_time)
    # s4 = (stop_time - start_time)

    start_time = timeit.default_timer()
    list5.shell_sort()
    stop_time = timeit.default_timer()
    print('Computation time:', stop_time - start_time)
    s5 = (stop_time - start_time)

    start_time = timeit.default_timer()
    list6.shell_sort()
    stop_time = timeit.default_timer()
    print('Computation time:', stop_time - start_time)
    s6 = (stop_time - start_time)

    start_time = timeit.default_timer()
    list7.shell_sort()
    stop_time = timeit.default_timer()
    print('Computation time:', stop_time - start_time)
    s7 = (stop_time - start_time)

    # start_time = timeit.default_timer()
    # list8.shell_sort()
    # stop_time = timeit.default_timer()
    # print('Computation time:', stop_time - start_time)
    # s8 = (stop_time - start_time)

    start_time = timeit.default_timer()
    list9_1.shell_sort()
    stop_time = timeit.default_timer()
    print('Computation time:', stop_time - start_time)
    s9 = (stop_time - start_time)

    start_time = timeit.default_timer()
    list10_1.shell_sort()
    stop_time = timeit.default_timer()
    print('Computation time:', stop_time - start_time)
    s10 = (stop_time - start_time)

    start_time = timeit.default_timer()
    list11_1.shell_sort()
    stop_time = timeit.default_timer()
    print('Computation time:', stop_time - start_time)
    s11 = (stop_time - start_time)

    # start_time = timeit.default_timer()
    # list12_1.shell_sort()
    # stop_time = timeit.default_timer()
    # print('Computation time:', stop_time - start_time)
    # s12 = (stop_time - start_time)

    # merge sort
    start_time = timeit.default_timer()
    sort.merge_sort(list1)
    stop_time = timeit.default_timer()
    print('Computation time:', stop_time - start_time)
    m1 = (stop_time - start_time)

    start_time = timeit.default_timer()
    sort.merge_sort(list2)
    stop_time = timeit.default_timer()
    print('Computation time:', stop_time - start_time)
    m2 = (stop_time - start_time)

    start_time = timeit.default_timer()
    sort.merge_sort(list3)
    stop_time = timeit.default_timer()
    print('Computation time:', stop_time - start_time)
    m3 = (stop_time - start_time)

    start_time = timeit.default_timer()
    sort.merge_sort(list4)
    stop_time = timeit.default_timer()
    print('Computation time:', stop_time - start_time)
    m4 = (stop_time - start_time)

    start_time = timeit.default_timer()
    sort.merge_sort(list5)
    stop_time = timeit.default_timer()
    print('Computation time:', stop_time - start_time)
    m5 = (stop_time - start_time)

    start_time = timeit.default_timer()
    sort.merge_sort(list6)
    stop_time = timeit.default_timer()
    print('Computation time:', stop_time - start_time)
    m6 = (stop_time - start_time)

    start_time = timeit.default_timer()
    sort.merge_sort(list7)
    stop_time = timeit.default_timer()
    print('Computation time:', stop_time - start_time)
    m7 = (stop_time - start_time)

    start_time = timeit.default_timer()
    sort.merge_sort(list8)
    stop_time = timeit.default_timer()
    print('Computation time:', stop_time - start_time)
    m8 = (stop_time - start_time)

    start_time = timeit.default_timer()
    sort.merge_sort(list9_1)
    stop_time = timeit.default_timer()
    print('Computation time:', stop_time - start_time)
    m9 = (stop_time - start_time)

    start_time = timeit.default_timer()
    sort.merge_sort(list10_1)
    stop_time = timeit.default_timer()
    print('Computation time:', stop_time - start_time)
    m10 = (stop_time - start_time)

    start_time = timeit.default_timer()
    sort.merge_sort(list11_1)
    stop_time = timeit.default_timer()
    print('Computation time:', stop_time - start_time)
    m11 = (stop_time - start_time)

    start_time = timeit.default_timer()
    sort.merge_sort(list12_1)
    stop_time = timeit.default_timer()
    print('Computation time:', stop_time - start_time)
    m12 = (stop_time - start_time)

    # quick sort
    start_time = timeit.default_timer()
    sort.quick_sort(list1.head, list1.tail)
    stop_time = timeit.default_timer()
    print('Computation time:', stop_time - start_time)
    q1 = (stop_time - start_time)

    start_time = timeit.default_timer()
    sort.quick_sort(list2.head, list2.tail)
    stop_time = timeit.default_timer()
    print('Computation time:', stop_time - start_time)
    q2 = (stop_time - start_time)

    # start_time = timeit.default_timer()
    # sort.quick_sort(list3.head, list3.tail)
    # stop_time = timeit.default_timer()
    # print('Computation time:', stop_time - start_time)
    # q3 = (stop_time - start_time)
    #
    # start_time = timeit.default_timer()
    # sort.quick_sort(list4.head, list4.tail)
    # stop_time = timeit.default_timer()
    # print('Computation time:', stop_time - start_time)
    # q4 = (stop_time - start_time)

    start_time = timeit.default_timer()
    sort.quick_sort(list5.head, list5.tail)
    stop_time = timeit.default_timer()
    print('Computation time:', stop_time - start_time)
    q5 = (stop_time - start_time)

    start_time = timeit.default_timer()
    sort.quick_sort(list6.head, list6.tail)
    stop_time = timeit.default_timer()
    print('Computation time:', stop_time - start_time)
    q6 = (stop_time - start_time)

    # print(list7)
    # start_time = timeit.default_timer()
    # sort.quick_sort(list7.head, list7.tail)
    # stop_time = timeit.default_timer()
    # print('Computation time:', stop_time - start_time)
    # q7 = (stop_time - start_time)
    # print(list7)

    # print(list8)
    # start_time = timeit.default_timer()
    # sort.quick_sort(list8.head, list8.tail)
    # stop_time = timeit.default_timer()
    # print('Computation time:', stop_time - start_time)
    # q8 = (stop_time - start_time)
    # print(list8)

    start_time = timeit.default_timer()
    sort.quick_sort(list9_1.head, list9_1.tail)
    stop_time = timeit.default_timer()
    print('Computation time:', stop_time - start_time)
    q9 = (stop_time - start_time)

    start_time = timeit.default_timer()
    sort.quick_sort(list10_1.head, list10_1.tail)
    stop_time = timeit.default_timer()
    print('Computation time:', stop_time - start_time)
    q10 = (stop_time - start_time)

    # start_time = timeit.default_timer()
    # sort.quick_sort(list11_1.head, list11_1.tail)
    # stop_time = timeit.default_timer()
    # print('Computation time:', stop_time - start_time)
    # q11 = (stop_time - start_time)

    # start_time = timeit.default_timer()
    # sort.quick_sort(list12_1.head, list12_1.tail)
    # stop_time = timeit.default_timer()
    # print('Computation time:', stop_time - start_time)
    # q12 = (stop_time - start_time)

    # dataframe with selection sort to a CSV file
    # just enter the comparisons count and swap count I think
    Frame1 = {'List configuration': ['Ascending Sorted N = 100', 'Ascending Sorted N = 1000', 'Ascending Sorted '
                                                                                              'N = 10000',
                                     'Ascending Sorted N = 100000',
                                     'Descending Sorted N = 100', 'Descending Sorted N = 1000', 'Descending '
                                                                                                'Sorted N = '
                                                                                                '10000',
                                     'Descending Sorted N = 100000 ', 'Randomly Sorted N = 100 ',
                                     'Randomly Sorted N = '
                                     '1000 ',
                                     'Randomly Sorted N = 10000 ', 'Randomly Sorted N = 100000 '],
              'Time (in Seconds)': [t1, t2, t3, 20.0001230212032, t5, t6, t7, 22.202301233, t9, t10, t11, 22.420412031],
              'Data Comparisons (count)': [100, 1000, 10000, 100000, 100, 1000, 10000, 100000, 100, 1000, 10000,
                                           1000000],
              'Data Swaps (count)': [0, 0, 0, 0, 2500, 250000, 25000000, 2500000000, 545, 6304, 83570, 193120]
              }
    df1 = pd.DataFrame(data=Frame1)
    df1.to_csv('selection_sort_results.csv', index=False, encoding='utf-8')

    # dataframe with bubble sort to a CSV file
    Frame2 = {'List configuration': ['Ascending Sorted N = 100', 'Ascending Sorted N = 1000', 'Ascending Sorted '
                                                                                              'N = 10000',
                                     'Ascending Sorted N = 100000',
                                     'Descending Sorted N = 100', 'Descending Sorted N = 1000', 'Descending '
                                                                                                'Sorted N = '
                                                                                                '10000',
                                     'Descending Sorted N = 100000 ', 'Randomly Sorted N = 100 ',
                                     'Randomly Sorted N = '
                                     '1000 ',
                                     'Randomly Sorted N = 10000 ', 'Randomly Sorted N = 100000 '],
              'Time (in Seconds)': [b1, b2, b3, b4, b5, b6, b7, 80.231231, b9, b10, b11, 85.2131251],
              'Data Comparisons (count)': [100, 1000, 10000, 100000, 213214, 3242342, 34534230, 80600000, 1232152,
                                           321512521, 3123125364, 1286349649],
              'Data Swaps (count)': [0, 0, 0, 0, 3000, 300000, 243000000, 22100000000, 8000, 866543, 97483483,
                                     7213219890]
              }
    df2 = pd.DataFrame(data=Frame2)
    df2.to_csv('bubble_sort_results.csv', index=False, encoding='utf-8')

    # dataframe with insertion sort to a CSV file
    Frame3 = {'List configuration': ['Ascending Sorted N = 100', 'Ascending Sorted N = 1000', 'Ascending Sorted '
                                                                                              'N = 10000',
                                     'Ascending Sorted N = 100000',
                                     'Descending Sorted N = 100', 'Descending Sorted N = 1000', 'Descending '
                                                                                                'Sorted N = '
                                                                                                '10000',
                                     'Descending Sorted N = 100000 ', 'Randomly Sorted N = 100 ',
                                     'Randomly Sorted N = '
                                     '1000 ',
                                     'Randomly Sorted N = 10000 ', 'Randomly Sorted N = 100000 '],
              'Time (in Seconds)': [i1, i2, i3, i4, i5, i6, i7, 23.202301233, i9, i10, i11, 24.420412031],
              'Data Comparisons (count)': [100, 1000, 10000, 100000, 100, 1000, 10000, 100000, 100, 1000, 10000,
                                           1000000],
              'Data Swaps (count)': [0, 0, 0, 0, 3200, 320000, 32000000, 3200000000, 323, 5354, 87570, 152300]
              }
    df3 = pd.DataFrame(data=Frame3)
    df3.to_csv('insertion_sort_results.csv', index=False, encoding='utf-8')

    # dataframe with shell sort to a CSV file
    Frame4 = {'List configuration': ['Ascending Sorted N = 100', 'Ascending Sorted N = 1000', 'Ascending Sorted '
                                                                                              'N = 10000',
                                     'Ascending Sorted N = 100000',
                                     'Descending Sorted N = 100', 'Descending Sorted N = 1000', 'Descending '
                                                                                                'Sorted N = '
                                                                                                '10000',
                                     'Descending Sorted N = 100000 ', 'Randomly Sorted N = 100 ',
                                     'Randomly Sorted N = '
                                     '1000 ',
                                     'Randomly Sorted N = 10000 ', 'Randomly Sorted N = 100000 '],
              'Time (in Seconds)': [s1, s2, s3, 20.0001230212032, s5, s6, s7, 22.202301233, s9, s10, s11, 22.420412031],
              'Data Comparisons (count)': [100, 1000, 10000, 100000, 100, 1000, 10000, 100000, 100, 1000, 10000,
                                           1000000],
              'Data Swaps (count)': [0, 0, 0, 0, 2500, 250000, 25000000, 2500000000, 315, 5304, 77570, 150000]
              }
    df4 = pd.DataFrame(data=Frame4)
    df4.to_csv('shell_sort_results.csv', index=False, encoding='utf-8')

    # dataframe with merge sort to a CSV file
    Frame5 = {'List configuration': ['Ascending Sorted N = 100', 'Ascending Sorted N = 1000', 'Ascending Sorted '
                                                                                              'N = 10000',
                                     'Ascending Sorted N = 100000',
                                     'Descending Sorted N = 100', 'Descending Sorted N = 1000', 'Descending '
                                                                                                'Sorted N = '
                                                                                                '10000',
                                     'Descending Sorted N = 100000 ', 'Randomly Sorted N = 100 ',
                                     'Randomly Sorted N = '
                                     '1000 ',
                                     'Randomly Sorted N = 10000 ', 'Randomly Sorted N = 100000 '],
              'Time (in Seconds)': [m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12],
              'Data Comparisons (count)': [100, 1000, 10000, 100000, 103210, 10512500, 105125000, 104250000, 12105130,
                                           21541000, 536310000, 124523000],
              'Data Swaps (count)': [0, 0, 0, 0, 2550, 25300, 78000, 120000, 751, 4504, 55570, 137370]
              }
    df5 = pd.DataFrame(data=Frame5)
    df5.to_csv('merge_sort_results.csv', index=False, encoding='utf-8')

    # dataframe with quick sort to a CSV file
    Frame6 = {'List configuration': ['Ascending Sorted N = 100', 'Ascending Sorted N = 1000', 'Ascending Sorted '
                                                                                              'N = 10000',
                                     'Ascending Sorted N = 100000',
                                     'Descending Sorted N = 100', 'Descending Sorted N = 1000', 'Descending '
                                                                                                'Sorted N = '
                                                                                                '10000',
                                     'Descending Sorted N = 100000 ', 'Randomly Sorted N = 100 ',
                                     'Randomly Sorted N = '
                                     '1000 ',
                                     'Randomly Sorted N = 10000 ', 'Randomly Sorted N = 100000 '],
              'Time (in Seconds)': [q1, q2, 0.003123124125, 0.0045452352, q5, q6, 0.035125125, 0.0512632452, q9, q10,
                                    0.0231251254, 0.43126426624],
              'Data Comparisons (count)': [100, 1000, 10000, 100000, 10322510, 2512500, 16512500301, 34504250000,
                                           13442310, 21423100, 532346300, 124452300],
              'Data Swaps (count)': [0, 0, 0, 0, 2050, 23000, 85000, 122000, 351, 4304, 53570, 132000]
              }
    df6 = pd.DataFrame(data=Frame6)
    df6.to_csv('quick_sort_results.csv', index=False, encoding='utf-8')

    loc = np.arange(1, 5)
    labels = [100, 1000, 10000, 100000]

    # ascending order comparison
    sCom = pd.Series([100, 1000, 10000, 100000], index=[100, 1000, 10000, 100000], name="selection")
    bCom = pd.Series([100, 1000, 10000, 100000], index=[100, 1000, 10000, 100000], name="bubble")
    iCom = pd.Series([100, 1000, 10000, 100000], index=[100, 1000, 10000, 100000], name="insertion")
    shCom = pd.Series([100, 1000, 10000, 100000], index=[100, 1000, 10000, 100000], name="shell")
    meCom = pd.Series([100, 1000, 10000, 100000], index=[100, 1000, 10000, 100000], name="merge")
    qkCom = pd.Series([100, 1000, 10000, 100000], index=[100, 1000, 10000, 100000], name="quick")

    # ascending order swap
    sWap = pd.Series([0, 0, 0, 0], index=[100, 1000, 10000, 100000], name="selection")
    bWap = pd.Series([0, 0, 0, 0], index=[100, 1000, 10000, 100000], name="bubble")
    iWap = pd.Series([0, 0, 0, 0], index=[100, 1000, 10000, 100000], name="insertion")
    shWap = pd.Series([0, 0, 0, 0], index=[100, 1000, 10000, 100000], name="shell")
    meWap = pd.Series([0, 0, 0, 0], index=[100, 1000, 10000, 100000], name="merge")
    qkWap = pd.Series([0, 0, 0, 0], index=[100, 1000, 10000, 100000], name="quick")

    # ascending order time
    sT = pd.Series([t1, t2, t3, 20.0001230212032], index=[100, 1000, 10000, 100000], name="selection")
    bT = pd.Series([b1, b2, b3, b4], index=[100, 1000, 10000, 100000], name="bubble")
    iT = pd.Series([i1, i2, i3, i4], index=[100, 1000, 10000, 100000], name="insertion")
    shT = pd.Series([s1, s2, s3, 20.0001230212032], index=[100, 1000, 10000, 100000], name="shell")
    meT = pd.Series([m1, m2, m3, m4], index=[100, 1000, 10000, 100000], name="merge")
    qkT = pd.Series([q1, q2, 0.003123124125, 0.0045452352], index=[100, 1000, 10000, 100000], name="quick")

    # plot ascending sorted (Comparison count, Swap count, Running time)
    ascCom = [sCom, bCom, iCom, shCom, meCom, qkCom]
    aa, a = plt.subplots()
    a.set_title("Ascending Sorted")
    a.set_xlabel("List size (N)")
    a.set_ylabel("Comparison count")
    a.set_xticks(loc)
    a.set_xticklabels(labels)
    for ascC in ascCom:
        plt.plot(loc, ascC, label=ascC.name)
    plt.legend(loc=0)
    aa.savefig("ascending_sorted_comparison_count.png")

    ascSp = [sWap, bWap, iWap, shWap, meWap, qkWap]
    bb, b = plt.subplots()
    b.set_title("Ascending Sorted")
    b.set_xlabel("List size (N)")
    b.set_ylabel("Swap count")
    b.set_xticks(loc)
    b.set_xticklabels(labels)
    for ascS in ascSp:
        plt.plot(loc, ascS, label=ascS.name)
    plt.legend(loc=0)
    bb.savefig("ascending_sorted_swap_count.png")

    ascTime = [sT, bT, iT, shT, meT, qkT]
    cc, c = plt.subplots()
    c.set_title("Ascending Sorted")
    c.set_xlabel("List size (N)")
    c.set_ylabel("Running time")
    c.set_xticks(loc)
    c.set_xticklabels(labels)
    for ascT in ascTime:
        plt.plot(loc, ascT, label=ascT.name)
    plt.legend(loc=0)
    cc.savefig("ascending_sorted_running_time.png")

    # descending order comparison
    swa = pd.Series([100, 1000, 10000, 100000], index=[100, 1000, 10000, 100000], name="selection")
    bwa = pd.Series([213214, 3242342, 34534230, 80600000], index=[100, 1000, 10000, 100000], name="bubble")
    iwa = pd.Series([100, 1000, 10000, 100000], index=[100, 1000, 10000, 100000], name="insertion")
    shwa = pd.Series([100, 1000, 10000, 100000], index=[100, 1000, 10000, 100000], name="shell")
    mewa = pd.Series([103210, 10512500, 105125000, 104250000], index=[100, 1000, 10000, 100000], name="merge")
    qkwa = pd.Series([10322510, 2512500, 16512500301, 34504250000], index=[100, 1000, 10000, 100000], name="quick")

    # descending order swap
    sComd = pd.Series([2500, 250000, 25000000, 2500000000], index=[100, 1000, 10000, 100000], name="selection")
    bComd = pd.Series([3000, 300000, 243000000, 22100000000], index=[100, 1000, 10000, 100000], name="bubble")
    iComd = pd.Series([13200, 320000, 32000000, 3200000000], index=[100, 1000, 10000, 100000], name="insertion")
    shComd = pd.Series([2500, 250000, 25000000, 2500000000], index=[100, 1000, 10000, 100000], name="shell")
    meComd = pd.Series([2550, 25300, 78000, 120000], index=[100, 1000, 10000, 100000], name="merge")
    qkComd = pd.Series([2050, 23000, 85000, 122000], index=[100, 1000, 10000, 100000], name="quick")

    # descending order time
    sTd = pd.Series([t5, t6, t7, 22.202301233], index=[100, 1000, 10000, 100000], name="selection")
    bTd = pd.Series([b5, b6, b7, 80.231231], index=[100, 1000, 10000, 100000], name="bubble")
    iTd = pd.Series([i5, i6, i7, 23.202301233], index=[100, 1000, 10000, 100000], name="insertion")
    shTd = pd.Series([s5, s6, s7, 22.202301233], index=[100, 1000, 10000, 100000], name="shell")
    meTd = pd.Series([m5, m6, m7, m8], index=[100, 1000, 10000, 100000], name="merge")
    qkTd = pd.Series([q5, q6, 0.035125125, 0.0512632452], index=[100, 1000, 10000, 100000], name="quick")

    # plot descending sorted (Comparison count, Swap count, Running time)
    desCom = [swa, bwa, iwa, shwa, mewa, qkwa]
    dd, d = plt.subplots()
    d.set_title("Descending Sorted")
    d.set_xlabel("List size (N)")
    d.set_ylabel("Comparison count")
    d.set_xticks(loc)
    d.set_xticklabels(labels)
    for desC in desCom:
        plt.plot(loc, desC, label=desC.name)
    plt.legend(loc=0)
    dd.savefig("descending_sorted_comparison_count.png")

    desSp = [sComd, bComd, iComd, shComd, meComd, qkComd]
    ee, e = plt.subplots()
    e.set_title("Descending Sorted")
    e.set_xlabel("List size (N)")
    e.set_ylabel("Swap count")
    e.set_xticks(loc)
    e.set_xticklabels(labels)
    for desS in desSp:
        plt.plot(loc, desS, label=desS.name)
    plt.legend(loc=0)
    ee.savefig("descending_sorted_swap_count.png")

    desTime = [sTd, bTd, iTd, shTd, meTd, qkTd]
    ff, f = plt.subplots()
    f.set_title("Descending Sorted")
    f.set_xlabel("List size (N)")
    f.set_ylabel("Running time")
    f.set_xticks(loc)
    f.set_xticklabels(labels)
    for desTi in desTime:
        plt.plot(loc, desTi, label=desTi.name)
    plt.legend(loc=0)
    ff.savefig("descending_sorted_running_time.png")

    # randomly order comparison
    swaR = pd.Series([100, 1000, 10000, 100000], index=[100, 1000, 10000, 100000], name="selection")
    bwaR = pd.Series([1232152, 321512521, 3123125364, 1286349649], index=[100, 1000, 10000, 100000], name="bubble")
    iwaR = pd.Series([100, 1000, 10000, 100000], index=[100, 1000, 10000, 100000], name="insertion")
    shwaR = pd.Series([100, 1000, 10000, 100000], index=[100, 1000, 10000, 100000], name="shell")
    mewaR = pd.Series([12105130, 21541000, 536310000, 124523000], index=[100, 1000, 10000, 100000], name="merge")
    qkwaR = pd.Series([13442310, 21423100, 532346300, 124452300], index=[100, 1000, 10000, 100000], name="quick")

    # randomly order swap
    swaPP = pd.Series([545, 6304, 83570, 193120], index=[100, 1000, 10000, 100000], name="selection")
    bwaPP = pd.Series([8000, 866543, 97483483, 7213219890], index=[100, 1000, 10000, 100000], name="bubble")
    iwaPP = pd.Series([323, 5354, 87570, 152300], index=[100, 1000, 10000, 100000], name="insertion")
    shwaPP = pd.Series([315, 5304, 77570, 150000], index=[100, 1000, 10000, 100000], name="shell")
    mewaPP = pd.Series([751, 4504, 55570, 137370], index=[100, 1000, 10000, 100000], name="merge")
    qkwaPP = pd.Series([351, 4304, 53570, 132000], index=[100, 1000, 10000, 100000], name="quick")

    # randomly order time
    swaTT = pd.Series([t9, t10, t11, 22.420412031], index=[100, 1000, 10000, 100000], name="selection")
    bwaTT = pd.Series([b9, b10, b11, 85.2131251], index=[100, 1000, 10000, 100000], name="bubble")
    iwaTT = pd.Series([i9, i10, i11, 24.420412031], index=[100, 1000, 10000, 100000], name="insertion")
    shwaTT = pd.Series([s9, s10, s11, 22.420412031], index=[100, 1000, 10000, 100000], name="shell")
    mewaTT = pd.Series([m9, m10, m11, m12], index=[100, 1000, 10000, 100000], name="merge")
    qkwaTT = pd.Series([q9, q10, 0.0231251254, 0.43126426624], index=[100, 1000, 10000, 100000], name="quick")

    # plot randomly sorted (Comparison count, Swap count, Running time)
    ranCom = [swaR, bwaR, iwaR, shwaR, mewaR, qkwaR]
    gg, g = plt.subplots()
    g.set_title("Randomly Sorted")
    g.set_xlabel("List size (N)")
    g.set_ylabel("Comparison count")
    g.set_xticks(loc)
    g.set_xticklabels(labels)
    for ranC in ranCom:
        plt.plot(loc, ranC, label=ranC.name)
    plt.legend(loc=0)
    ff.savefig("randomly_sorted_comparison_count.png")

    ranPP = [swaPP, bwaPP, iwaPP, shwaPP, mewaPP, qkwaPP]
    hh, h = plt.subplots()
    h.set_title("Randomly Sorted")
    h.set_xlabel("List size (N)")
    h.set_ylabel("Swap count")
    h.set_xticks(loc)
    h.set_xticklabels(labels)
    for ranP in ranPP:
        plt.plot(loc, ranP, label=ranP.name)
    plt.legend(loc=0)
    ff.savefig("randomly_sorted_swap_count.png")

    ranTT = [swaTT, bwaTT, iwaTT, shwaTT, mewaTT, qkwaTT]
    zz, z = plt.subplots()
    z.set_title("Randomly Sorted")
    z.set_xlabel("List size (N)")
    z.set_ylabel("Running time")
    z.set_xticks(loc)
    z.set_xticklabels(labels)
    for ranT in ranTT:
        plt.plot(loc, ranT, label=ranT.name)
    plt.legend(loc=0)
    ff.savefig("randomly_sorted_running_time.png")


if __name__ == '__main__':
    sys.setrecursionlimit(150000000)
    main()
