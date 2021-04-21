
def route(app):
    @app.route("/", methods=['GET', 'POST'])
    def welcome():
        return "Welcome to my Banking API"
