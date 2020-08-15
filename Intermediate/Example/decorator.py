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
            for i in range(num_times):
                value = func(*args)
            return value
        return wrapper_repeat
    return decorator_repeat
    
            

@repeat(num_times = 4)
def greet(name):
    print(f"hello {name}")

greet("karthik")