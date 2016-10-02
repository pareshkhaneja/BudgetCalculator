from sqlite3 import connect
from calendar import month_name

def getMonthName(month_num):
        if month_num.isdigit() == True:                                 #To check whether the passed string is number or not
                month_num=int(month_num)
                month = month_name[month_num]
        else:
                month = month_num
        return month

def Create_Table(month_num):

        month = getMonthName(month_num)

        Month_DB = """CREATE TABLE IF NOT EXISTS %s
                        (ID                     integer         PRIMARY KEY,
                        date_text       integer         NOT NULL,
                        Balance         integer         NOT NULL,
                        Break_Fast      integer         NULL,
                        Lunch           integer         NULL,
                        Dinner          integer         NULL,
                        Travel          integer         NULL,
                        Others          integer         NULL,
                        Total           integer         NOT NULL);
                        """ %(month)

        return Month_DB

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

if choice == 1:                         #Abstract Function to Show this month's Data
        month_num = str(input("Enter the month you want the data of (name or number) ?"))       #Conversion of int input into string
        month = getMonthName(month_num)

#Handling of Exception, if table doesn't exist.
        try:
                curs.execute('select * from %s'%(month))
        except:
                print('Table doesn\'nt exist! Kindly add the table first.')

elif choice == 2:                               #Abstract Fumction to add an Entry
        month_num = str(input('Enter the month you want to add data of (name or number) ?'))
        month = getMonthName(month_num)
        try:
                curs.execute('SELECT * from sql_master WHERE name = %s and type = "table"'%(month)) #Not working. Hence, TODO.
        except:
                print('Table doesn\'t exist!')

elif choice == 4:                               #Abstract Function to create a new table
        month_num= str(input('Enter month name or number: '))
        month = getMonthName(month_num)
        curs.execute(Create_Table(month_num))
        print('Table for %s has been created'%(month))

elif choice == 6:
        exit()

else:
        print("Your choice"+choice+"Is not an option, please try again...")
