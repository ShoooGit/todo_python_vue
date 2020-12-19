from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from models import get_all, insert

api_bp = Blueprint('api', __name__, url_prefix='/api')

class Task(Resource):
  def get(self):
    return [{'id': x.id, 'name': x.name, 'status': x.status, 'limit': x.limit} for x in get_all()]

  def post(self):
    insert(request.json["name"].split())
    result = {
        "results": request.json["name"].split()
    }
    return result

api = Api(api_bp)
api.add_resource(Task, '/task')