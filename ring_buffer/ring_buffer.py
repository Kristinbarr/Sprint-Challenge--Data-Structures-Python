from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # if at capacity,
        if self.capacity == self.storage.length:
            # remove oldest from tail
            self.storage.remove_from_tail()
        # create new node
        # add new node to head
        self.storage.add_to_head(item)
        # set head's next pointer to the tail
        self.storage.head.prev = self.storage.tail
        self.storage.tail.next = self.storage.head
        # set current pointer to OLDEST node??
        self.current = self.storage.head
        print("\nSET finisihed, new curr head:",self.current.value)


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # temp length variable
        size = self.storage.length
        print('\nstarting size:', size, 'cur:', self.current.value)
        # set current to tail
        # self.current = self.storage.tail
        # while length is not 0,
        # OR while current is not head?
        while size > 0:
            # if current val is not None,
            print('\ncur val inside while loop:', self.current.value)
            if self.current.value is not None:
                # add current to list
                list_buffer_contents.append(self.current.value)
                print('list:', list_buffer_contents)
            # change current to head's next
            self.current = self.current.prev
            print('new current:',self.current.value)
            # decrement temp length variable
            size -= 1
            print('size:', size )

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
