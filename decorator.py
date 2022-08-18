
def decorate(fun):

  def wrapper(*arg, **kwarg):
    lis = []
    responses = fun(*arg)
    for res_ in responses:
      if type(res_) == list:
        responses = fun(next(res_))



      else:
        yield res_
  return wrapper
