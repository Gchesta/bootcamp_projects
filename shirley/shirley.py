
import os
from wrap import SqliteWrapper
from termcolor import colored, cprint
from pyfiglet import figlet_format

os.system("clear")
print("\n")
cprint(figlet_format('Shirley', font='roman'), "yellow")
cprint("\t=======================================", "cyan")
cprint("\tSHIRLEY - Your Pretty Little Secretary", "green")
cprint("\t=======================================", "cyan")
cprint("\n\t\t\tFor help, type -h\n", "white")


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
		if command == "-h":
			cprint("To create a new collection: todo create <collection>", "green" )
			cprint("To add an item to a collection: todo open (<collection>|<collection id>)", "green")
			cprint("\t:item add <item>", "green")
			cprint("To view all collections: todo list", "green")
			cprint("To view all items in a collection: list items (<collection>|<collection id>)", "green")
			cprint("\t:item add <item>", "green")
			Shirley.shirley_start()

		elif command == "quit":
			raise SystemExit(0)

		elif command == "todo create": #for creating a new list
			if arguments:
				if arguments[0] != "\"" and arguments[0] != "\'":
					print("INVALID ARGUMENTS. TRY AGAIN")
					Shirley.shirley_start()
				else:
					arguments = str(arguments[1:-1])
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
					arguments = str(arguments[1:-1]) #will send a list
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
				print("Add an item to collection" + arguments)
				entries_item = input(":") 
				command_item =  " ".join(entries_item.split(" ")[0:2])
				arguments_item = " ".join(entries_item.split(" ")[2:])


				if command_item == "item add":
					if arguments_item:
						if arguments.isdigit():
							arguments = int(arguments) #will send a list id
						else:
							arguments = str(arguments[1:-1]) #will send a list
						arguments_item = str(arguments_item[1:-1])
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
	

