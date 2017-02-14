import os
import sys
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///todo.db')
engine.echo = False  

metadata = MetaData(engine)

Base = declarative_base()
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


class TodoList(Base):
	
	__tablename__ = "todo_list"

	id = Column(Integer, primary_key=True)

	lists = Column(String(250), nullable=False)

	
