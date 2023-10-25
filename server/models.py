from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Puzzle(db.Model, SerializerMixin): 
    __tablename__ = 'puzzles'

    id = db.Column(db.Integer, primary_key=True)
    quote = db.Column(db.String(255))  
    created_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now(), nullable=False)  

    def __repr__(self):
        return '<Puzzle %r>' % self.id
