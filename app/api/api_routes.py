from flask import jsonify
from app import db
from app.models import TodoTask
from . import bp

@bp.route('/api/tasks', methods=['GET'])
def get_tasks():
    tasks = TodoTask.query.all()
    return jsonify([task.to_dict() for task in tasks])
