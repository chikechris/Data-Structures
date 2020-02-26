
"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""

    def add_to_head(self, value):
        # make a new node
        new_node = ListNode(value, None, None)
        # grow the length of the linked list
        self.length += 1

        # if this is not head or tail (singular node)
        if not self.head and not self.tail:
            # set the head and tail to this new node
            self.head = new_node
            self.tail = new_node
        # otherwise
        else:
            # set the new nodes Next to the current head
            new_node.next = self.head
            # set the heads prev to the new node
            self.head.prev = new_node
            # set the head ref to the new node
            self.head = new_node

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):
        # set the return value to the value of the head
        value = self.head.value
        # delete head
        self.delete(self.head)
        # return the value
        return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        # make a new node
        new_node = ListNode(value, None, None)
        # grow the length of the linked list
        self.length += 1

        # if this is not head or tail (singular node)
        if not self.head and not self.tail:
            # set the head and tail to this new node
            self.head = new_node
            self.tail = new_node
        # otherwise
        else:
            # set the new nodes Prev to the current tail
            new_node.prev = self.tail
            # set the tails next to the new node
            self.tail.next = new_node
            # set the tail ref to the new node
            self.tail = new_node

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):
        # set the return value to the tail value
        value = self.tail.value
        # delete the tail
        self.delete(self.tail)
        # return the value
        return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):
        # if node is head then return
        if node is self.head:
            return
        # set value to nodes value
        value = node.value
        # if the node is the tail
        if node is self.tail:
            # remove node from tail
            self.remove_from_tail()
        # otherwise
        else:
            # delete the node
            node.delete()
            # decrement the length
            self.length -= 1

        # add the value to the head
        self.add_to_head(value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
                # if node is tail then return
        if node is self.tail:
            return
        # set value to nodes value
        value = node.value
        # if the node is the head
        if node is self.head:
            # remove node from head
            self.remove_from_head()
        # otherwise
        else:
            # delete the node
            node.delete()
            # decrement the length
            self.length -= 1

        # add the value to the tail
        self.add_to_tail(value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):
        # decrement the length
        self.length -= 1
        # if not head or tail return
        if not self.head and not self.tail:
            return
        # if the head is the tail
        if self.head == self.tail:
            # set the head and tail to none
            self.head = None
            self.tail = None
        # otherwise if head is the node
        elif self.head == node:
            # set the head to the nodes next
            self.head = node.next
            # delete node
            node.delete()
        # otherwise if tail is the node
        elif self.tail == node:
            # set the tail to the nodes prev
            self.tail = node.prev
            # delete node
            node.delete()
        # otherwise
        else:
            # delete node
            node.delete()

    """Returns the highest value currently in the list"""

    def get_max(self):
        # if no head the return None
        if not self.head:
            return None
        # set the initial max value to the heads value
        max_value = self.head.value
        # set current node to head
        current_node = self.head
        # loop over nodes while current exists
        while current_node:
            # if current value is greater than the max value
            if current_node.value > max_value:
                # set the max value to the current value
                max_value = current_node.value
            # move to the next node
            current_node = current_node.next
        # return max value
        return max_value


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
     """

    def __init__(self, limit=10):
        self.limit = limit
        self.size = 0
        self.list = DoublyLinkedList()
        self.cache = dict()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
     """

    def get(self, key):
        # Check if key is in cache
        if key in self.cache.keys():
            # The cache is holding a reference to the node
            node = self.cache[key]
            # Move the node to the head because it's being accessed, or "used"
            self.list.move_to_front(node)
            # Return the value of the node: Tuple ('key', 'value')
            return node.value[1]
        else:
            # If the key doesn't exist in the cache, return None
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
     """

    def set(self, key, value):
        # Check if key is in cache
        if key in self.cache.keys():
            # The cache is holding a reference to the node
            node = self.cache[key]
            # Update the existing node's value
            node.value = (key, value)
            # Move the node to the head because it's being accessed, or "used"
            self.list.move_to_front(node)
        else:
            # Check to see if the limit is reached
            if self.size == self.limit:
                # Delete the oldest from the cache
                del self.cache[self.list.remove_from_tail()[0]]
                self.size -= 1
            # Add the new node to the head
            node = (key, value)
            self.list.add_to_head(node)
            # Set the cache to reference the node
            self.cache[key] = self.list.head
            self.size += 1
