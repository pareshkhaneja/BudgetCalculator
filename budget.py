from sqlite3 import connect
from sqlite3 import OperationalError, IntegrityError
from calendar import month_name
from datetime import datetime

def getMonthName(month_num):
	'''
	convert user input month name or number
	to upercase month name
	'''
	if month_num.isdigit() == True:
		month_num=int(month_num)
		month = month_name[month_num]
	else:
		month = month_num
	return month.upper()

def Create_Table(month_num):
	
	'''Generate SQL statement for table creation
	'''

	month = getMonthName(month_num)
	
	Month_DB = """CREATE TABLE IF NOT EXISTS ?
						(ID				integer			PRIMARY KEY,
						date_text		integer			NOT NULL,
						Balance			integer			NOT NULL,
						Break_Fast		integer			NOT NULL,
						Lunch			integer			NOT NULL,
						Dinner			integer			NOT NULL,
						Travel			integer			NOT NULL,
						Others			integer			NOT NULL,
						Total			integer			NOT NULL,);
						""",(month)

	return Month_DB 

print("Welcome to your daily Budget Planner")
conn=connect('G:\Git\Python Work\Budget Analyzer\expense.db')
curs=conn.cursor()
while (True):
	print("Menu:")
	print("1. Show data")
	print("2. Add an entry.")
	print("3. Delete an entry.")
	print("4. Create a new table.")
	print("5. Delete a table.")
	print("6. Exit")
	choice = int(input("Enter your choice(1-6): "))

	if choice == 1:			#To show data of a table
			month_num = input("Enter the month you want the data of (name or number) : ")
			month = getMonthName(month_num)
			try:
				response = curs.execute("SELECT * FROM '%s'"%month)
				table_list=(curs.fetchall())
				l=sum(table_list,())
				list1=list(l)
				if(not table_list):
					
					print('Table is empty')
				else:
					print('\n')
					for i in list1:
						print(i)
					
			except OperationalError as e:
				print(e.args[0])
				

	elif choice == 2:					#To add an entry into a table
			month_num = input("Enter the month you want to add data of (name or number) : ")
			month = getMonthName(month_num)
			try:
				
				today = datetime.today()
				data = input('Press 1/2/3/4/5/6 to enter Balance/BreakFast/Lunch/Dinner/Travel/Others data else press enter to exit')
				#TODO: handle all elements
				if data == 1:
					balance = input("Enter balance")
				elif data==2:
					BF = input('How much for Breakfast?')
				elif data==3:
					Lunch = input('How much for Lunch?')
				elif data==4:
					Dinner = input('How much for Dinner?')
				elif data==5:
					Travel = input('How much for travelling?')
				elif data==6:
					Others = input('Tell me Other expense?')
				#curs.execute('''INSERT INTO %s (?, date_text) VALUES (?,?)'''%month,(, today))
				#NOT NULL constraint failed. month.Total
				conn.commit()
			except IntegrityError as integ_error:
				   print(integ_error)
				   var = integ_error.args[0].rsplit(".",1)[-1]
				   print("Entry with the same",var,"already exists")

	elif choice == 3:			#To delete an entry
			month_num= str(input("Enter month name or number: "))
			month = getMonthName(month_num)
			#TODO
	
	elif choice == 4:			#To create a new table
			month_num= str(input("Enter month name or number: "))
			month = getMonthName(month_num) 
			conn.execute('''CREATE TABLE IF NOT EXISTS %s
						(ID				integer			PRIMARY KEY,
						date_text		integer			NOT NULL,
						Balance			integer			NOT NULL,
						Break_Fast		integer			NULL,
						Lunch			integer			NULL,
						Dinner			integer			NULL,
						Travel			integer			NULL,
						Others			integer			NULL,
						Total			integer			NULL)
						'''%(month)
						)
			month_sql = Create_Table(month)						
			conn.commit()
			print("Table for %s has been created" %(month))

	elif choice == 5:
		month_num = input("Enter name of month or number")
		month = getMonthName(month_num)
		try:
			del_table=curs.execute('DROP TABLE '+month)
			print('Table has been deleted')
			conn.commit()
		except OperationalError as drop_error:
			print(drop_error.args[0])
			
	elif choice == 6:
			break

	else:
			print("Your choice "+choice+" is not an option, please try again...")
#Close the database connection
conn.close()
#Sample data to show how git works