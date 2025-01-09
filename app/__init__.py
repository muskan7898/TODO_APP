from flask import Flask
from app.database import mongo
from app.routes import todo_bp as todo



def create_app():
    app = Flask(__name__)

    ''' MongoDB Configuration '''
    app.config['MONGO_URI'] = 'mongodb://localhost:27017/todo_db'

    '''Initialize MongoDB '''
    # pymango.init_app(app) or 
    mongo.init_app(app)

    '''Register Blueprint'''
    app.register_blueprint(todo, url_prefix='/api')


    @app.route("/")
    def hello_world():
        return "<p>Hello, World!</p>"

    return app
    