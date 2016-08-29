import sqlite3
months={1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June', 7:'July', 8:'August', 9:'September', 10:'October', 11:'November', 12:'December'}
flag=0;
conn=''
print('Welcome to your daily Budget Planner');
def opendb():
	global conn
	try:
		conn=sqlite3.connect('expensecalc.db')

	except:
		print('Database already exist');

opendb();
curs=conn.cursor()

'''Creation of Database table has been done below'''
print('\nMenu:\n1. Show this month\'s data\n2. Add an entry.\n3. Delete an entry.\n4. Create a new table.\n5. Delete a table.\n6. Press h for help\n');
choice = input('Enter your choice(1-6): ');


if choice == 1:

	try:
		curs.execute('Show * from jan')#TODO try function
	except:
		print('Error occured'); #TODO except function
'''
elif choice == 2:
	try:
		#TODO try function
	except:
		#TODO except function

elif choice == 3:
	try:
		#TODO try function
	except:
		#TODO except function
'''
if choice == '4':
	month = input('Enter month name: ');
try:
	curs.execute("create table %month(Date text, Balance real, Break_Fast real, Lunch real, Dinner real, Travel integer, Others real, Total real)")
	print('Table for %s has been created'%month)
except:
	print('Table already exists');