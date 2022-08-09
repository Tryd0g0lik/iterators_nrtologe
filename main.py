import decision as dec



if __name__ == ('__main__'):
  # l = []
  i = 0
  nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None]
  ]
  o = (dec.SingleList3(iter(nested_list)))

  print("----------должен быть такой список------------")
  for l in dec.SingleList2(nested_list):
    print(l)
    break

  print("----------")
  r = [(res) for res in next(dec.SingleList3(iter(nested_list)))]
  print(r)


  print("----------Должен отпечататься каждый----------")
  for obj in next(dec.SingleList3(iter(nested_list))):
    print(obj)


