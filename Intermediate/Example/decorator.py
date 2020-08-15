import functools


def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # do something before
        value = func(*args, **kwargs)
        # do something after
        return value

    return wrapper_decorator


def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args)
            return value

        return wrapper_repeat

    return decorator_repeat


def better_repeat(_func=None, *, num_times=2):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value

        return wrapper_repeat

    return decorator_repeat

    if _func is not None:
        return decorator_repeat(_func)
    else:
        return decorator_repeat(func)


@repeat(num_times=4)
def greet(name):
    print(f"hello {name}")


@better_repeat(num_times=4)
def greet_world(name):
    print(f"hello {name}, Welcome to World")


@better_repeat()
def say_whee():
    print("hola hola")


greet_world("karthik")
say_whee()
