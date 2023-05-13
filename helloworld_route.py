from flask_restful_app import Resource

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}
