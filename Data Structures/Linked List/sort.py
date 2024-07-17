""" TO SORT
1. instantiate a new linked list
2. find the maximum value
3. insert the maximum to the beginning of the linked list
4. remove the maximum value from the linked list
5. repeat steps 2-4 until head node points to None
6. return the new linked list
"""
from linkedlist import LinkedList

# we are sorting from smallest to largest
def sort_linked_list(linked_list):
    print("\n---------------------------")
    print("The original linked list is:\n{0}".format(linked_list.stringify_list()))
    new_linked_list = LinkedList()

    current = linked_list.get_head_node()
    maximum = current.get_value()
    while current.get_next_node():
        if current.get_value() > maximum:
            new_linked_list.insert_beginning(current.get_value())
            linked_list.remove_node(current.get_value())
    
        current.get_next_node()

    return new_linked_list




    return new_linked_list

  

#Test Cases
ll = LinkedList("Z")
ll.insert_beginning("C")
ll.insert_beginning("Q")
ll.insert_beginning("A")
print("The sorted linked list is:\n{0}".format(sort_linked_list(ll).stringify_list()))

ll_2 = LinkedList(1)
ll_2.insert_beginning(4)
ll_2.insert_beginning(18)
ll_2.insert_beginning(2)
ll_2.insert_beginning(3)
ll_2.insert_beginning(7)
print("The sorted linked list is:\n{0}".format(sort_linked_list(ll_2).stringify_list()))

ll_3 = LinkedList(-11)
ll_3.insert_beginning(44)
ll_3.insert_beginning(118)
ll_3.insert_beginning(1000)
ll_3.insert_beginning(23)
ll_3.insert_beginning(-92)
print("The sorted linked list is:\n{0}".format(sort_linked_list(ll_3).stringify_list()))

#Runtime
runtime = "N"
print("The runtime of sort_linked_list is O({0})\n\n".format(runtime))