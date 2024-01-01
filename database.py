# database.py
from sqlalchemy.orm import sessionmaker
from models import engine, Base, User

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()
