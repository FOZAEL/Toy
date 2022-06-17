from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class Toy(Resource):
    def get(self, name):
        return {'massage': 'Hello {} !'.format(name)}

api.add_resource(Toy, '/hello/<string:name>')

if __name__ == '__main__':
    app.run(debug=True)