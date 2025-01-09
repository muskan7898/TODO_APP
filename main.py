from app import create_app
from flask_pymongo import PyMongo
import os

app = create_app()

app.config["MONGO_URI"] = os.environ.get(
    "MONGO_URL",
    "LOCAL_MONGO_CONNECTION"
)

mongo = PyMongo(app)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
