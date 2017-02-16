
from sqlite_wrapper import SqliteWrapper
class Shirley(object):
	def shirley_start():
		"""
		This is the main function that runs the program. It is the one
		that will interact with the user. Extensive use of if/else
		instead of the "pythonic" try/except is because of the fact that
		the erros will be expected since this is a CLA. 
		"""

		entries = input(":") #get the entrie 
		command = " ".join(entries.split(" ")[0:2]) #get the command section from the entries
		arguments = " ".join(entries.split(" ")[2:]) #get the arguments
	
		if command == "todo create": #for creating a new list
			if arguments:
				SqliteWrapper.sql_add_list(arguments) 
				Shirley.shirley_start() #return to the base

			else:
				print("INVALID ARGUMENTS. TRY AGAIN")
				Shirley.shirley_start()

		elif command == "todo list":
			SqliteWrapper.sql_view_lists()
			Shirley.shirley_start()

		"""elif command == "list items":
			if arguments:
				if arguments.isdigit():
					arguments = int(arguments)
				else:
					arguments = arguments
				SqliteWrapper.sql_view_items(arguments)
				Shirley.shirley_start()

			else:
				print("INVALID ARGUMENTS. TRY AGAIN")
				Shirley.shirley_start()
	
		elif command == "item add":
			print("USE COMMAND 'todo open' BEFORE USING COMMAND 'item add'")
			Shirley.shirley_start()

		elif command == "todo open":
			if arguments:
				entries_item = input(":")
				command_item =  " ".join(entries_item.split(" ")[0:2])
				arguments_item = " ".join(entries_item.split(" ")[2:])

				if command_item == "item add":
					if arguments_item:
						SqliteWrapper.sql_add_item(arguments, arguments_item)
						Shirley.shirley_start()

					else:
						print("INVALID ARGUMENTSSSSSSS. TRY AGAIN")
						Shirley.shirley_start()
				else:
					print(command_item)
					print("INVALID COMMAND. TRY AGAIN")
					Shirley.shirley_start()

			
			else:
				print("INVALID ARGUMENTS. TRY AGAIN")
				Shirley.shirley_start()
		else:
			print("INVALID COMMANDS. TRY AGAIN")
			Shirley.shirley_start()

Shirley.shirley_start()"""
	

