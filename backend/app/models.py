from . import db
import uuid
from datetime import datetime

class QRCode(db.Model):
    __tablename__ = 'qr_codes'

    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(36), unique=True, nullable=False, default=lambda: str(uuid.uuid4()))
    status = db.Column(db.String(20), nullable=False, default='Created')  # Created, Printed, Linked
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    linked_at = db.Column(db.DateTime, nullable=True)

    # Relationship to StudentLink
    student_link = db.relationship('StudentLink', backref='qr_code', uselist=False)

class StudentLink(db.Model):
    __tablename__ = 'student_links'

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String(50), nullable=False)
    qr_code_id = db.Column(db.Integer, db.ForeignKey('qr_codes.id'), nullable=False)
    submitted_at = db.Column(db.DateTime, default=datetime.utcnow)