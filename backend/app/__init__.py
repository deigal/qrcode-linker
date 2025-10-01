from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from dotenv import load_dotenv
import os
import urllib.parse

load_dotenv()

db = SQLAlchemy()
csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key')

    # Azure SQL connection
    params = urllib.parse.quote_plus(os.getenv("AZURE_SQL_CONNECTION_STRING"))
    app.config['SQLALCHEMY_DATABASE_URI'] = f"mssql+pyodbc:///?odbc_connect={params}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    csrf.init_app(app)

    # Register routes (once created)
    # from .routes import main
    # app.register_blueprint(main)

    return app