from functools import wraps #import wraps from functool to overcome stacking decorators issue


def my_logger(orig__function):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig__function.__name__), level=logging.INFO)

    @wraps(orig__function)
    def wrapper(*args, **kwargs):
        logging.info('Ran with args: {}, and kwargs: {}'.format(args,kwargs))
        return orig__function(*args,**kwargs)

    return wrapper


def my_timer(orig__function):
    import time

    @wraps(orig__function)
    def wrapper(*args,**kwargs):
        t1 = time.time()
        result = orig__function(*args,**kwargs)
        t2 = time.time()-t1
        print('{} ran in: {} sec'.format(orig__function.__name__, t2))
    return wrapper

import time

@my_logger
@my_timer
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))

display_info('Johnny', 26)