from datetime import datetime
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
        while last.next:
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
        if self.head is not None:
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
        while self.head is not None:
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
            self.head.previous = new_node

        self.head = new_node

    def endAdd(self, new_data):
        new_node = Node(new_data)
        new_node.prev = self.tail

        if self.tail is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = None
        else:
            self.tail.next = new_node
            new_node.next = None
            self.tail = new_node

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
        self.count -= 1
        return

    def deleteFirstElement(self):
        if self.head is not None:

            temp = self.head

            self.head = self.head.next

            temp = None

            if self.head is not None:
                self.head.previous = None

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
            if start.data == data:
                return i
            start = start.next
        return None

    def print(self):
        current = self.head

        while current is not None:
            print(current.data),
            current = current.next

    def clear(self):
        while self.head is not None:
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

    start_time4 = datetime.now()
    listType.deleteFirstElement()
    print('\nDeletion time of the first element: ' + str(datetime.now() - start_time4))

    start_time5 = datetime.now()
    listType.deleteLastElement()
    print('Deletion time of the last element: ' + str(datetime.now() - start_time5))

    start_time6 = datetime.now()
    listType.deleteElement(3)
    print('Deletion time after index: ' + str(datetime.now() - start_time6))

    start_time7 = datetime.now()
    listType.find(1337)
    print('\nFinding time: ' + str(datetime.now() - start_time7))


class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        if self.head is None:
            self.head = Node(data)

        else:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode

    def pop(self):
        if self.head is None:
            return None

        else:
            popNode = self.head
            self.head = self.head.next
            popNode.next = None
            return popNode.data

    def peek(self):
        if self.head is None:
            return None
        else:
            return self.head.data

    def print(self):
        iterationNode = self.head

        if self.head is None:
            print("Stack Underflow")
        else:
            while iterationNode is not None:
                print(iterationNode.data, end=" ")
                iterationNode = iterationNode.next
            return


class Queue:
    def __init__(self):
        self.first = self.last = None

    def size(self):
        temp = self.first
        count = 0
        while temp is not None:
            count = count + 1
            temp = temp.next
        return count

    def EnQueue(self, item):
        temp = Node(item)

        if self.last is None:
            self.first = self.last = temp
            return
        self.last.next = temp
        self.last = temp

    def DeQueue(self):
        if self.first is None:
            print('Queue is empty')
            return
        temp = self.first
        self.first = temp.next

        if self.first is None:
            self.last = None

    def printFirstElement(self):
        print('First element is: ' + str(self.first.data))

    def printLastElement(self):
        print('Last element is: ' + str(self.last.data))


def stackRealisation():
    print('\nThis is a stack that uses a linked list:')
    stackRange = int(input('Input size of stack: '))

    stack = Stack()

    for i in range(stackRange):
        stack.push(randint(10, 100))

    stack.print()

    stack.pop()

    print('\nTop element of stack after pop() is ' + str(stack.peek()))

    stack.print()


def queueRealisation():
    print('\n\nThis is a queue that uses a linked list:')
    queueRange = int(input('Input size of queue: '))

    queue = Queue()

    for i in range(queueRange):
        queue.EnQueue(randint(10, 100))

    print('\nQueue size is: ' + str(queue.size()))

    queue.printFirstElement()
    queue.printLastElement()

    for i in range(queueRange + 1):
        queue.DeQueue()


if __name__ == '__main__':
    Range = 1000

    llist = LinkedList()
    dllist = DoublyLinkedList()
    print("-------------------Linked List--------------------\n")
    operations(llist)
    print("\n----------------Doubly Linked List----------------\n")
    operations(dllist)

    stackRealisation()
    queueRealisation()
