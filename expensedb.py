from sqlite3 import connect
from sqlite3 import OperationalError, IntegrityError
from calendar import month_name
from datetime import datetime

def getMonthName(month_num):
        if month_num.isdigit() == True:                                 #To check whether the passed string is number or not
                month_num=int(month_num)
                month = month_name[month_num]
        else:
                month = month_num
        return month.upper()

def Create_Table(month_num):

        month = getMonthName(month_num)

        Month_DB = """CREATE TABLE IF NOT EXISTS %s
                        (ID             integer         PRIMARY KEY,
                        date_text       date            NOT NULL,
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
choice = int(input("Enter your choice(1-6): "))

if choice == 1:                         #Abstract Function to Show this month's Data
        month_num = input("Enter the month you want the data of (name or number) ?")    #Conversion of int input into string
        month = getMonthName(month_num)

#Handling of Exception, if table doesn't exist.
        try:
                response = curs.execute("select * from ?",(month))
                for row in response:
                    #TODO: make printed data look pretty.
                    print(row)
        except OperationalError as e:
                print(e.args[0])

elif choice == 2:                               #Abstract Fumction to add an Entry
        month_num = input('Enter the month you want to add data of (name or number) ?')
        month = getMonthName(month_num)
        try:
            balance = input("Enter balance")
            today = datetime.today.date()
            #TODO: handle all elements
            #TODO: implement datetime element as a date entry
                curs.execute('''INSERT INTO ? (balance, date_text) VALUES(?,?) ''', (month, balance, today))
        except IntegrityError as integ_error:
               var = integ_error.args[0].rsplit(".",1)[-1]
               print("Entry with the same ",var," Already exists")

elif choice == 4:                               #Abstract Function to create a new table
        month_num= str(input('Enter month name or number: '))
        month = getMonthName(month_num)
        month_sql = Create_Table(month_num)
        curs.execute(month_sql)
        conn.commit()
        print('Table for %s has been created' %(month))

elif choice == 6:
        exit()

else:
        print("Your choice "+choice+" is not an option, please try again...")
