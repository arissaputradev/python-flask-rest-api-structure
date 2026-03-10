from app.repositories.product_repository import ProductRepository


class ProductService:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def create_product(self, name, price):
        if not name:
            raise ValueError("Name is required")
        if price is None:
            raise ValueError("Price is required")

        product = {"name": name, "price": price}

        return self.repository.save(product)

    def list_products(self):
        return self.repository.find_all()

    def get_product(self, product_id):
        product = self.repository.find_by_id(product_id)

        if not product:
            raise ValueError("Product not found")

        return product

    def update_product(self, product_id, product):
        product = self.repository.update(product_id, product)
        if not product:
            raise ValueError("Product not found")

        return product

    def delete_product(self, product_id):
        product = self.repository.find_by_id(product_id)

        if not product:
            raise ValueError("Product not found")

        self.repository.delete(product_id)
        return product
