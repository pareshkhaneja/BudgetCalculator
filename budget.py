from calendar import month_name
from datetime import datetime
import queryfunctions


print("Welcome to your daily Budget Planner")
while (True):
        print("Menu:")
        print("1. Show data")
        print("2. Add an entry.")
        print("3. Delete an entry.")
        print("4. Create a new table.")
        print("5. Delete a table.")
        print("6. Exit")
        choice = int(input("Enter your choice(1-6): "))

        if choice == 1:                 #To show data of a table
                        month_num = str(input("Enter the month number you want the data of : "))
                        month = queryfunctions.getMonthName(month_num)
                        queryfunctions.fetchdata(month)

        elif choice == 2:                                       #To add an entry into a table
                        month_num = input("Enter the month you want to add data of (name or number) : ")
                        month = queryfunctions.getMonthName(month_num)
                        try:

                                today = datetime.today()
                                data = input('Press 1/2/3/4/5/6 to enter Balance/BreakFast/Lunch/Dinner/Travel/Others data else press enter to go back to previous menu')
                                #TODO: handle all elements
                                if data == '1':
                                        Balance_input = input("Enter your balance : ")
                                        insertquery(month,Balance,today,Balance_input)

                                elif data== '2':
                                        BF_input = input('How much for Breakfast? : ')
                                        insertquery(month,Break_Fast,today,BF_input)

                                elif data== '3':
                                        Lunch_input = input('How much for Lunch? : ')
                                        insertquery(month,Lunch,today,Lunch_input)

                                elif data== '4':
                                        Dinner_input = input('How much for Dinner? : ')
                                        insertquery(month,Dinner,today,Dinner_input)
				elif data== '5':
                                        Travel_input = input('How much for travelling? : ')
                                        insertquery(month,Travel,today,Travel_input)

                                elif data== '6':
                                        Others_input = input('Tell me Other expense? : ')
                                        insertquery(month,Balance,today,Balance_input)
					
                                conn.commit()
                        except IntegrityError as integ_error:
                                   print(integ_error)
                                   var = integ_error.args[0].rsplit(".",1)[-1]
                                   print("Entry with the same",var,"already exists")

        elif choice == 3:                       #To delete an entry
                        month_num= str(input("Enter month name or number: "))
                        month = queryfunctions.getMonthName(month_num)
                        #TODO

        elif choice == 4:                       #To create a new table
                        month_num= str(input("Enter month name or number: "))
                        month = queryfunctions.getMonthName(month_num)
			queryfunctions.createtable(month)
        elif choice == 5:
                month_num = input("Enter name of month or number")
                month = queryfunctions.getMonthName(month_num)
                queryfunctions.deltable(month)
        elif choice == 6:                       #Close the database connection
                queryfunctions.exitcall()

        else:
                        print("Your choice "+str(choice)+" is not an option, please try again...")


                                                                                                      
