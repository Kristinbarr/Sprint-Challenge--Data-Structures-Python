class Node:
  def __init__(self, value=None, next_node=None):
    # the value at this linked list node
    self.value = value
    # reference to the next node in the list
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    # set this node's next_node reference to the passed in node
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    # reference to the head of the list
    self.head = None

  def add_to_head(self, value):
    node = Node(value)
    if self.head is not None:
      node.set_next(self.head)

    self.head = node

  def contains(self, value):
    if not self.head:
      return False
    # get a reference to the node we're currently at; update this as we traverse the list
    current = self.head
    # check to see if we're at a valid node
    while current:
      # return True if the current value we're looking at matches our target value
      if current.get_value() == value:
        return True
      # update our current node to the current node's next node
      current = current.get_next()
    # if we've gotten here, then the target node isn't in our list
    return False

  def reverse_list(self):

    # save values
    # switch values
    # change head

    # save node in cur position, start w copy of current head (v5,n4)
    curr = self.head
    # save node in prev position, currently none but will be (v4,n3)
    prev = None

    # while head.next is not none
    while curr != None:
      # temp to save curr.next
      tempNext = curr.next_node
      # set curr.next to prev (none)
      curr.next_node = prev

      # reset/reassign/shift variables over:

      # reset/shift prev to be new cur (4)
      prev = curr
      # reset curr to future next node(temp)
      curr = tempNext

    # set head to prev once at the end (saved in outer scope)
    self.head = prev

