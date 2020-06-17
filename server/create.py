from application import db
from application.models import Students, Teachers

db.drop_all()
db.create_all()
