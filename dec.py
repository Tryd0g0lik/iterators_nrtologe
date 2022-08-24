"------------------Part one------------------"
class Iterator():
  def __init__(self, lists):
    self.lists = (lists)

  def __iter__(self):
    self.li = []
    for el in self.lists:
      self.li += el
    return self

  def __next__(self):
    li = self.li
    if li == []:
      raise StopIteration
    for l in li:
      li.remove(l)
      return (l)

"------------------Part two------------------"
def generate(lists):
    lists = iter(lists)
    li = []
    for el in lists:
      li += el

    for l in li:
      if li == []:
        exit()
      yield (l)
