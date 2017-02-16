import os
import sys
from sqlalchemy import *
import unittest
from wrap import *
from tables import *

engine = create_engine('sqlite:///todo.db')
engine.echo = False  

metadata = MetaData(engine)

Base = declarative_base()
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

class TestSqliteWrapper(unittest.TestCase):
	"""A class for testing the functioning of the functions @sqlite_wrapper"""
	def test_sql_add_list(self):
		q = "Tests to Run"
		sql_add_list(q)
		self.assertEqual(True, session.query(TodoList).filter_by(lists = q).count() >= 1)

	def test_sql_add_item_by_list_name(self):
		q = "Tests to Run"
		r = "Check test_sql_add_list"
		sql_add_item(q, r)
		self.assertEqual(True, session.query(Items).filter_by(items = r).count() >= 1)


if __name__ == "__main__":
    unittest.main()

	




