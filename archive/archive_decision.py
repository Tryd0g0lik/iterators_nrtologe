class SingleList:
  def __init__(self, lists):
    self.lists = lists
    self.el = []

#
  def __iter__(self):

    return self
#
  def __next__(self):
    result = self.el
    for lis in self.lists:
      for l in lis:
        result.append(l)

    return result

class SingleList2:
  def __init__(self, lists):
    self.lists = lists


  def __iter__(self):
    self.ind = 0

    return self

  def __next__(self):
    self.f = []
    try:
      if self.ind <= len(self.lists) -1 :
        for lis in self.lists:
          # self.lis = lis

          for li in lis:
            # self.f.append(li)
            self.f.append(li)
        # self.ind += 1
        return self.f

    # else StopIteration:
    except StopIteration:
      print("Стоп")
      exit()

class SingleList3:
  def __init__(self, lists):
    self.lists = lists

  #
  def __iter__(self):


    return self

  def __next__(self):
    lists = self.lists
    self.el = []
    for lis in lists:
      for l in lis:
        yield l



