#!/usr/bin/python

from sqlite3 import connect
from sqlite3 import OperationalError, IntegrityError

from calendar import month_name

conn=connect('expensedb')
curs=conn.cursor()

def getMonthName(month_input):						#Function to get month name
        '''
        Input Handling for Month number and Month name
        '''
        if month_input.isalpha():                                       #Condition to check if string contains Alphabets or Digits
                return month_input
        else:
                month = int(month_input)
                month = month_name[month]
                return month


def fetchdata(month):							#Function to fetch data from table
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


def exitcall():			#To close the database connection and take exit from the program.

	
	print('Thanks for your time!')
	conn.close()
	exit()
	



def deltable(month):

	try:
		del_table=curs.execute('DROP TABLE '+month)
		print('Table has been deleted')
		conn.commit()
	except OperationalError as drop_error:
		print(drop_error.args[0])


def createtable(month):

	curs.execute('''CREATE TABLE IF NOT EXISTS %s
		(ID                             integer                 PRIMARY KEY,
		date_text               integer                 NOT NULL,
		Balance                 integer                 NOT NULL,
		Break_Fast              integer                 NULL,
		Lunch                   integer                 NULL,
		Dinner                  integer                 NULL,
		Travel                  integer                 NULL,
		Others                  integer                 NULL,
		Total                   integer                 NULL)
		'''%(month)
                                               ) 
		#month_sql = Create_Table(month)
	conn.commit()
	print("Table for %s has been created" %(month))


