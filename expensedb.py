from sqlite3 import connect
from calendar import month_name

getMonthName(month_num):
	if month_num.isdigit() == True:
		month = month_name[month_num]
	else:
		month = month_num
	return month

Create_Table(month_num):

	month = getMonthName(month_num)

	Month_DB = """CREATE TABLE IF NOT EXISTS %s
			(ID			integer		PRIMARY KEY,
			date_text	integer		NOT NULL,
			Balance 	integer		NOT NULL,
			Break_Fast	integer		NULL,
			Lunch		integer		NULL,
			Dinner		integer		NULL,
			Travel		integer		NULL,
			Others		integer		NULL,
			Total		integer 	NOT NULL);
			""" %(month)

	return Month_DB_string

print('Welcome to your daily Budget Planner')
conn=connect('expense.db')
curs=conn.cursor()

#Creation of Database table has been done below
print('Menu:')
print("1. Show this month's data")
print("2. Add an entry.")
print("3. Delete an entry.")
print("4. Create a new table.")
print("5. Delete a table.")
print("6. Exit")
choice = input("Enter your choice(1-6): ")


if choice == '1':
	month_num = input("Enter the month you want the data of (name or number) ?")
	month = getMonthName(month_num)
	curs.execute('select * from %s', %(month))

elif choice == '2':
	#TODO

elif choice == '3':
	#TODO

elif choice == '4':
	month= input('Enter month name or number: ')
	curs.execute(Create_Table(month_num))
	print('Table for %s has been created'%(month))

elif choice == '6':
	exit()

else:
	print("Your choice"+choice+"Is not an option, please try again...")
