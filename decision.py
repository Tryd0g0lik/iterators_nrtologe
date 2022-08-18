from decorator import decorate
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
    self.lists = iter(lists)
    self.element = (element for element in next(self.lists))
  def __iter__(self):

    return self

  def __next__(self):


    for item in list(self.element):

      el = list(item).pop(0)
      if type(item) == list:
        el += self.lists
        continue
      else:
        return item


#
# def IteratorTask3(lists):
#   # lists = next(iter(lists))
#   el = list(lists).pop(0)
#   while lists:
#     for item in (lists):
#       # el = list(lists).pop(0)
#
#       if isinstance(item, list):
#         # return IteratorTask3(next(item))
#         lists = list(el) + lists
#         continue
#       else:
#         return item
