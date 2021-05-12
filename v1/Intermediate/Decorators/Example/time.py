import functools
import time


def timer(func):
    """ print the run time of the decorator function"""

    @functools.wraps(func)
    def wrapper_time(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"finished {func.__name__!r} in {run_time:.4f} secs")
        return value

    return wrapper_time


@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i ** 2 for i in range(1000)])


if __name__ == "__main__":
    waste_some_time(0)
