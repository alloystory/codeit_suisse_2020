from flask import Flask, request
from src import logger
from src.controllers import salad_spree, contact_tracing, \
    inventory_management, revisit_geometry, cluster, intelligent_farming, \
    social_distancing, fruit_basket

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
    return inventory_management.solve(data)

@app.route('/revisitgeometry', methods = ['POST'])
def revisit_geometry_route():
    data = request.get_json()
    return revisit_geometry.solve(data)

@app.route('/cluster', methods = ['POST'])
def cluster_route():
    data = request.get_json()
    return cluster.solve(data)

@app.route('/intelligent-farming', methods = ['POST'])
def intelligent_farming_route():
    data = request.get_json()
    return intelligent_farming.solve(data)

@app.route('/social_distancing', methods = ['POST'])
def social_distancing_route():
    data = request.get_json()
    return social_distancing.solve(data)

@app.route('/fruitbasket', methods = ['POST'])
def fruit_basket_route():
    data = request.get_data()
    return fruit_basket.solve(data)