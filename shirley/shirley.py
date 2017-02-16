
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

		elif command == "list items": #this control flow must chek for list/list_id
			if arguments:
				if arguments.isdigit():
					arguments = int(arguments) #will send a list id
				else:
					arguments = arguments #will send a list
				SqliteWrapper.sql_view_items(arguments)
				Shirley.shirley_start()

			else:
				print("INVALID ARGUMENTS. TRY AGAIN") #reject the invalid argumenst
				Shirley.shirley_start()
	
		elif command == "item add": #a user may accidentally enter "item add" before "todo open"
			print("USE COMMAND 'todo open' BEFORE USING COMMAND 'item add'") #check for the above error
			Shirley.shirley_start()

		elif command == "todo open": #check the todo open command
			if arguments:
				entries_item = input(":") 
				command_item =  " ".join(entries_item.split(" ")[0:2])
				arguments_item = " ".join(entries_item.split(" ")[2:])

				if command_item == "item add":
					if arguments_item:
						if arguments.isdigit():
							arguments = int(arguments) #will send a list id
						else:
							arguments = arguments #will send a list
						SqliteWrapper.sql_add_item(arguments, arguments_item)
						Shirley.shirley_start()

					else:
						print("INVALID ARGUMENTS. TRY AGAIN")
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

Shirley.shirley_start()
	

