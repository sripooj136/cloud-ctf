from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_restful.utils import cors
from flask_jwt_extended import jwt_required, get_jwt, create_access_token, JWTManager
from challenges import ch1




class chl1(Resource):
    
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('key', type=str)
        self.parser.add_argument('secret', type=str)

    def options(self):
        return "", 200

    def get(self):
        return "Hello"

    @jwt_required()
    def post(self):
        name = get_jwt()['sub']
        arg = self.parser.parse_args()
        result = ch1(arg['key'], arg['secret'])
        return result


class Register(Resource):
    
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name', type=str)
        self.persons = ['bhavsha2', 'hari','praprama']

    def get(self):
        return "Hello"

    def post(self):
        name = self.parser.parse_args()['name']
        if name in self.persons:
            access_token = create_access_token(identity=name)
            return {'access_token': access_token}, 200
        else:
            return {'message': "Who are you?"}




def create_app():
    # Initialize the flask application
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "SECRET_KEY"
    # Create Restful API with CORS enabled
    api = Api(app)
    jwt = JWTManager(app)
    api.decorators = [cors.crossdomain(origin='*',
        methods=['OPTIONS', 'GET', 'POST'],
        headers='*')]

    api.add_resource(Register, '/register')
    api.add_resource(chl1, '/ch1')
    
    return app

if __name__ == "__main__":
    try:
        app = create_app()
        app.run(debug=True, host="0.0.0.0")
    finally:
        print("Exiting.....")
