import functools

def debug(func):
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}= {v!r}" for k, v in kwargs.items()]
        signature = ",".join(args_repr + kwargs_repr)
        print(f"calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"calling {func.__name__!r} returned {value !r}")
        return value
    return wrapper_debug


@debug
def make_greeting(name, age = None):
    if age is None:
        return f"Howdy {name}"
    else:
        return f"Whao {name}! {age} already you're growing up!"
        
        
make_greeting("Karthik")
make_greeting("Karthik", age=26)