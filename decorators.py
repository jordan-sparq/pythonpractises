# Decorators

# Decorators in Python are a powerful and flexible way to modify or enhance the behavior of functions or methods. 
# They allow you to wrap another function, adding functionality before or after the wrapped function runs without 
# permanently modifying it. This is particularly useful for logging, enforcing access control, instrumentation, caching, 
# and timing.

# A decorator is essentially a function that takes another function as an argument, adds some kind of functionality, 
# and returns a new function. You can apply a decorator to a function using the @decorator_name syntax above the 
# function definition.

import time
from functools import wraps

def timer_decorator(func):
    @wraps(func)  # This preserves the metadata of the original function
    def wrapper(*args, **kwargs):
        start_time = time.time()  
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' executed in {execution_time:.4f} seconds.")
        return result
    return wrapper

# Example usage of the timer decorator
@timer_decorator
def example_function(seconds):
    """A function that simulates a delay."""
    time.sleep(seconds)
    return f"Function finished after {seconds} seconds."

# Call the example function
result = example_function(2)
print(result)

# Function 'example_function' executed in 2.0051 seconds.
# Function finished after 2 seconds.