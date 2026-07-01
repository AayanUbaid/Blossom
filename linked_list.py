class Node:
  def __init__(self, value, next_node=None):
    self.value = value         # stores the data of this node
    self.next_node = next_node # pointer to next node (None by default = end of list)
    
  def get_value(self):
    return self.value          # RETURNS value (does not print, you print it yourself)
  
  def get_next_node(self):
    return self.next_node      # RETURNS next node object (does not print!)
  
  def set_next_node(self, next_node):
    self.next_node = next_node # WRITES/CREATES connection between two nodes


# LinkedList class manages all nodes together
class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value) # create the first node (head = front of the list)
  
  def get_head_node(self):
    return self.head_node        # RETURNS the first node of the list

  def insert_beginning(self, new_value):
    new_node = Node(new_value)            # step 1: create a new node with given value
    new_node.set_next_node(self.head_node)# step 2: point new node to current head (so nothing is lost)
    self.head_node = new_node             # step 3: make new node the new head of the list

  def stringify_list(self):
    string_list = ""                      # start with empty string to collect all values
    current_node = self.head_node         # begin traversal from head node

    while current_node:                   # keep looping as long as node exists (None = False = stop)
      string_list += str(current_node.get_value()) + "\n" # add node value + new line to string
      current_node = current_node.get_next_node()         # move to next node (follow the pointer)
    
    return string_list                    # return the final collected string (you print it yourself)


  def remove_node(self, value_to_remove):
    if self.head_node.get_value() == value_to_remove:   # check if head_node is the node to remove
        self.head_node = self.head_node.get_next_node() # skip head_node by pointing to second node
    else:
        current_node = self.head_node                   # start traversal from head node
        while current_node:                             # keep looping as long as node exists
            next_node = current_node.get_next_node()    # get the next node
            if next_node.get_value() == value_to_remove: # check if next node is the one to remove
                current_node.set_next_node(next_node.get_next_node()) # skip over the removed node
                current_node = None                     # set to None to exit the loop
            else:
                current_node = current_node.get_next_node() # move to next node and keep traversing 