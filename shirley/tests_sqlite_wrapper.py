import os
import sys
from sqlalchemy import *
import unittest
from sqlite_wrapper import *
from sqlite_tables import *

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
		self.assertEqual(True, session.query(TodoList).filter_by(lists = q).count())

		
if __name__ == "__main__":
    unittest.main()

	



