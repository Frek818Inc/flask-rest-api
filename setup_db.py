from flask_sqlalchemy import SQLAlchemy
from main import app
import settings

app.config["SQLALCHEMY_DATABASE_URI"] = settings.DB_URI

dv = SQLAlchemy(app)

import resources

dv.create_all()
