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
