from abc import ABC

from daos.account_dao import AccountDAO


class AccountDAOImpl (AccountDAO, ABC):

    def deposit(self, amount):
        pass

    def transfer(self, amount_id):
        pass

