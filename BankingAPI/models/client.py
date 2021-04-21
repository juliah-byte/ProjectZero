class Client:

    def __init__(self, client_id=0, username="", password="", firstname="", lastname=""):
        self.client_id = client_id
        self.username = username
        self.password = password
        self.firstname = firstname
        self.lastname = lastname

    def json(self):
        return{
            'clientId': self.client_id,
            'username': self.username,
            'password': self.password,
            'firstName': self.firstname,
            'lastName': self.lastname
        }

    @staticmethod
    def json_parse(json):
        client = Client()
        client.client_id = json["clientId"] if "clientId" in json else 0
        client.username = json["username"]
        client.password = json["password"]
        client.firstname = json["firstname"]
        client.lastname = json["lastname"]
        return client
