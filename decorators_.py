def outer(message):
    print('In the outer function')

    def inner():
        print('calling the inner functions')
        print(message)

    return inner


# f = outer('Hello world')
# f()


def decorator(original_func):
    def wrapper():
        print(f'wrapper executed before {original_func.__name__}()')

        if 10 > 5:
            print('yes it is true')

        return original_func()

    return wrapper


# non key word arguments => f(1,2,3)
# keyword arguments => f(arg1=1, arg2=2)

def decorator_2(original_func):

    def wrapper(*args, **kwargs):
        print(f'wrapper executed before {original_func.__name__}()')

        if 10 > 5:
            print('yes it is true')

        return original_func(*args, **kwargs)

    return wrapper


@decorator
def print_something():
    print('print_something is being ran!')


@decorator_2
def print_something_more(arg1, arg2):
    print(f'printing argument 1 = {arg1} and argument 2 = {arg2}')


print_something_more(1, 2)


# func = decorator(print_something)
# func()
