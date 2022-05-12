from datetime import datetime
import time
from random import *


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def find(self, item):

        while self.head is not None:
            if self.head.data == item:
                return True
            self.head = self.head.next
        return False

    def beginAdd(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def endAdd(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while (last.next):
            last = last.next

        last.next = new_node

    def insertAfterIndex(self, previous_node, new_data):
        if previous_node is None:
            print("Previous element is none")
            return

        new_node = Node(new_data)
        new_node.next = previous_node.next
        previous_node.next = new_node

    def deleteElement(self, data):
        if self.head is None:
            return

        temp = self.head

        if data == 0:
            self.head = temp.next
            temp = None
            return

        for i in range(data - 1):
            temp = temp.next
            if temp is None:
                break

        if temp is None:
            return

        if temp.next is None:
            return

        next = temp.next.next
        temp.next = None
        temp.next = next

    def deleteFirstElement(self):
        if self.head != None:
            temp = self.head

            self.head = self.head.next

            temp = None

    def deleteLastElement(self):
        if self.head is not None:

            if self.head.next is None:
                self.head = None
            else:

                temp = self.head
                while temp.next.next is not None:
                    temp = temp.next

                lastNode = temp.next
                temp.next = None
                lastNode = None

    def print(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

    def clear(self):
        while (self.head != None):
            temp = self.head
            self.head = self.head.next
            temp = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
        self.next = None
        self.previous = None

    def beginAdd(self, new_data):

        new_node = Node(new_data)

        new_node.next = self.head

        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node

    def endAdd(self, new_data):

        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = new_node

        new_node.prev = temp

        return

    def insertAfterIndex(self, previous_node, new_data):
        if previous_node is None:
            print("previous node cannot be null")
            return

        new_node = Node(new_data)

        new_node.next = previous_node.next

        previous_node.next = new_node

        new_node.prev = previous_node

        if new_node.next:
            new_node.next.prev = new_node

    def deleteElement(self, data):
        if data == 0:
            self.head = self.head.next
            self.head.previous = None
            self.count -= 1
            return

        if data == (self.count - 1):
            self.tail = self.tail.previous
            self.tail.next = None
            self.count -= 1
            return

        start = self.head
        for i in range(data):
            start = start.next
#        start.previous.next, start.next.previous = start.next, start.previous
        self.count -= 1
        return

    def deleteFirstElement(self):
        if self.head is not None:

            temp = self.head

            self.head = self.head.next

            temp = None

            if self.head is not None:
                self.head.prev = None

    def deleteLastElement(self):
        if self.head is not None:

            if self.head.next is None:
                self.head = None
            else:
                temp = self.head
                while temp.next.next is not None:
                    temp = temp.next

                lastNode = temp.next
                temp.next = None
                lastNode = None

    def find(self, data):
        start = self.head
        for i in range(self.count):
            if (start.data == data):
                return i
            start = start.next
        return None

    def print(self):
        current = self.head

        while current != None:
            print(current.data),
            current = current.next

    def clear(self):
        while self.head != None:
            temp = self.head
            self.head = self.head.next
            temp = None


def operations(listType):
    start_time1 = datetime.now()
    for i in range(Range):
        listType.beginAdd(randint(10, 8000))
    print('Insert time at the begin: ' + str(datetime.now() - start_time1))

    listType.clear()

    start_time2 = datetime.now()
    for i in range(Range):
        listType.endAdd(randint(10, 8000))
    print('Insert time at the end: ' + str(datetime.now() - start_time2))

    listType.clear()
    listType.beginAdd(12)
    listType.beginAdd(2)

    start_time3 = datetime.now()
    for i in range(Range):
        listType.insertAfterIndex(listType.head.next, randint(10, 8000))
    print('Insert time after index: ' + str(datetime.now() - start_time3))

#    listType.print()

    start_time4 = datetime.now()
    listType.deleteFirstElement()
    print('\nDeletion time of the first element: ' + str(datetime.now() - start_time4))

#    listType.print()

    start_time5 = datetime.now()
    listType.deleteLastElement()
    print('Deletion time of the last element: ' + str(datetime.now() - start_time5))

#   listType.print()

    start_time6 = datetime.now()
    listType.deleteElement(3)
    print('Deletion time after index: ' + str(datetime.now() - start_time6))

#    listType.print()

    start_time7 = datetime.now()
    listType.find(1337)
    print('\nFinding time: ' + str(datetime.now() - start_time7))


if __name__ == '__main__':
    newString = '\n'
    Range = 1000
    start_time = datetime.now()

    llist = LinkedList()
    dllist = DoublyLinkedList()
    print("-------------------Linked List--------------------\n")
    operations(llist)
    print("\n----------------Doubly Linked List----------------\n")
    operations(dllist)