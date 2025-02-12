from sqlalchemy.dialects.postgresql import UUID, TEXT
from sqlalchemy import func
from db import db

class Book(db.Model):
    __tablename__ = 'book'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=func.uuid_generate_v4())
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    description = db.Column(TEXT(), nullable=False)
    isFavorite = db.Column(db.Boolean, deafault=False)
    isReading = db.Column(db.Boolean, deafault=False)
    isFinished = db.Column(db.Boolean, deafault=False)
