# Type Hinting 3.10+

# Basic Types:

# int: Integer type
# float: Floating-point type
# str: String type
# bool: Boolean type

# Collections:

# List: A list type (e.g., List[int] for a list of integers)
# Tuple: A tuple type (e.g., Tuple[str, int] for a tuple containing a string and an integer)
# Dict: A dictionary type (e.g., Dict[str, int] for a dictionary with string keys and integer values)
# Set: A set type (e.g., Set[str] for a set of strings)

# Optional Types:

# Optional: Indicates that a value could be of a specified type or None (e.g., Optional[int] means it could be an int or None).

# Any Type:

# Any: Represents any type (not recommended for general use as it defeats the purpose of type hints).


from dataclasses import dataclass, field
from typing import List, Tuple, Dict, Optional, Union, Any

@dataclass
class User:
    """Class to represent a user with various attributes."""
    name: str
    age: int
    favorite_fruits: List[str] # list of strings
    user_data: Dict[str, int] = field(default_factory=dict)  # Default to an empty dictionary

@dataclass
class DataProcessor:
    """Class to demonstrate different typing features."""
    integer_value: Optional[int] # int OR none
    string_value: Optional[str] # str OR none
    float_list: List[float]
    user: User
    item_index: Optional[int] = None  # To store the index of a favorite fruit