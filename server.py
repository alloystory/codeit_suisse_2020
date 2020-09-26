import os
from src.app import app

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 3000 if not "PORT" in os.environ else os.environ.get("PORT")

    app.run(host = host, port = port)