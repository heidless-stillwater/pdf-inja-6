from icecream import ic
from functools import wraps
import time

# Decoratores

#
# def outer_function(msg):
#     def inner_function():
#         ic(msg)
#     return inner_function
#
# hi_func = outer_function('Hi')
# bye_func = outer_function('Buy')
#
# hi_func()
# bye_func()

def decorator_function(orig_func):
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        ic('wrapper executes this before {}'.format(original_function.__name__))
        return orig_func(*args, **kwargs)
    return wrapper


# class decorator_class(object):
#     def __init__(self, original_function):
#         self.original_function = original_function
#
#     def __call__(self, *args, **kwargs):
#         ic('__call__ class executes this before {}'.format(self.original_function.__name__))
#         return self.original_function(*args, *kwargs)


def pn_logger(orig_func):
    import logging
    logging.basicConfig(filename='./app/logs/pdf_ninja.log'.format(orig_func.__name__), level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper


def pn_timer(orig_func):
    import time

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))

        return result

    return wrapper
#
# @my_logger
# @my_timer
# def display():
#     time.sleep(2)
#     ic(' display function ran')
#
# @my_logger
# @my_timer
# def display_info(name, age):
#     time.sleep(1)
#     ic('display_info ran with arguements ({}, {})'.format(name, age))
#
#
# display_info('Hank', 35)
# # display()
#
# #
# # decorated_display = decorator_function(display)
# #
# # decorated_display()
# #
# # display()
