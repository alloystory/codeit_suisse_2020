from flask import Flask, request
from src import logger
from src.routers.books import router as books_router

app = Flask(__name__)
for handler in logger.get_handlers(log_directory = "./log/"):
    app.logger.addHandler(handler)

@app.route('/')
def index():
    return 'Hello!'

app.register_blueprint(books_router, url_prefix = '/books')