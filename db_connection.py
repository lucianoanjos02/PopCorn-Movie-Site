import config
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker


engine = db.create_engine(f'{config.MYSQL_ENGINE}://{config.MYSQL_USER}:{config.MYSQL_PASSWORD}@{config.MYSQL_HOST}:{config.MYSQL_PORT}/{config.MYSQL_DB}', echo=False)
Session = sessionmaker(bind=engine)
session = Session()