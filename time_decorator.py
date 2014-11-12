#comment for github
import time
def timer(f):
    def tmp(*args, **kwargs):
        t = time.time()
        res = f(*args, **kwargs)
        print "Время выполнения функции: %f" % (time.time()-t)
        return res

    return tmp

@timer
def func(x, y):
    return x + y

@timer
def func1(x, y):
    return x / y
