from dict.abstract import DictAbstract

# Node class with key and value 
class _Node:
  def __init__(self, key, value):
    self.key = key
    self.value = value
    self.next = None
  
  # print out node
  def __str__(self):
    return str(self.key) + ": " + str(self.value)
  

class LLDict(DictAbstract):
  
  def __init__(self):
    self._head = None
    self._size = 0

  # Jude - return number of elements in linked list
  def __len__(self):
    return self._size
    pass

  #Implementing the python magic method __contains__
  #This will help to use in true or false sentences
  #e.g., if key is in dict
  # Abigail
  def __contains__(self, key):
    return not self._find(self._head, key) is None
    pass

  # Jude
  # Implementing the python magic method __getitem__
  # This function will help in using this sytax dict[key]
  def __getitem__(self, key):  
    node = self._find(self._head, key)
    if node == None:
      raise KeyError("Item does not exist")
    return node.value
    
  
  # Jude - recursive function -- if key matches, then return the node
  # otherwise, go to the next node until key matches
  def _find(self, node, key):
    curr_node = node
    while curr_node is not None:
      if key == curr_node.key:
        return curr_node
      curr_node = curr_node.next
    return None
  
  # Jude
  # Implements self[key] = value. If key is already stored in
  # the dictionary then its value is modified.
  def __setitem__(self, key, value):
    # If linked list is empty, then create a head node
    if self._head == None:
      self._head = _Node(key, value)
      self._size += 1
    # Otherwise insert a new node at the head
    else:
      self._insert(self._head, key, value)
    

  # Jude - helper function to __setitem__
  def _insert(self, node, key, value):
    # if a key already exists in the linked list, update value
    if node.key == key:
      node.value = value
    # otherwise create a new node, make the new node point to current head, set the head node to the new node, increase size count by 1
    else:
      new_node = _Node(key, value)
      new_node.next = self._head
      self._head = new_node
      self._size += 1
    
  #Isaac
  #Remove a node from the tree with the indicated key
  #Return the value after removing the node
  #Raise a KeyError if the key is not in the map."
  def pop(self, key):

    #calling on the __getitem__ function to get value
    #calling on the help method _remove 
    value = self[key]
    self._head = self._remove(self._head, key)
    self._size -= 1
    
    return value
  # Isaac
  # a helper method to remove a country
  def _remove(self, node, key):
    if node is None:
      return None

    #key check for the key 
    if key < node.key:
      node.next = self._remove(node.next, key)
    elif key > node.key:
      node.next = self._remove(node.next, key)

    else:
      #temp os the node to be deleted
      temp = node
      #set node to next node
      node = node.next
      #delete temp
      temp = None

    return node
  
  #Isaac
  #helper method to look for the smallest key
  def _min_value_node(self, node):
    current = node
    while (current.next is not None):
      current = current.next

    return current
    
  # Jude - from the linked list, get a specified attribute value from all Country objects.
  def getatt_lldict(self, attribute):
    if self._head is not None:
      return self._getatt_lldict(self._head, attribute)

  # Jude - helper function to getatt_lldict
  # create an empty list. Recursively traverse linked list 
  # starting from given node (head node) and append the given attribute
  # and country name to the list, return the list.
  def _getatt_lldict(self, node, attribute):
    list = []
    if node:
      list = self._getatt_lldict(node.next, attribute)
      list.append(getattr(node.value, attribute))
      list.append(getattr(node.value, "country_name"))
    return list
    
  pass