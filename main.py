from datetime import datetime
import time

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

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

    #def deleteBeginning(self):
        

    def print(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next


if __name__ == '__main__':
    start_time = datetime.now()
    llist = LinkedList()
    llist.beginAdd(4)
    llist.endAdd(34)
    llist.endAdd(6)
    llist.endAdd(3)
    llist.insertAfterIndex(2, 5)
    llist.print()

    time.sleep(5)
    print(datetime.now() - start_time)

