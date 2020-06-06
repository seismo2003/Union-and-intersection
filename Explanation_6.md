Explanation on problem 6 - Union and intersection

1. I first wrote the code to sort out the LinkedList and I applied this extra
function to sort out the input linked-lists in the very beginning of both union
and intersection code.

2. For intersection code, I used while loop to cross compare the nodes from
linked-list 1 and linked-list 2. I append the smaller value of the nodes being
compared to the new "temp" linked-list and then move one node next for the
linked-list which has that smaller value. I continue to iterate until one of then
linked-list was pointing to None, then I attached the rest of the node for then
other linked-list to my "temp" linked-list and return "temp"

3. For Union code, I first used my sort function to sort out the linkedlist
in ascending order. With ascending order, I can apply similar comparison technique
I used in intersection code to compare nodes between linked-list-1 and linked-list-2,
I append the node value when I found common node value between linked-list-1 and
linked-list-2. If the value doesn't match, I move the pointers for both lists to
next node and compare again, until one of the list is pointing to None

Run time is O(n), since there's while iteration within the code. In the end, the
space complexity of the code will be O(len(element_1) + len(element_2) + 2) due to then
two linkedlists and two return union/intersection lists it has created
