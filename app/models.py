from datetime import datetime
from app import db

class Thought(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(500), nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    mood = db.Column(db.String(50))  # Optional: add mood tracking
    category = db.Column(db.String(50))  # Optional: add categorization

    def __repr__(self):
        return f'<Thought {self.id}: {self.content[:20]}...>'