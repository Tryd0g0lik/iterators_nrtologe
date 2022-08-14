class IteratorTask1:
  def __init__(self, lists):
    self.lists = lists
    self.ind = 0

  def __iter__(self):
    return self

  def __next__(self):
    try:

      for lis in self.lists:
        for li in lis:
          yield li

    except StopIteration:
      print("Стоп")
      exit()

def GenratorTask2(lists):

  for lis in lists:
    for li in lis:
      yield li


class IteratorTask3:
  def __init__(self, lists):
    self.lists = lists
    self.ind = 0

  def __iter__(self):
    return self

  def __next__(self):

    for item in self.lists:
      if list == type(item):
        return IteratorTask3(item)

      else:
        yield item

class IteratorTask4:
  def __init__(self, lists):
    self.lists = lists
    self.ind = 0

  def __iter__(self):
    return self

  def __next__(self):

    for item in self.lists:
      # if list == type(item):
      if type(item) == list:
        self.lists = IteratorTask4(next(item))

      else:
        return item


