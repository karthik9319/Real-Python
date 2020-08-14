import functools
import time


def slow_time(func):
    @functools.wraps(func)
    def wrapper_slow_time(*args, **kwargs):
        time.sleep(1)
        value = func(*args, **kwargs)
        return value
    return wrapper_slow_time


@slow_time
def countdown(number):
    if number < 1:
        print("Lift off")
    else:
        print(number)
        countdown(number -1)
        

if __name__ == "__main__":
    inp = int(input("Enter number: "))
    countdown(inp)