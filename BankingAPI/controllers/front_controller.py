from controllers import client_controllers, home_controllers


def route(app):
    client_controllers.route(app)
    home_controllers.route(app)
