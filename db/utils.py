from sqlalchemy.exc import SQLAlchemyError
from db import create_session


class AutoSession(object):

    def __init__(self):
        self.session = create_session()

    def __enter__(self):
        # make a database connection and return it
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            self.session.commit()
        except SQLAlchemyError:
            self.session.rollback()
        finally:
            self.session.close()

def to_dict(query_obj):
    """."""
    return [obj._asdict() for obj in query_obj]
