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

class Items(Base):
	
	__tablename__ = "item_list"

	id = Column(Integer, primary_key=True)

	
Base.metadata.create_all(engine)

class Action(object):
	def __init__(self, to_do_list):
		pass

	def sql_add_list(to_do_list):
		new_list = TodoList(lists = to_do_list)
		session.add(new_list)
		session.commit()

	def sql_add_item(to_do_list, item):
		new_item = Items(items = item)
		session.add(new_item)
		session.commit()

		pass
