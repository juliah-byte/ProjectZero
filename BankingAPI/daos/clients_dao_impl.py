from daos.client_dao import ClientDAO
from exceptions.resource_not_found import ResourceNotFound
from models.client import Client
from util.db_connection import connection


class ClientsDAOImpl(ClientDAO):

    def create_client(self, client):
        sql = "INSERT INTO client VALUES (DEFAULT,%s,%s,%s,%s) RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, (client.username, client.password, client.firstname, client.lastname))

        connection.commit()
        record = cursor.fetchone()

        new_Client = Client(float(record[0]), record[1], record[2], record[3], record[4])
        return new_Client

    def get_client(self, client_id):
        sql = "SELECT * FROM client WHERE id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [client_id])

        record = cursor.fetchone()

        if record:
            return Client(record[0], record[1], record[2], record[3], record[4])
        else:
            raise ResourceNotFound(f"Movie with id: {client_id} - Not Found")

    def get_all_clients(self):
        sql = "SELECT * FROM client"
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()

        client_list = []

        for record in records:
            client = Client(record[0], record[1], record[2], record[3], record[4])

            client_list.append(client.json())

        return client_list

    def update_client(self, change):
        sql = "UPDATE client SET username=%s,password=%s,firstname=%s,lastname=%s WHERE id = %s RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, (change.username, change.password, change.firstname, change.lastname, change.client_id))
        connection.commit()

        record = cursor.fetchone()

        new_client = Client(record[0], record[1], record[2], record[3], record[4])
        return new_client

    def delete_client(self, client_id):
        sql = "DELETE FROM client WHERE id = %s"

        cursor = connection.cursor()
        cursor.execute(sql, [client_id])
        connection.commit()


def _test():
    m_dao = ClientsDAOImpl()
    movies = m_dao.get_all_clients()
    print(movies)

    print(m_dao.get_client(1))


if __name__ == '__main__':
    _test()
