from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Task(db.Model):
    __tablename__ = 'task'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    status = db.Column(db.Text, nullable=False)
    limit = db.Column(db.Text, nullable=False)
    detail = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

def init_db(app):
    db.init_app(app)
    db.create_all()

def get_all():
    return Task.query.order_by(Task.id).all()

def insert(name, status, limit, detail):
    model = Task(name=name, status=status, limit=limit, detail=detail)
    db.session.add(model)
    db.session.commit()

def delete(id):
    target = Task.query.get(id)
    db.session.delete(target)
    db.session.commit()