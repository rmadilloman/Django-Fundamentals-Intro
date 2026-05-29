import random
from miapp.models import Product

def create_test_products():
    products = []
    brands = ["Toyota", "Honda", "Ford", "Chevrolet", "Nissan", "BMW", "Mercedes", "Hyundai", "Mitsubishi"]
    colors = ["Red", "Blue", "Black", "White", "Silver", "Gray", "Yellow"]

    for i in range(500):
        product = Product(
            name=f"Car Part {i+1} - {random.choice(brands)} Bumper",
            price=round(random.uniform(29.99, 899.99), 2),
            description=f"High quality replacement bumper for {random.choice(brands)} vehicles. Model {i+1}",
            seller="Auto Parts Pro",
            color=random.choice(colors),
            product_dimensions=f"{random.randint(150, 250)}x{random.randint(80, 150)}x{random.randint(20, 60)} cm"
        )
        products.append(product)

    Product.objects.bulk_create(products)
    print(f"created {len(products)} test products")

# run
if __name__ == "__main__":
    create_test_products()