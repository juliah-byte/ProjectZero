from abc import ABC, abstractmethod


class AccountDAO(ABC):
    @abstractmethod
    def transfer(self, amount):
        pass

    @abstractmethod
    def deposit(self, amount):
        pass
