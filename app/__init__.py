from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)
app.config.from_object('config.Config')  # Certifique-se de que isso está presente

db = SQLAlchemy(app)
migrate = Migrate(app, db)
admin = Admin(app, name='MyApp', template_mode='bootstrap3')

from app import routes, models

# Import the User model
from app.models import User

# Add views to the admin interface
admin.add_view(ModelView(User, db.session))
