def allcaps(func):
    def wrapper():
        res = func()
        return res.upper()
    return wrapper