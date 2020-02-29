from sqlalchemy.orm.session import sessionmaker
from sqlalchemy import create_engine
import sqlite3
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "noteskepper.db")

def create_session():
    """."""
    Session = sessionmaker()
    engine = create_engine('sqlite:///{}'.format(db_path), echo = True)
    Session.configure(bind=engine)
    return Session()

