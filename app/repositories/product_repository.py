class ProductRepository:
    def __init__(self):
        self.products = []
        self.current_id = 1

    def save(self, product):
        product.id = self.current_id
        self.current_id += 1
        self.products.append(product)
        return product

    def find_all(self):
        return self.products
