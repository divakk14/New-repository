import time

def timestamp(func):
    def wrapper(*args, **kwargs):
        print(time.ctime())
        return func(*args, **kwargs)
    return wrapper