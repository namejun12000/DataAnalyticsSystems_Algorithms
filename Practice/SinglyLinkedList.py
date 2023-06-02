###
# Singly Linked List
# Author: Nam Jun Lee
# Date: Sept 30th, 2021
###

# Node class
class Node:
    # initialization method.
    def __init__(self, data):
        self.data = data
        self.next = None


# LinkedList class
class LinkedList:
    # initialization method.
    def __init__(self):
        self.head = Node(None)
        self.length = 0

    # add new item to list (front)
    def add(self, item):
        temp = Node(item)
        temp.next = self.head
        self.head = temp
        self.length = self.length + 1

    # append new item to list (back)
    def append(self, item):
        if self.head is None:
            self.head = Node(item)
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = Node(item)
        self.length = self.length + 1

    # add a new item to list at position index
    def insert(self, index, item):
        if self.head is None:
            self.head = item
        elif index == 0:
            self.add(item)
        else:
            curr = self.head
            i = 1
            while (curr.next is not None) and (i < index):
                curr = curr.next
                i += 1
            temp = Node(item)
            temp.next = curr.next
            curr.next = temp
        self.length = self.length + 1

    # Remove item at position index
    def pop(self, index=None):
        if index is None:
            index = self.length + 1

        if self.head is None:
            return None
        elif index == 0:
            curr = self.head
            self.head = curr.next
            curr.next = None
            self.length = self.length - 1
            return curr.data
        else:
            prev = self.head
            i = 1
            while (prev.next is not None) and (i < index):
                prev = prev.next
                i = i + 1
            temp = prev.next
            prev.next = temp.next
            temp.next = None
            self.length = self.length - 1
            return temp.data

    # remove item from the list
    def remove(self, item):
        temp = self.head
        prev = None
        while temp is not None:
            if temp.data == item:
                break
            else:
                prev = temp
                temp = temp.next
        if prev is None:
            self.head = temp.next
        else:
            prev.next = temp.next
        self.length = self.length - 1

    # search item's position index in list
    def search(self, item):
        curr = self.head
        for i in range(self.length):
            if item in curr.data:
                return i
            i += 1
            curr = curr.next
        return -1

    # list is empty or not
    def is_empty(self):
        return self.head is None

    # current list size
    def size(self):
        return self.length

    # Write a normal string that print result.
    def __str__(self):
        if self.head is None:
            return ""
        temp = self.head
        s = str(temp.data)
        while temp.next is not None:
            temp = temp.next
            s += ", " + str(temp.data)
        return s


def main():
    # main program to prompt
    # instance of LinkedList class in practice
    practice = LinkedList()
    # add items in list
    practice.add("Apple")
    practice.add('Banana')
    practice.add('Orange')
    practice.add('Cucumber')
    practice.add('Rice')
    # print result
    print(practice)
    # search items
    print("Search idx of Banana:", practice.search("Banana"))
    print("Search idx of Cucumber:", practice.search("Cucumber"))
    # remove item and print result
    print("Remove Orange in list")
    practice.remove('Orange')
    print(practice)
    # current size of list
    print("Size of list:", practice.size())
    # insert item at position index
    print("Insert idx[2] in Coke")
    practice.insert(2, 'Coke')
    print(practice)


if __name__ == '__main__':
    main()
