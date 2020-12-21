from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from models import get_all, insert, delete

api_bp = Blueprint('api', __name__, url_prefix='/api')

class Task(Resource):
  def get(self):
    return [{'id': x.id, 'name': x.name, 'status': x.status, 'limit': x.limit} for x in get_all()]

  def post(self):
    insert(
      request.json["name"],
      request.json["status"],
      request.json["limit"],
      request.json["detail"]
    )
    name = request.json["name"]
    return name

  def delete(self):
    print("shuto")
    req = request.get_json(force=True)
    print(req)
    print(type(req))
    print(req['id'])
    delete(req['id'])

api = Api(api_bp)
api.add_resource(Task, '/task')