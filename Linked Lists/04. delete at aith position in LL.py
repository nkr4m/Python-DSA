class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def take_input():
    li = [int(x) for x in input().split()]
    head = None
    tail = None
    for ele in li:
        if ele == -1:
            break

        newNode = Node(ele)
        if head is None:
            head = newNode
            tail = newNode
        elif head is not None:
            tail.next = newNode
            tail = newNode
    return head

def length_LL(head):
    count = 0
    while(head) is not None:
        count = count + 1
        head = head.next
    return count

def delete_aith(head, pos):
    if(pos<0 or pos>length_LL(head)):
        return None

    count = 0
    prev = None
    curr = head

    while(count<pos and count != None):
        prev = curr
        curr = curr.next
        count = count + 1

    if curr is None:
        prev.next = None
    elif curr is not None:
        prev.next = curr.next

def print_LL(head):
    while head is not None:
        print(head.data,end=" ")
        head = head.next

head = take_input()
delete_aith(head, 2)
print_LL(head)