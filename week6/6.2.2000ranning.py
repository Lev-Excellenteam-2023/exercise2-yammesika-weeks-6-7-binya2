import time
""""
    This function calculate the run time of the argument function.
    :param f: The function.
    :param args1: this is the parameters of the function if they are given by position
    :param args2: this is the parameters of the function if they are given by name
    :return: the execution time of the function
    """

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        elapsed_time = time.time() - start_time
        print(f"Function '{func.__name__}' took {elapsed_time:.4f} seconds to execute.")
        return result
    return wrapper

@timer_decorator
def function_1(message):
    print(message)

@timer_decorator
def function_2(list1, list2):
    result = list(zip(list1, list2))
    print(result)

@timer_decorator
def function_3(name):
    result = "Hi {name}".format(name=name)
    print(result)

if __name__ == '__main__':
    function_1("Hello")
    function_2([1, 2, 3], [4, 5, 6])
    function_3(name="Bug")

