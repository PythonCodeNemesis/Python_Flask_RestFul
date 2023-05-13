from flask import Flask
from flask_restful_app import Api
from helloworld_route import HelloWorld

app = Flask(__name__)
api = Api(app)

api.add_resource(HelloWorld, '/hello')

if __name__ == '__main__':
    app.run()
