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


# before:
# (1, n:2) (2, n:3) (3, n:4) (4, n:None)

# pre: None
# cur: (1, n:2) -> (1, n:pre)
# nex: (2, n:3)
# (1, n:None) (2, n:3) (3, n:4) (4, n:None)

# pre: (1, n:None)
# cur: (2, n:3) -> (2, n:pre)
# nex: (3, n:4)
# (1, n:None) (2, n:1) (3, n:4) (4, n:None)

# pre: (2, n:1)
# cur: (3, n:4) -> (3, n:pre)
# nex: (4, n:None)
# (1, n:None) (2, n:1) (3, n:4) (4, n:None)

# pre: (3, n:2)
# cur: (4, n: None) -> (4, n:pre)
# nex: None
# (1, n:None) (2, n:1) (3, n:2) (4, n:3)

  def reverse_list(self):

    if not self.head:
      return

    pre = None
    cur = self.head
    print('\nCUR START:',cur.value)
    nex = cur.next_node

    # while temp itself is not None
    while nex is not None:
      # save cur node(starting at first node)
      # cur = self.head
      # save nex for the cur node's next
      # nex = self.head.next_node
      # print('NEX:', nex.value)
      # reassign cur node's next
      cur.next_node = pre

      # reassign cur to the nex node
      cur = nex
      print('\nCUR:',cur.value)
      # reassign nex to the cur.next_node
      nex = cur.next_node
      print('NEX:',nex.value)
      # reassign pre to the cur node
      pre = cur
      print('PRE:',pre.value)
      