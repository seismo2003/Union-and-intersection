
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    # Your Solution Here
    if llist_2.head is None and llist_1.head is None:
        return None

    if llist_1.head is None:
        return sortlist(llist_2)

    if llist_2.head is None:
        return sortlist(llist_1)

    llist_1 = sortlist(llist_1)
    llist_2 = sortlist(llist_2)

    list1 = llist_1.head
    list2 = llist_2.head
    temp = LinkedList()

    while list1 and list2:
        if list1.value > list2.value:
            temp.append(list2.value)
            list2 = list2.next
        elif list1.value < list2.value:
            temp.append(list1.value)
            list1 = list1.next
        else:
            temp.append(list1.value)
            list2 = list2.next
            list1 = list1.next

    while list2:
        temp.append(list2.value)
        list2 = list2.next

    while list1:
        temp.append(list1.value)
        list1 = list1.next

    return temp


def intersection(llist_1, llist_2):
    # Your Solution Here

    if llist_1.head is None:
        return None

    if llist_2.head is None:
        return None

    llist_1 = sortlist(llist_1)
    llist_2 = sortlist(llist_2)

    list1 = llist_1.head
    list2 = llist_2.head
    temp = LinkedList()

    while list1 and list2:
        if list1.value > list2.value:
            list2 = list2.next
        elif list1.value < list2.value:
            list1 = list1.next
        elif list1.value == list2.value:
            temp.append(list1.value)
            list1 = list1.next
            list2 = list2.next

    if temp.head is None:
        return "None"
    else:
        return temp


def sortlist(llist):
    prev = llist.head
    cur = llist.head.next

    while (cur != None):
        if (cur.value < prev.value):
            prev.next = cur.next
            cur.next = llist.head
            llist.head = cur
            prev = cur
            #prev = llist.head
        elif (cur.value > prev.value):
            prev = cur
        else:
            prev.next = cur.next
        cur = cur.next

    return llist

# Test case 1 - Edge Case

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = []
element_2 = [1,3,5,5,3,26]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)


print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))


# Test case 2 - Edge Case

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))

# Test case 3

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [0,1,1000,2,4,62,32,7]
element_2 = [6,32,4,9,2,12,110,21,1]

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)


print (union(linked_list_5,linked_list_6))
print (intersection(linked_list_5,linked_list_6))
