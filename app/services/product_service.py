from app.models.product import Product


class ProductService:
    def __init__(self, repository):
        self.repository = repository

    def create_product(self, name, price):
        if not name:
            raise ValueError("Name is required")
        if price is None:
            raise ValueError("Price is required")

        product = Product(name, price)

        return self.repository.save(product)

    def list_products(self):
        return self.repository.find_all()
