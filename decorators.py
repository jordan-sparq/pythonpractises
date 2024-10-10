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
from typing import Callable, Any, Dict

def timer_decorator(func: Callable) -> Callable:
    """A decorator that measures the execution time of a function."""
    @wraps(func)  # This preserves the metadata of the original function
    def wrapper(*args, **kwargs) -> Any:
        start_time = time.time()  
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' executed in {execution_time:.4f} seconds.")
        return result
    return wrapper

def caching_decorator(func: Callable) -> Callable:
    """A decorator that caches the results of a function based on its arguments."""
    cache: Dict[tuple, Any] = {}
    
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        # Create a cache key based on the function arguments
        cache_key = args + tuple(kwargs.items())
        
        # Check if the result is already cached
        if cache_key in cache:
            print(f"Returning cached result for {func.__name__} with args: {args}, kwargs: {kwargs}")
            return cache[cache_key]
        
        # If not cached, call the function and cache the result
        result = func(*args, **kwargs)
        cache[cache_key] = result
        return result

    return wrapper

# Example usage of the timer decorator and caching decorator
@timer_decorator
@caching_decorator
def example_function(seconds: int) -> str:
    """A function that simulates a delay."""
    time.sleep(seconds)
    return f"Function finished after {seconds} seconds."

# Call the example function
result1 = example_function(2)
print(result1)

# Call the example function with the same argument to test caching
result2 = example_function(2)
print(result2)

# Call the example function with a different argument
result3 = example_function(3)
print(result3)
