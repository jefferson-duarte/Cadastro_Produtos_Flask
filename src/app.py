from flask import Flask
from src.routes.routes import *

app = Flask(__name__)

app.add_url_rule(routes['ola_route'], view_func=routes['olacontroller'])

app.register_error_handler(routes['not_found_route'], routes['not_found_controller'])