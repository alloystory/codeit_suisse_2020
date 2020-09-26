from flask import Flask, request
from src import logger
from src.controllers import salad_spree, contact_tracing, inventory_management

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

@app.route('/contact_trace', methods = ['POST'])
def contact_trace_route():
    data = request.get_json()
    return contact_tracing.solve(data)

@app.route('/inventory-management', methods = ['POST'])
def inventory_management_route():
    data = request.get_json()
    result = inventory_management.solve(data)
    print("Data: {}".format(data))
    print("Result: {}".format(result.get_json()))
    return result