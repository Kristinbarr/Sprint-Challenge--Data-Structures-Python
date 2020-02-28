
class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if value is smaller than root,
        if value < self.value:
            # if left node is present, 
            if self.left == None:
                # insert new 'tree' on left
                self.left = BinarySearchTree(value)
            else:
                # repeat steps on left side
                self.left.insert(value)
        # if value is greater or equal than root,
        else:
            # if right node is present,
            if self.right == None:
                # insert new 'tree' on right
                self.right = BinarySearchTree(value)
            else:
                # repeat steps on right side
                self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if target is equal to root:
        if target == self.value:
            return True

        # if target is smaller than the root:
        if target < self.value:
            if self.left == None:
                return False
            # repeat on left
            print('left node val:',self.left.value)
            return self.left.contains(target)
        # if target is larger than root:
        else: # target >= self.value:
            if self.left == None:
                return False
            # repeat on right side
            return self.right.contains(target)


    # Return the maximum value found in the tree
    def get_max(self):
        if not self.right:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        pass
        # call cb on self.value
        cb(self.value)
        # if left is present,
        if self.left:
            # call for_each
            self.left.for_each(cb)
        # if right is present,
        if self.right:
            # call for_each
            self.right.for_each(cb)
