from flask import Flask
from dotenv import load_dotenv
import os
import urllib.parse

from .extensions import db, csrf  # ✅ import from extensions

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key')

    params = urllib.parse.quote_plus(os.getenv("AZURE_SQL_CONNECTION_STRING"))
    app.config['SQLALCHEMY_DATABASE_URI'] = f"mssql+pyodbc:///?odbc_connect={params}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    csrf.init_app(app)

    from . import models
    from .qr_routes import qr_bp
    app.register_blueprint(qr_bp)

    return app