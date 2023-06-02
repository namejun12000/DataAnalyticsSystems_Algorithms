###
# Title: Linked Lists (PA2)
# Author: Nam Jun Lee
# Version: 1.0
# Date: Oct 9st, 2021
#
# Description: This program computes Doubly Linked List and Circular Doubly Linked List
###

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

    def pop(self, index):
        """
        Remove item at position index in doubly linked list.
        If index is not selected than removes last item in list.
        Decrease list size 1.
        """
        if index is None:
            index = self.size() - 1
        if index == (self.length - 1):
            self.tail = self.tail.prev
            self.tail.next = None
            self.length = self.length - 1
            return
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            self.length = self.length - 1
            return
        pop_in = self.head
        for i in range(index):
            pop_in = pop_in.next
        pop_in.prev.next = pop_in.next
        pop_in.next.prev = pop_in.prev
        self.length = self.length - 1
        return

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
        Search item in doubly linked list.
        If item in list, return item index number
        else, return -1.
        """
        if self.head is None:
            return False
        st_point = self.head
        for i in range(self.length):
            if st_point.data == item:
                return i
            else:
                st_point = st_point.next
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


class CircularDoublyLinkedList:
    """
    A class representing a Circular Doubly Linked List.
    """

    def __init__(self):
        """
        Create properties for Circular Doubly Linked List class.
        Returns nothing.
        """
        self.head = None
        self.length = 0

    def add(self, item):
        """
        Adds a new item to the front of the circular doubly linked list.
        It needs the item and returns nothing.
        If list is empty then add item in list.
        If item added, length will increase 1.
        """
        if self.is_empty():
            self.head = Node(item)
        else:
            temp = Node(item)
            if self.length == 1:
                add_temp = self.head
            else:
                add_temp = self.head.prev
            add_temp.next = temp
            temp.prev = add_temp
            self.head.prev = temp
            temp.next = self.head
            self.head = temp
        self.length = self.length + 1

    def append(self, item):
        """
        Adds a new item to the end of the circular doubly linked list.
        It needs the item and returns nothing.
        if item is not in list, add item in list.
        if item added, length will increase 1.
        """
        if self.is_empty():
            self.head = Node(item)
        else:
            temp = Node(item)
            if self.length == 1:
                new_temp = self.head
            else:
                new_temp = self.head.prev
            new_temp.next = temp
            temp.prev = new_temp
            temp.next = self.head
            self.head.prev = temp
        self.length = self.length + 1

    def insert(self, index, item):
        """
        Adds a new item to the circular doubly linked list at position index.
        It needs index, item.
        If list is empty then add item in list.
        If item added (selected position), list will increase 1
        """
        if self.is_empty():
            self.head = Node(item)
            self.head.next = self.head
        else:
            curr = self.head
            i = 0
            if (curr.next is not None) and (i < index):
                # Add item from the beginning index
                for i in range(index):
                    curr = curr.next
            else:
                # Add item from the ending index
                for i in range(index):
                    curr = curr.prev
            temp = Node(item)
            temp_n = curr.prev
            temp_n.next = temp
            temp.prev = temp_n
            temp.next = curr
            curr.prev = temp
        self.length += 1

    def pop(self, index):
        """
        Remove item at position index in circular doubly linked list.
        If index is not selected than removes last item in list.
        If head is None, return nothing.
        Decrease list size 1.
        Returns: data.
        """
        if index is None:
            index = self.size() - 1
        if self.head is None:
            return None
        elif index == 0:
            pop_i = self.head
            self.head = pop_i.next
            pop_i.next = None
            self.length = self.length - 1
            return pop_i.data
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

    def remove(self, item):
        """
       Removes the item from the circular doubly linked list.
       If item in list, remove that item in list.
       If item removed, decrease list size decrease 1.
       """
        curr = self.head
        if curr.data == item:
            self.head = curr.prev
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
        Search item in circular doubly linked list.
        If list is empty than exit.
        If item in list, return item index number
        else, return -1.
        """
        if self.head is None:
            return False
        curr_search = self.head.next
        i = 1
        while curr_search is not self.head:
            if curr_search.data == item:
                self.head = curr_search
                return i
            i += 1
            curr_search = curr_search.next
        return -1

    def is_empty(self):
        """
        See circular doubly linked list is empty or not.
        Returns: boolean value.
        """
        return self.head is None

    def size(self):
        """
        This shows that current circular doubly linked list total length
        Returns: list size (integer).
        """
        return self.length

    def __str__(self):
        """
       Write a normal string that print result in circular doubly Linked List.
       Returns: string(list content).
       """
        if self.head is None:
            return ""
        pt = ""
        if self.head.next is not self.head:
            tp = self.head.next
            pt = str(self.head.data)
            while tp != self.head:
                pt = pt + ' <=> ' + str(tp.data)
                tp = tp.next
        return ' <= ' + pt + ' => '


def main():
    # practice 1 (Doubly Linked List)
    practice1 = DoublyLinkedList()
    # Title of doubly linked list
    print('\n==============================================================')
    print('=                Doubly Linked List Practice                 =')
    print('==============================================================\n')
    # Add item in list (front)
    practice1.add("Apple")
    practice1.add('Banana')
    practice1.add('Orange')
    practice1.add('Cucumber')
    # Add item in list (back)
    practice1.append('Jelly')
    # Add item in list (position index)
    practice1.insert(2, 'Wine')
    # Search item in list (index number)
    print("Search idx of Banana:", practice1.search("Banana"))
    print(practice1)
    # Remove item 'Apple" in list
    print('Remove item Apple!!!')
    practice1.remove('Apple')
    print(practice1)
    # Current size of list
    print('Total length of List:', practice1.size())
    # Remove item in list (position index)
    practice1.pop(2)
    practice1.pop(3)
    print('Pop idx[2] and idx[4]!!!')
    # Print result of doubly linked list
    print(practice1)
    # Size of list
    print('Total length of List:', practice1.size())

    # practice 2 (CircularDoubly Linked List)
    practice2 = CircularDoublyLinkedList()
    # Title of circular doubly linked list
    print('\n===============================================================')
    print('=            Circular Doubly Linked List Practice             =')
    print('===============================================================\n')
    # Add item in list (front)
    practice2.add('Cake')
    practice2.add('Juice')
    practice2.add('Jam')
    practice2.add('Water')
    # Add item in list (back)
    practice2.append('Spam')
    print(practice2)
    # Current size of list
    print('Current size of list:', practice2.size())
    # Insert 'Grape' item in list (position index[1])
    practice2.insert(1, 'Grape')
    print('Insert item Grape in index[1]!!!')
    print(practice2)
    # Search 'Jam' index in list
    print("Search idx of Jam:", practice2.search('Jam'))
    # Remove 'Spam' item in list
    practice2.remove('Spam')
    print('Remove item Spam!!!')
    print(practice2)
    # Remove item in list (position index [2])
    practice2.pop(2)
    print('Pop idx[2]!!!')
    print(practice2)
    # Insert 'Kiwi' item in list (position index [-1])
    practice2.insert(-1, 'Kiwi')
    print('Insert item Kiwi in index[-1]!!!')
    # Print result of list
    print(practice2)
    # Size of circular doubly linked list
    print('Current size of list:', practice2.size())


if __name__ == '__main__':
    main()
