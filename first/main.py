from linked_list import LinkedList, Node

def reverse_list(linked_list: LinkedList):
    prev = None
    current = linked_list.head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    linked_list.head = prev


def merge_sort(linked_list: LinkedList):
    if not linked_list.head or not linked_list.head.next:
        return linked_list

    middle = get_middle(linked_list.head)
    next_to_middle = middle.next

    middle.next = None

    left_half = LinkedList()
    right_half = LinkedList()
    left_half.head = linked_list.head
    right_half.head = next_to_middle

    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    sorted_list = merge_two_sorted_lists(left_sorted, right_sorted)
    return sorted_list

def get_middle(head):
    if not head:
        return head

    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow

def merge_two_sorted_lists(list1, list2):
    dummy = Node(0)
    tail = dummy

    l1, l2 = list1.head, list2.head
    while l1 and l2:
        if l1.data <= l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    if l1:
        tail.next = l1
    elif l2:
        tail.next = l2

    merged_list = LinkedList()
    merged_list.head = dummy.next
    return merged_list


llist1 = LinkedList()
llist2 = LinkedList()

llist1.append(1)
llist1.append(4)
llist1.append(5)

llist2.append(2)
llist2.append(3)
llist2.append(6)

merged_llist = merge_two_sorted_lists(llist1, llist2)
merged_llist.print_list()

reverse_list(merged_llist)
merged_llist.print_list()

llist3 = LinkedList()
llist3.append(3)
llist3.append(2)
llist3.append(1)
llist3.append(5)
llist3.append(4)
llist3.append(6)

sorted_llist = merge_sort(merged_llist)
sorted_llist.print_list()