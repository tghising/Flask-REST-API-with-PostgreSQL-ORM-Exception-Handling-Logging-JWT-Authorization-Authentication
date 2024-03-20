from flask import jsonify
from flask_restful import Resource


class Home(Resource):
    def get(self):
        return jsonify(message="Welcome to the Home Page: Object Detection")

    def post(self):
        return jsonify(message="POST method not allowed for this endpoint"), 405

    def put(self):
        return jsonify(message="PUT method not allowed for this endpoint"), 405

    def delete(self):
        return jsonify(message="DELETE method not allowed for this endpoint"), 405
