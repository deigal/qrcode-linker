from flask import Blueprint, send_file
from app.extensions import db  # ✅ import from extensions
from app.models import QRCode
import uuid
import qrcode
from io import BytesIO
from datetime import datetime

qr_bp = Blueprint('qr_bp', __name__)

@qr_bp.route('/generate_qr', methods=['POST'])
def generate_qr():
    new_uuid = str(uuid.uuid4())
    qr_record = QRCode(uuid=new_uuid, status='Created', created_at=datetime.utcnow())
    db.session.add(qr_record)
    db.session.commit()

    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(new_uuid)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    img_io = BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)

    return send_file(
        img_io,
        mimetype='image/png',
        as_attachment=True,
        download_name='qr.png'
)