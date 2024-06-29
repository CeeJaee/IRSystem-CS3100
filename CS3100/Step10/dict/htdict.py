import math
from dict.abstract import DictAbstract

# Jude - node class for linked list
class _Node:
  def __init__(self, key, value):
    self.key = key
    self.value = value
    self.next = None

  # print out node
  def __str__(self):
    return str(self.key) + ": " + str(self.value)

class HTDict(DictAbstract):
  def __init__(self):
    # it is usually recommended to keep the load factor below a certain threshold, such as 0.7 or 0.8.
    # 20 / 0.7 = 28.5 round up to 29
    self._arr_size = 1000
    self._size = math.ceil(self._arr_size/0.7)
    self.keys = [None] * self._size
    self.value = [None] * self._size
    self._data = [None] * self._size
    self._ht_list = [None] * self._size
    
  
  def __len__(self):
    return len(self._ht_list)

  # Isaac - this will be summing all the ASCII values of string and then mod it by array length  
  def __contains__(self, key):
    try:
      self._find(key)
      return True
    except KeyError:
      return False
  # Jude - Implementing the python magic method __getitem__
  # This function will help in using this sytax dict[key]
  def __getitem__(self, key):  
    item = self._find(key)

    if item == None:
      raise KeyError("Item does not exist.")
    return item

  # Jude - find index, if index slot full, must traverse the slot's linked list until the key is found.
  def _find(self, key):
    # get the hash code of the key
    hash_code = self._hash(key)

    if hash_code >= len(self._ht_list):
      return None
    # start at the given key's slot, then search linked list
    curr_node = self._ht_list[hash_code]
    # if the current node matches key, then return the node
    # else set current to the next node
    '''if key == curr_node.key:
      return curr_node
    else:
      return self._find(curr_node.next, key)'''
    while curr_node:
      if curr_node.key == key:
        return curr_node.value
      else:
        curr_node = curr_node.next
    return None
  
  def __setitem__(self, key, value):
    self._insert(key, value)
    
  # in this must check if value exists in slot, if there is, add to the slot's linked list...must use the hash function to find the index to insert in the list
  # Abigail - insert a key and value pair into the hashtable
  def _insert(self, key, value):
    #self._size += 1
    
    hash_code = self._hash(key)
    if hash_code >= len(self._ht_list):
        self._ht_list += [None] * (hash_code - len(self._ht_list) + 1)
        
    curr_node = self._ht_list[hash_code]
    # if node is empty
    if curr_node is None:
      # create new node and add it, then return
      self._ht_list[hash_code] = _Node(key, value)
      return
    # iterates through the linked list
    prev = curr_node

    while curr_node is not None:
      prev = curr_node
      curr_node = curr_node.next
    # add a node at the end of the linked list with the key and value
    prev.next = _Node(key, value)

  # It takes a key as input and computes a hash code using Python's built-in hash function. The resulting hash value is then used as an index to determine where to store or retrieve the value in the hash table. The modulo operation with the size of the hash table is applied to ensure that the hash value is within the range of the hash table's indices.
  # Isaac
  def _hash(self, key):
    # Abigail - added the string folding method into the function
    # hash function using string folding (converted the code from the book into python)
    # takes the string as a input
    # processes the string four bytes at a time and processes it into a interger value
    # the values are added together and then mod by self._size
    
    sum = 0
    mul = 1
    for i in range(len(key)):
      if i % 4 == 0:
        mul = 1
      else:
        mul * 256
      sum += ord(key[i]) * mul
    return abs(sum) % self._size
    
    #return hash(key) % self._size
    
  # Isaac - needs to pop out the key, keeping the other key in order 
  def pop(self, key):
    #gets the index of the key in the hash table
    index = self._hash(key)
    #check if index greater, if so then raise error
    if index >= len(self._ht_list):
      raise KeyError("Key does not exist")

    #set the cuurent node to the head of the linked list at the index
    curr_node = self._ht_list[index]
    # set the previous node to None
    prev_node = None

    # loops through the linked list
    while curr_node:
      #finding the key
      if curr_node.key == key:
        #check if the node is head of the linked list
        if prev_node is None:
          #set new head to the linked list
          self._ht_list[index] = curr_node.next
        else:
          #node wasn't the head so goes to the next pointer
          prev_node.next = curr_node.next
        return curr_node.value
    raise KeyError("Key does not exist")
      
  

  # Isaac - remove the key 
  def _remove(self, key):
    #gets the index of the key in the hash table
    index = self._hash(key)
    #check if index greater, if so then raise error
    if index >= len(self._ht_list):
      raise KeyError("Key does not exist")

    #set the cuurent node to the head of the linked list at the index
    curr_node = self._ht_list[index]
    # set the previous node to None
    prev_node = None

    # loops through the linked list
    while curr_node:
      #finding the key
      if curr_node.key == key:
        #check if the node is head of the linked list
        if prev_node is None:
           # set the new head of the linked list
          self._ht_list[index] = curr_node.next
        # if the node to be removed is not the head of the linked list
        else:
          # set the previous node's next pointer to the node after curr_node
          prev_node.next = curr_node.next
        return
        
      # set the previous node to the current node
      prev_node = curr_node
      # set the current node to the next node in the linked list
      curr_node = curr_node.next

    raise KeyError("Key does not exist")
        
  # Jude - get a specific indicator from all the nodes
  def getatt_htdict(self, attribute):
    items = []
    # for each index, and for each node, append the attribute of the node's value (which is a Country object) as well as the country name of the node
    for idx, node in enumerate(self._ht_list):
      curr_node = node
      while curr_node:
        items.append(getattr(curr_node.value, attribute))
        #items.append(getattr(curr_node.value, "country name"))
        items.append(curr_node.key)
        curr_node = curr_node.next
    return items

  # Jude - be able to print out the dictionary
  def __str__(self):
    items = []
    for idx, node in enumerate(self._ht_list):
      curr_node = node
      # while a node exists, append the node's key and value to items
      while curr_node:
        items.append(f"{curr_node.key}: {curr_node.value}")
        curr_node = curr_node.next
    # in brackets, join together all elements in the 'items' list
    return "{" + ", ".join(items) + "}"
    pass
