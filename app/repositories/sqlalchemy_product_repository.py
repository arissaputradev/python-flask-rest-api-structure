from app.database import db
from app.models.product import Product
from app.repositories.product_repository import ProductRepository


class SQLAlchemyProductRepository(ProductRepository):
    def save(self, product):

        db_product = Product(name=product["name"], price=product["price"])

        db.session.add(db_product)
        db.session.commit()

        return db_product

    def find_all(self):
        return Product.query.all()

    def find_by_id(self, id):
        return Product.query.get(id)

    def update(self, id, data):
        product = Product.query.get(id)

        if not product:
            return None

        product.name = data.get("name", product.name)
        product.price = data.get("price", product.price)

        db.session.commit()

        return product

    def delete(self, id):
        product = Product.query.get(id)

        if not product:
            return False

        db.session.delete(product)
        db.session.commit()

        return True
