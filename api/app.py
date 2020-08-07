from flask import Flask
from flask_restful import Resource, Api, request

app = Flask(__name__)
api = Api(app)


class Hello(Resource):
    def get(self):
        return {'hello': 'world'}

    def post(self):
        json_data = request.json
        message = json_data['message']
        return {"message": message}


api.add_resource(Hello, '/api/hello')

if __name__ == '__main__':
    app.run(debug=True)
