import decision as dec


"""ВОПРОС
В каких задачах по факту применятся итератор?
На курсе упоминалась ситуация - подсчет веса.
Но вчем там особенность логики, из-за которой приходится применить итератор?


https://prnt.sc/9wIfi5ByXZwu
Какая логика вшита в функцию next(...)?

"""


if __name__ == ('__main__'):
  nested_list2 = [
    ['a', [11, 5, ['sss', 'ddd', None], 91], 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None]]

  i = 0
  nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None]
  ]
  objec = dec.IteratorTask1(nested_list)
  print("----------1. Написать итератор------------")
  for l in next(iter(objec)):
    print(l)

  print("----------")
  flat_list = [res for res in next(dec.IteratorTask1(iter(nested_list)))]
  print("flat_list: ", flat_list)

  print()
  print()
  print("----------2. Написать генератор ----------")
  mylist = []
  for element in dec.GenratorTask2(nested_list):
    mylist.append(element)
  print(mylist)

  # print("---------------")
  # print("---------------")
  #
  # print("----------3. *Написать итератор аналогичный ----------")
  # o = dec.IteratorTask3(nested_list2)

  # for el in dec.IteratorTask3(nested_list2):
  #   print(el)


  # nested_list2 = [
  #   ['a', [11, 5, ['sss', 'ddd', None], 91], 'c'],
  #   ['d', 'e', 'f', 'h', False],
  #   [1, 2, None]]


# 18.08. 13:40
# 315
#
# анотация типов - прочитать
#
# Класс метод
# Стат метод
