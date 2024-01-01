# models.py
from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base

# Define the SQLAlchemy engine and create a SQLite database file
engine = create_engine('sqlite:///todo.db', echo=True)

# Define the base class for declarative class definitions
Base = declarative_base()

# Define a simple table model
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    task = Column(String(100), nullable = False)
    points = Column(Integer, default=10)

# Create the table in the database
Base.metadata.create_all(engine)
