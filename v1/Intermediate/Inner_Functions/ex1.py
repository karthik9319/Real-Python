import functools


def decorator(func):
    functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        value = func(*args, **kwargs)
        return value
    return wrapper_decorator


def generate_power(exponent):
    def decorator(f):
        functools.wraps(f)
        def inner(*args, **kwargs):
            value = f(*args, **kwargs)
            return value ** exponent
        return inner
    return decorator

@decorator
def square(n):
    return n**n


@generate_power(3)
def raise_two(n):
    return n

print(square(2))
print(raise_two(2))