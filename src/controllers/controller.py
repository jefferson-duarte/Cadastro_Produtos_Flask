from flask.views import MethodView


class OlaController(MethodView):
    def get(self):
        return "Ola todos Mundo!!!"
