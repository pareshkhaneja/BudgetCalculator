from sqlite3 import connect
from sqlite3 import OperationalError, IntegrityError
from calendar import month_name
from datetime import datetime

def getMonthName(month_num):
    '''
    convert user inputted month name or number
    to upercase month name
    '''
        if month_num.isdigit() == True:
                month_num=int(month_num)
                month = month_name[month_num]
        else:
                month = month_num
        return month.upper()

def Create_Table(month_num):
    '''
    Generate SQL statement for table creation
    '''

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

print("Welcome to your daily Budget Planner")
conn=connect('expense.db')
curs=conn.cursor()
while (True):
    print("Menu:")
    print("1. Show this month's data")
    print("2. Add an entry.")
    print("3. Delete an entry.")
    print("4. Create a new table.")
    print("5. Delete a table.")
    print("6. Exit")
    choice = int(input("Enter your choice(1-6): "))

    if choice == 1:
            month_num = input("Enter the month you want the data of (name or number) : ")
            month = getMonthName(month_num)

            try:
                    response = curs.execute("select * from ?",(month))
                    for row in response:
                        #TODO: make printed data look pretty.
                        print(row)
            except OperationalError as e:
                    print(e.args[0])

    elif choice == 2:
            month_num = input("Enter the month you want to add data of (name or number) : ")
            month = getMonthName(month_num)
            try:
                balance = input("Enter balance")
                today = datetime.today.date()
                #TODO: handle all elements
                    curs.execute('''INSERT INTO ? (balance, date_text) VALUES(?,?) ''', (month, balance, today))
            except IntegrityError as integ_error:
                   var = integ_error.args[0].rsplit(".",1)[-1]
                   print("Entry with the same ",var," Already exists")

    elif choice == 4:
            month_num= str(input("Enter month name or number: "))
            month = getMonthName(month_num)
            month_sql = Create_Table(month_num)
            curs.execute(month_sql)
            conn.commit()
            print("Table for %s has been created" %(month))

    elif choice == 5:
        month_num = input("Enter name of month or number")
        month = getMonthName(month_num)
        try:
            curs.execute('DROP TABLE IF EXISTS '+month)
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
