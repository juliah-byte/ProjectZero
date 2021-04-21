import logging

from flask import jsonify, request

from Services.client_service import ClientService
from exceptions.resource_not_found import ResourceNotFound
from models.client import Client


def route(app):

    @app.route("/clients", methods=['GET'])
    def get_all_clients():
        return jsonify(ClientService.get_all_clients()), 200

    @app.route("/clients/<client_id>", methods=['GET'])
    def get_client(client_id):
        try:
            client = ClientService.get_client_by_id(int(client_id))
            return jsonify(client.json()), 200
        except ValueError as e:
            logging.DEBUG("Client does not exist")
            return "Client does not exist", 400
        except ResourceNotFound as r:
            logging.debug("Resource Not Found")
            return r.message, 404

    @app.route("/clients", methods=["POST"])
    def post_client():
        client = Client.json_parse(request.json)
        ClientService.create_client(client)
        return jsonify(client.json()), 201

    @app.route("/clients/<client_id>", methods=["PUT"])
    def put_clients(client_id):
        client = Client.json_parse(request.json)
        client.client_id = int(client_id)
        ClientService.update_client(client)
        return jsonify(client.json()), 200

    @app.route("/clients/<client_id>", methods=["DELETE"])
    def del_client(client_id):
        try:
            return 'Deletion Successful', 204
        except ValueError as e:
            e.message("Client does not exist.")
        except ResourceNotFound as r:
            r.message()

    @app.route("/clients/<client_id>", methods=["PATCH"])
    def patch_client(client_id):
        return



