from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item): # head is the most current?

        # if at capacity, remove old, add new item
        if self.capacity == self.storage.length:
            # remove oldest (tail?)
            self.storage.remove_from_tail()
            # add new item tail
            self.storage.add_to_tail(item)

        # then set new item as current node
        self.current = self.storage.head
        self.storage.add_to_head(item)
        # set head's prev to tail node, vis versa to make a ring
        self.storage.head.prev = self.storage.tail
        self.storage.tail.next = self.storage.head


    # returns all buffer elements in a list in their given order
    # it should not return any None values in the ring buffer
    def get(self):
        list_buffer_contents = []
        print()

        cur = self.storage.tail
        print('while loop:', cur, self.storage.tail.next.value)

        while cur.value != self.storage.tail.next.value:
            print('value inside:', cur.value)
            # take current, add to list,
            list_buffer_contents.append(cur.value)
            print('list buffer inside', list_buffer_contents)

            # get next value, set as current?, add to list
            cur = cur.prev
            print('new current', cur.value)

        list_buffer_contents.append(cur.value)
        print('END list buffer:',list_buffer_contents)
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
