from flask_sqlalchemy import SQLAlchemy


db2 = SQLAlchemy()




def create_all2():
    db2.create_all()
