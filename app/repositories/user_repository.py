from abc import ABC, abstractmethod


class UserRepository(ABC):
    @abstractmethod
    def save(self, product):
        pass

    @abstractmethod
    def find_all(self):
        pass

    @abstractmethod
    def find_by_id(self, id):
        pass

    @abstractmethod
    def update(self, id, data):
        pass

    @abstractmethod
    def delete(self, id):
        pass
