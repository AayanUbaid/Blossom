from linked_list import Node, LinkedList
from blossom_lib import flower_definitions

class HashMap:
    def __init__(self, array_size):
        self.array_size = array_size
        self.array = [LinkedList() for i in range(array_size)]

    def hash(self, key):
        key_bytes = key.encode()
        hash_code = sum(key_bytes)
        return hash_code

    def compress(self, hash_code):
        return hash_code % self.array_size

    def assign(self, key, value):
      array_index = self.compress(self.hash(key))
      list_at_array = self.array[array_index]

      node = list_at_array.get_head_node()

    # handle the case where the bucket's "head" is just the empty placeholder
      if node.get_value() is None:
        list_at_array.head_node = Node([key, value])
        return

      while node is not None:
        if node.get_value()[0] == key:
            node.value = [key, value]
            return
        if node.get_next_node() is None:
            node.set_next_node(Node([key, value]))
            return
        node = node.get_next_node()

    def retrieve(self, key):
      array_index = self.compress(self.hash(key))
      list_at_array = self.array[array_index]

      node = list_at_array.get_head_node()
      while node is not None:
        if node.get_value() is not None and node.get_value()[0] == key:
            return node.get_value()[1]
        node = node.get_next_node()

      return None

blossom = HashMap(len(flower_definitions))

for flower in flower_definitions:
    blossom.assign(flower[0], flower[1])

print(blossom.retrieve('daisy'))