from flask import Blueprint, jsonify
from app.extensions import db
from app.models import QRCode
import uuid
from datetime import datetime

qr_bp = Blueprint('qr_bp', __name__)

@qr_bp.route('/generate_qr', methods=['POST'])
def generate_qr():
    try:
        new_uuid = str(uuid.uuid4())
        qr_record = QRCode(uuid=new_uuid, status='Created', created_at=datetime.utcnow())
        db.session.add(qr_record)
        db.session.commit()

        return jsonify({"uuid": new_uuid}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@qr_bp.route('/ping', methods=['GET'])
def ping():
    return jsonify({"status": "alive"}), 200