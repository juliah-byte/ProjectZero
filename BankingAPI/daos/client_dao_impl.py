from abc import ABC

from daos.client_dao import ClientDAO
from exceptions.resource_not_found import ResourceNotFound
from util.dblayer import DbLayer as db


class ClientDAOImpl(ClientDAO, ABC):

    def create_client(self, client):
        db.client[client.client_id] = client

    def get_all_clients(self):
        # return [client.__dict__ for client in db.client.values()]
        return [client.json() for client in db.client.values()]

    def get_client(self, client_id):
        try:
            return db.client[client_id]
        except KeyError:
            raise ResourceNotFound(f"Client with ID: {client_id} -- Not Found")

    def update_client(self, change):
        db.client.update({change.id: change})







