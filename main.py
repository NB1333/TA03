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

    def deletion(self, data):
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

    def deleteLastElement(self, data):
        if data is None:
            return None
        if data.next is None:
            data = None
            return None
        second_last = data
        while (second_last.next.next):
            second_last = second_last.next
        second_last.next = None
        return data

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


if __name__ == '__main__':
    newString = '\n'
    Range = 1000
    start_time = datetime.now()

    llist = LinkedList()

    start_time1 = datetime.now()
    for i in range(Range):
        llist.beginAdd(randint(10, 8000))
    print('Insert time at the begin: ' + str(datetime.now() - start_time1) + newString)

    llist.clear()

    start_time2 = datetime.now()
    for i in range(Range):
        llist.endAdd(randint(10, 8000))
    print('Insert time at the end: ' + str(datetime.now() - start_time2) + newString)

    llist.clear()
    llist.beginAdd(12)
    llist.beginAdd(2)

    start_time3 = datetime.now()
    for i in range(Range):
        llist.insertAfterIndex(llist.head.next, randint(10, 8000))
    print('Insert time after index: ' + str(datetime.now() - start_time3) + newString)

    llist.print()

    start_time4 = datetime.now()
    llist.deleteFirstElement()
    print('\n\nDeletion time of the first element: ' + str(datetime.now() - start_time4) + newString)
    llist.print()
    head = llist.endAdd(1337)

    start_time5 = datetime.now()
    llist.deleteLastElement(head)
    print('\nDeletion time of the last element: ' + str(datetime.now() - start_time5) + newString)
    llist.print()
    start_time6 = datetime.now()
    llist.deletion(3)
    print('\nDeletion time after index: ' + str(datetime.now() - start_time6) + newString)
    llist.print()
    start_time7 = datetime.now()
    llist.find(1337)
    print('Finding time: ' + str(datetime.now() - start_time7) + newString)
