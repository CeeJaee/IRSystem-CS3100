from dict.abstract import DictAbstract

class SLDict(DictAbstract):
  
  def __init__(self):
    self._list = []
    pass
  # Jude - return length of list
  def __len__(self):
    return len(self._list)
    pass

  # Abigail 
  # used bubble sort to sort through the list by the country name
  def _sort(self):
    l = len(self._list)
    for i in range(l):
      for j  in range(l-i-1):
        # swaps the data if the element is less than the next element in the list
        if self._list[j][0] > self._list[j+1][0]:
          self._list[j], self._list[j+1] = self._list[j+1], self._list[j]
    return self._list

  def __contains__(self, key):
    return not self._find(key) is None
    
  
  # Jude - helps in using dict[key]
  def __getitem__(self, key):
    # search _list for the key
    # if the key exists, then return the value
    val = self._find(key)
    if val is not None:
      # [1] is the value of key
      return self._list[val][1]
    
  # Abigail - inserted binary search algorithm in replace to the linear search
  # notes: insert binary search
  def _find(self, key):
    """
    # searching through all the keys in _list
    # if the key matches with the given key, return it
    for x in range(len(self._list)):
      # [x][0] is the x number index, with 0 meaning the first
      # element in the tuple, which is the key
      if self._list[x][0] == key:
        return x
    """
    # lower half or left half
    low = 0
    # higher half or right half
    high = len(self._list) - 1
    
    while low <= high:
      mid = (high + low) // 2
      # if key is greater, ingore the left half
      if self._list[mid][0] < key:
        low = mid + 1
      # if key is smaller, ignore the right half
      elif self._list[mid][0] > key:
        high = mid - 1
      # key is found at the mid
      else:
        return mid
    # key was not found 
    return None
    

  # Jude - self[key] = value
  def __setitem__(self, key, value):
    # check if the key exists in _list, if it does
    # update the value
    val = self._find(key)
    if val is not None:
      self._list[val] = (key, value)
    # otherwise, insert the new item (the new key and value)
    else:
      self._insert(key, value)
    

  # need to add sorting algorithm in _insert
  # Abigail - append key and value using tuple to _list
  def _insert(self, key, value):
    
    self._list.append((key, value))
    self._sort()
    
  # Isaac - pop out the key
  def pop(self, key):
    #find the key
    idx = self._find(key)
    if idx is not None:
      #remove key and value at the index
      val = self._list[idx][1]
      self._list.pop(idx)
      return val
    else: 
      #return error that keyt was not found
      raise KeyError(f"Key '{key}' not found")
    

  # Isaac - remove the key
  def _remove(self, key):
    #find the key
    idx = self._find(key)
    if idx is not None:
      #pop out all of the data from the key
      self._list.pop(idx)
    else:
      #return a error is country not found
      raise KeyError(f"Key '{key}' not found")
    

  # Jude
  # get specific attribute from all Country objects, returns as a list
  def getatt_sldict(self, attribute):
    items = []
    # iterate through _list
    # for each element in the list, access the value (country object)
    # and retrieve user input's attribute and its country name
    for x in range(len(self._list)):
      items.append(getattr(self._list[x][1], attribute))
      items.append(getattr(self._list[x][1], "country_name"))
    return items
  
  # Jude - be able to print out the dictionary
  def __str__(self):
    items = []
    # for all the keys and values in _list, append the pairs
    # of keys and values to items
    # each element looks like: [key1:value, key2:value,....]
    for key, value in self._list:
      items.append(f"'{key}': {value}")
    # in brackets, join together all elements in the 'items' list
    return "{" + ", ".join(items) + "}"
  

