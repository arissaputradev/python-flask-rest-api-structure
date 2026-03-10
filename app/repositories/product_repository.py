from abc import ABC, abstractmethod


class ProductRepository(ABC):
    @abstractmethod
    def save(self, product):
        pass

    @abstractmethod
    def find_all(self):
        pass
