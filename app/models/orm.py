from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import MetaData

convention = {
  "pk": "pk_%(table_name)s"
}

Base = declarative_base()
Base.metadata = MetaData(naming_convention=convention)


class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    phone = Column(String(10))
