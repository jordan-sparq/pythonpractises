# This python file demonstrates the basic functionality of data classes

### DATA CLASSES
# Data classes in Python, introduced in Python 3.7, 
# are a convenient way to create classes that primarily store data. 
# They automatically generate several methods like __init__, __repr__, __eq__, __hash__
# and more, reducing boilerplate code. 

from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float
    stock: int

# Example usage
# Data classes come with some nice features:
# 1. Immutability: 

@dataclass(frozen=True)
class ImmutableProduct:
    name: str
    price: float
    stock: int

# Example usage
# immutableproduct = ImmutableProduct("parking", 100, 10_000)
# immutableproduct.price = 10  # Raises a FrozenInstanceError: cannot assign to field 'x'

# 2. Default Factory

from dataclasses import field

@dataclass
class DefaultFactoryProduct:
    name: str
    price: float = 100  # Default value for price
    stock: list = field(default_factory=list)  # Use default_factory for mutable types

# Example usage
# defaultfactoryproduct = DefaultFactoryProduct(name="parking")
# print(defaultfactoryproduct)  # DefaultFactoryProduct(name='parking', price=100, stock=[])
# This ensures that mutable types like lists or dictionaries don't share the same
# instance across objects, which is a common pitfall in Python.

# 3. Field customisation

@dataclass
class FieldCustomisationProduct:
    name: str
    creationdatestr: str = field(compare=False, repr=False)  # Exclude creationdatestr from comparison and representation
    price: float = 100  # Default value for price

# Example usage
# fieldcustomisationprod1 = FieldCustomisationProduct("Toyota", 100, creationdatestr="2024-01-01")
# fieldcustomisationprod2 = FieldCustomisationProduct("Toyota", 100, creationdatestr="2024-02-01")
# print(fieldcustomisationprod1 == fieldcustomisationprod2)  # True, ignores creationdatestr during comparison

# 4. Simple Conversions

# You can easily convert your dataclass instances to dictionaries or tuples using the asdict() 
# and astuple() functions. This is handy when you need to serialize or process the data in a different format.

from dataclasses import asdict, astuple

@dataclass
class ConversionsProduct:
    name: str
    price: float

# Example usage
# conversionsproduct = ConversionsProduct("Laptop", 999.99)
# print(asdict(conversionsproduct))  # {'name': 'Laptop', 'price': 999.99}
# print(astuple(conversionsproduct))  # ('Laptop', 999.99)

# 5. Post init

# If you need to initialise given the member variables you can using post init

@dataclass
class PostInitProduct:
    name: str
    base_price: float
    tax_rate: float

    def __post_init__(self):
        # Calculate total price after tax
        self.total_price = self.base_price * (1 + self.tax_rate)

# Example usage
# postinitproduct = PostInitProduct(name="Laptop", base_price=1000, tax_rate=0.15)
# print(postinitproduct.total_price)  # Outputs: 1150.0 (1000 + 15% tax)

# 6. Hidden Fields


@dataclass
class HiddenFieldsProduct:
    name: str
    price: float
    supplier_code: str = field(repr=False)  # Don't include supplier code in repr output

# type: ignore # Example usage
# hiddenfieldsproduct = HiddenFieldsProduct(name="Smartphone", price=799.99, supplier_code="SUP12345")
# print(hiddenfieldsproduct)  # Outputs: Product(name='Smartphone', price=799.99)``