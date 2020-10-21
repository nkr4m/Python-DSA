class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def take_input():
    li = [int(x) for x in input().split()]
    head = None
    tail = None
    for ele in li:
        if (ele == -1):
            break

        newNode = Node(ele)
        if head is None:
            head = newNode
            tail = newNode
        elif head is not None:
            tail.next = newNode
            tail = newNode
    return head

def printLL(head):
    while(head) is not None:
        print(head.data,end=" ")
        head = head.next

head = take_input()
printLL(head)