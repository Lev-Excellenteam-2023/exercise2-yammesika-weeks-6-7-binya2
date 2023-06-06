def join(*lists, sep='-'):
    """
    :param lists: If the parameter 'sep' is provided then it is threaded between any two lists.
    :param sep: Default value is "-".
    :return: All lists obtained as parameters as one list.
    """
   
    result = []
    for index in range(len(lists) - 1):
        result += lists[index]
        result.append(sep)
     result += lists[len(lists) - 1]
     return "".join(str(res))
  


if __name__ == '__main__':
    print(join())
    print(join([1, 2, 3], [4, 5, 6], sep='@'))
    print(join([1, 2], [8], [9, 5, 6], sep='@'))
