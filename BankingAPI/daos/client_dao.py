from abc import abstractmethod, ABC


class ClientDAO(ABC):

    @abstractmethod
    def create_client(self, client):
        pass

    @abstractmethod
    def get_all_clients(self):
        pass

    @abstractmethod
    def get_client(self, client_id):
        pass

    @abstractmethod
    def update_client(self, change):
        pass

    @abstractmethod
    def delete_client(self, client_id):
        pass
