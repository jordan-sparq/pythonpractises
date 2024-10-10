# Inheritance vs Composition

# Inheritance: The DiscountedProduct is a specialized type of Product and can directly extend and 
# override its functionality. It follows an "is-a" relationship (e.g., a DiscountedProduct is-a Product).

# Composition: The ProductWithSupplier class uses Product as one of its components, establishing a "has-a" 
# relationship (e.g., a ProductWithSupplier has-a Product).

# 1. Inheritance

# discounted product is a product --> use inheritance

from dataclasses import dataclass, field

@dataclass
class Product:
    name: str
    base_price: float
    tax_rate: float

    def __post_init__(self):
        self.total_price = self.base_price * (1 + self.tax_rate)

@dataclass
class DiscountedProduct(Product):  # Inherits from Product
    discount: float = 0.0  # Default discount is 0%

    def __post_init__(self):
        # First, call the parent class's __post_init__ to calculate total price
        super().__post_init__()
        # Then, apply discount to the total price
        self.total_price -= self.total_price * self.discount

# Example usage:
laptop = DiscountedProduct(name="Laptop", base_price=1000, tax_rate=0.15, discount=0.1)
print(laptop.total_price)  # Outputs: 1035.0 (1000 + 15% tax, then 10% discount)

# 2. Composition

# Supplier has a product --> use composition

@dataclass
class Product:
    name: str
    price: float

@dataclass
class ProductWithSupplier:
    product: Product  # Composition: A Product is part of this class
    supplier_code: str = field(repr=False)  # Hide supplier code in repr output

    def product_info(self):
        return f"{self.product.name} costs {self.product.price}, supplied by {self.supplier_code}"

# Example usage:
smartphone = Product(name="Smartphone", price=799.99)
product_with_supplier = ProductWithSupplier(product=smartphone, supplier_code="SUP12345")

print(product_with_supplier.product_info())  # Outputs: Smartphone costs 799.99, supplied by SUP12345

