import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

load_dotenv()

db = SQLAlchemy()
engine = None


def config_db(app):
    global engine

    db_url = os.getenv("DB_URL")
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Configurar o engine do SQLAlchemy para usar o PostgreSQL
    engine = create_engine(db_url)
    db.init_app(app)
