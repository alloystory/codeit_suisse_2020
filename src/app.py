from flask import Flask, request
from src import logger
from src.controllers import salad_spree

app = Flask(__name__)
for handler in logger.get_handlers(log_directory = "./log/"):
    app.logger.addHandler(handler)

@app.route('/')
def index():
    return 'Hello!'

@app.route('/salad-spree', methods = ['POST'])
def salad_spree_route():
    data = request.get_json()
    return salad_spree.solve(data)