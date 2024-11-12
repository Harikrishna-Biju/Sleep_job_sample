def qmetrykey(key):
    def decorator(func):
        setattr(func, 'testcasekey', key)
        return func
    return decorator