class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    value_index = len(self.storage) - 1
    self._bubble_up(value_index)

  def delete(self):
    last_item = self.storage.pop()
    if self.storage:
      deleted = self.storage[0]
      self.storage[0] = last_item
      self._sift_down(0)
      return deleted
    else:
      return last_item

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    while index > 0:
      parent = (index - 1) // 2
      if self.storage[index] > self.storage[parent]:
        self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
        index = parent
      else:
        break

  def _sift_down(self, index):
    while index * 2 + 1 <= len(self.storage) - 1:
      if index * 2 + 2 > len(self.storage) - 1:
        max_size = index * 2 + 1
      elif self.storage[index * 2 + 1] > self.storage [index * 2 + 2]:
        max_size = index * 2 + 1
      else:
        max_size = index * 2 + 2
      
      if self.storage[max_size] > self.storage[index]:
        self.storage[max_size], self.storage[index] = self.storage[index], self.storage[max_size]
      index = max_size