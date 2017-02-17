import os
import sys
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
#from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
#from sqlalchemy.ext.automap import automap_base
from tables import *
from terminaltables import AsciiTable
#from shirley import Shirley

#declarations
engine = create_engine('sqlite:///todo.db')
engine.echo = False  

metadata = MetaData(engine)

Base = declarative_base()
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

class SqliteWrapper(object):

	def __init__ (self):
		pass

	def sql_add_list(to_do_list):
		"""A function to add lists to the todo_list table"""
		new_list = TodoList(lists = to_do_list)
		session.add(new_list)
		session.commit()
		print("Successfully created a new collection called '" + to_do_list + "'")
		

	def sql_add_item(to_do_list, item):
		"""A function to add items to a to-do list"""
		if to_do_list != None and item != None:
			try:
				if type(to_do_list) != int:
					f = session.query(TodoList).filter_by(lists = to_do_list).one()
					f_id = f.list_id
				else:
					f_id = to_do_list
				new_item = Items(items = item, list_id = f_id)
				session.add(new_item)
				session.commit()
				print("Successfully added a new item called '" + str(item) + "' " + "to collection " + "'" + str(to_do_list) + "'")
			except Exception:
				print("THERE WAS AN ERROR PROCESSING YOUR REQUEST. TRY AGAIN")

	def sql_view_lists():
		"""A function to view all the to-do lists"""
		my_lists = session.query(TodoList).all()
		data = [["No.", "Lists"]]
		for my_list in my_lists:
			data.append([my_list.list_id, my_list.lists])
		table = AsciiTable(data)
		print(table.table)
		
	def sql_view_items(to_do_list):
		"""A function to view the data in a to-do list"""
		if to_do_list != None:
			try:
				if type(to_do_list) != int:
					f = session.query(TodoList).filter_by(lists = to_do_list).one()
					f_id = f.list_id
				else:
					f_id = to_do_list
				my_items = session.query(Items).filter_by(list_id = f_id).all()
				counter = 1
				data = [["No.", to_do_list]]
				for my_item in my_items:
					data.append([counter, my_item.items])
					counter += 1
				table = AsciiTable(data)
				print(table.table)
			except Exception:
				print("THERE WAS AN ERROR PROCESSING YOUR REQUEST. TRY AGAIN")


		