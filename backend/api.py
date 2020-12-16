from flask import Blueprint
from flask_restful import Api, Resource
from models import get_all

api_bp = Blueprint('api', __name__, url_prefix='/api')

class Task(Resource):
  def get(self):
    return [{'id': x.id, 'name': x.name, 'status': x.status, 'limit': x.limit} for x in get_all()]

api = Api(api_bp)
api.add_resource(Task, '/task')