from datetime import datetime
from movieReview import db


class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    review = db.Column(db.String(300))
    username = db.Column(db.String(20))
    mark = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)
