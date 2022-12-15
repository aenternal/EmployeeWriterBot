from sqlalchemy import Column, String, Integer, Date, ForeignKey, BIGINT
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Role(Base):

    __tablename__ = 'roles'

    id = Column(Integer, autoincrement=True, primary_key=True, unique=True)
    name = Column(String(50), unique=True)  # Не VARCHAR для того, чтобы можно было спокойно менять СУБД


class User(Base):

    __tablename__ = 'users'

    id = Column(BIGINT, autoincrement=True, primary_key=True, unique=True, nullable=False)
    fio = Column(String)
    datar = Column(Date)

    id_role = Column(Integer, ForeignKey('roles.id'))
