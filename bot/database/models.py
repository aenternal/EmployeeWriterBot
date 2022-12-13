from sqlalchemy import Column, String, Integer, BigInteger, Date, ForeignKey
from bot.database.db import Base


class Role(Base):

    __tablename__ = 'Roles'

    id = Column(Integer, autoincrement=True, primary_key=True, unique=True)
    name = Column(String(50), unique=True)  # Не VARCHAR для того, чтобы можно было спокойно менять СУБД


class User(Base):

    __tablename__ = 'Users'

    id = Column(BigInteger, autoincrement=True, primary_key=True, unique=True)
    fio = Column(String)
    datar = Column(Date)

    id_role = Column(Integer, ForeignKey('Roles.id'))

