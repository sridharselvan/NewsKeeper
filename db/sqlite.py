import sqlite3 as sqlite
import os

user_query=(
    '''CREATE TABLE IF NOT EXISTS user ('''
    '''user_idn INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,'''
    '''name varchar(25) NOT NULL,'''
    '''hash1 VARCHAR(64) NOT NULL,'''
    '''email_id varchar(50) NOT NULL UNIQUE,'''
    '''crt_dt DATETIME DEFAULT CURRENT_TIMESTAMP,'''
    '''upd_dt DATETIME DEFAULT CURRENT_TIMESTAMP)'''
)

table_names = [user_query]
db_path = os.getcwd()

def create_table():
    """."""
    filepath = 'noteskepper.db'
    connection = sqlite.connect(filepath)
    cursor = connection.cursor()
    for each in table_names:
        cursor.execute(each)
    connection.commit()


create_table()