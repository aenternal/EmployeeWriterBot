from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from bot.core.config import DATABASE_URL


engine = create_engine(DATABASE_URL, echo=True, encoding='utf-8')

session = sessionmaker(
    engine, class_=Session, expire_on_commit=False
)

Base = declarative_base()
