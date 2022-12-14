from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///./database/app.db', echo=True, encoding='utf-8')

Session = sessionmaker(engine)
