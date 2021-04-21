from models.client import Client


class DbLayer:

    client = {
        1: Client(client_id=1, username="john1", password="pass1", firstname="John", lastname="Doe"),
        2: Client(client_id=2, username="julia", password="pass2", firstname="Julia", lastname="Smith"),
        3: Client(client_id=3, username="jack", password="pass3", firstname="Jack", lastname="Walker")
    }