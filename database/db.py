from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///./database/app.db', echo=True,
                       encoding='utf-8', connect_args={'check_same_thread': False})

Session = sessionmaker(engine)
