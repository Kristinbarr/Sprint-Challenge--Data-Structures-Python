from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # if at capacity,
        if self.capacity > self.storage.length:
            # add to tail, tail will be the right side
            self.storage.add_to_tail(item)
            self.current = self.storage.head
        else:
            # replace the curr value
            self.current.value = item
            if self.current == self.storage.tail:
                self.current = self.storage.head
            else:
                self.current = self.current.next


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        current = self.storage.head
        # temp length variable
        size = self.storage.length
        # while length is not 0,
        while size > 0:
            # don't add to list if value is None
            if current.value is not None:
                # add current to list
                list_buffer_contents.append(current.value)
            # change current to head's next
            current = current.next
            # decrement temp length variable
            size -= 1

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
