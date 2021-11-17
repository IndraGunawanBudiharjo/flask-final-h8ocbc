import os
from config import db
from models import Director, Movie

# Delete database file if it exists currently
if os.path.exists('final_proj.db'):
    os.remove('final_proj.db')

# Create the database
db.create_all()

db.session.commit()
