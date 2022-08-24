from dec import Iterator, generate

if __name__ == "__main__":
  nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None]
  ]
  print("------------------Part one------------------")
  obj = Iterator(nested_list)
  for el in Iterator(nested_list):
    print(el)

  el = [el for el in Iterator(nested_list)]
  print(el)
  print()
  print("------------------Part two------------------")
  el = [el for el in generate(nested_list)]
  print(el)
  print()

