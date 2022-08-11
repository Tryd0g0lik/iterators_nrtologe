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






