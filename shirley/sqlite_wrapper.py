import os
import sys
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
#from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
#from sqlalchemy.ext.automap import automap_base
from sqlite_tables import *


#declarations
engine = create_engine('sqlite:///todo.db')
engine.echo = False  

metadata = MetaData(engine)

Base = declarative_base()
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


def sql_add_list(to_do_list):
	"""A function to add lists to the todo_list table"""
	new_list = TodoList(lists = to_do_list)
	session.add(new_list)
	session.commit()

def sql_add_item(to_do_list, item):
	f = session.query(TodoList).filter_by(lists = to_do_list).one()
	f_id = f.list_id
	#new_list = TodoList(lists = to_do_list)
	new_item = Items(items = item, list_id = f_id)
	session.add(new_item)
	session.commit()

def sql_view_lists():
	my_lists = session.query(TodoList).all()
	for my_list in my_lists:
		print(str(my_list.list_id) + ". " + my_list.lists)



"""def sql_view_items(to_do_list):
	f = session.query(TodoList).filter_by(lists = to_do_list).one()
	f_id = f.list_id
	my_items = session.query(Items).filter_by(list_id = f_id).all()
	counter = 1
	print(to_do_list)
	for my_item in my_items:
		print(str(counter) + ". " + my_item.items)
		counter += 1"""

"""sql_add_item("Jobs to Apply To", "Teaching - TSC")
sql_add_item("Books to Read", "The Souls of Black Folks")
sql_add_item("Jobs to Apply To", "KQ Pilot")
sql_add_item("Books to Read", "The Government Inspector")
sql_add_item("Books to Read", "Midshipman Easy")
sql_add_item("Jobs to Apply To", "Andela Fellowship")
sql_add_item("Books to Read", "Decolonising the Mind")
sql_add_item("Books to Read", "You Don't Know JS")
sql_add_item("Books to Read", "Education for Self-Reliance")
sql_add_item("Books to Read", "Utenzi wa Mwana Kupona")
sql_add_item("Books to Read", "Bible")

sql_view_items("Books to Read")"""

sql_view_lists()