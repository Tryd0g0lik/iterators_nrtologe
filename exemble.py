class FlatIterator:
  def __init__(self, some_list):
    self.iter1 = iter(some_list)
    self.iter2 = iter(next(self.iter1))

  def __iter__(self):
    return self

  def __next__(self):
    try:
      return next(self.iter2)
    except StopIteration:
      try:
        next_list = next(self.iter1)
        while not next_list:
          next_list = next(self.iter1)
        self.iter2 = iter(next_list)
        return next(self.iter2)
      except StopIteration:
        raise StopIteration


class DeepFlatIterator:
  def __init__(self, some_list):
    self.long_list = list(some_list)

  def __iter__(self):
    return self

  def __next__(self):
    while self.long_list:
      element = self.long_list.pop(0)
      if isinstance(element, list):
        self.long_list = element + self.long_list
      else:
        return element
    raise StopIteration


def flat_generator(some_list):
  while some_list:
    inner_list = some_list.pop(0)
    while inner_list:
      yield inner_list.pop(0)


def deep_flat_generator(some_list):
  while some_list:
    element = some_list.pop(0)
    if isinstance(element, list):
      some_list = element + some_list
    else:
      yield element


if __name__ == '__main__':
  nested_list = [
    ['a', 'b', 'c'],
    [],
    [],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None]
  ]

  print('Результат работы обыного итератора:')

  for item in FlatIterator(nested_list):
    print(item)

  # flat_list = [item for item in FlatIterator(nested_list)]
  # print(flat_list)

  print('\n--------------------------------')
  print('Результат работы обычного генератора:')

  for item in flat_generator(nested_list):
    print(item)

  nested_list1 = [11,
                  ['a', 'b', [1, 2, 3, [4, 5], 6], 'c'],
                  [22],
                  [[]],
                  [],
                  ['d', 'e', [], 'f', 'h', False],
                  [1, 2, None]
                  ]
  print('\n--------------------------------')
  print('Результат работы глубого итератора:')

  for item in DeepFlatIterator(nested_list1):
    print(item)

  print('\n--------------------------------')
  print('Результат работы глубого генератора:')

  for item in deep_flat_generator(nested_list1):
    print(item)