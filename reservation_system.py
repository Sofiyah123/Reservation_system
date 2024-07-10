import csv
import os
from datetime import datetime
lists_of_table = [
    {'table':1, 'seats':6},
    {'table':2, 'seats':5},
    {'table':3, 'seats':4},
    {'table':4, 'seats':7},
    {'table':5, 'seats':8},
    {'table':6, 'seats':7}
]
# available_tables = [table for table in lists_of_table if table['seats'] >]
reservations_file = 'reservations_file.csv'

def view_tables(lists_of_table):
    for table in lists_of_table:
        print(table)

# reservations = {}
available_tables = []
def make_reservation(lists_of_table, reservations_file):
    name = input('Enter your Name: ')
    name = name.lower()
    contact  = input('Enter your Contact Number ')
    party_size = int(input('Enter Number of People: '))
    start_time =  input('Enter Reservation Start Time (HH:MM): ')
    end_time =  input('Enter Reservation End time (HH:MM): ')
    date =  input('Enter reservation Date (YYYY-MM-DD): ')

    #available_tables variable stores the lists of tables that are available for reservation
    available_tables = [table for table in lists_of_table if table['seats'] >= party_size]
    if not available_tables:
        print("No available tables for your party size")
        return
    
    print("Available tables: ")
    table_numbers = [table['table']for table in available_tables]
    for table in available_tables:
        print(f"Table {table['table']} - Seats {table['seats']}")
    

    table_number = int(input("Enter the desired table number: "))
    if table_number not in table_numbers:
            print("invalid table number")
            return
    
    new_row = [name, contact, party_size, start_time, end_time, date, table_number]

    file_exists = os.path.isfile(reservations_file)
    header_needed = True

    if file_exists:
    #This line checks if a file specified by reservations_file exists and assigns the result (True or False) to file_exists
        with open(reservations_file, mode='r', newline='') as file:
            #this line create a CSV reader object that will be used to read data from the file
            reader = csv.reader(file)

            headers = next(reader, None)
            if headers and headers == ["Name", "Contact", "Party Size", "Start time","End time","Date", "Table Number"]:
                header_needed = False

    try:
        with open(reservations_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            if header_needed:
                # print("Writing header row...")
                writer.writerow(["Name", "Contact", "Party Size", "Start time","End time","Date", "Table Number"])
            # print("Writing new row...")
            writer.writerow(new_row)
        print(f"The table {table_number} has been successfully reserved for {name}")
    except Exception as e:
        print(f"Error saving reservation:{e}")
    # print(reservations)
    
def view_reservations(reservations_file):
    #This line checks if a file specified by reservations_file exists and assigns the result (True or False) to file_exists
        try:    
            with open(reservations_file, mode='r', newline='') as file:
                #this line creates a CSV reader object that can iterate over lines in the CSV file specified by file
                reader = csv.reader(file)
                header = next(reader,None)
                print(f"Here is the lists of reservations that has been made:")
                print(header)
                for row in reader:
                    print(f"{row[header.index('Name')]},{row[header.index('Contact')]},\
                          {row[header.index('Party Size')]},{row[header.index('Start time')]},\
                          {row[header.index('End time')]},{row[header.index('Date')]},\
                          {row[header.index('Table Number')]}")
        except Exception as e:
            print(f"Error viewing reservation:{e}")
                
# calling the functions that was created
# The parameter table_number serves as the unique id that is been used to 
# identify the particular reservation what will be deleted

def cancel_reservation(reservations_file):
    table_number = int(input("Enter table number that needs to be deleted "))
    name = input("Enter Name of the Table ")
    name = name.lower()
    with open(reservations_file, mode='r', newline='') as file:      
        reader = csv.reader(file)
        header = next(reader,None)    
        reservations = list(reader)
        # print("reader is", reader)
        row_to_remove =[reservations.remove(reserved_table) for reserved_table in reservations 
                                   if(int(reserved_table[header.index('Table Number')]) == table_number) and 
                                   ((reserved_table[header.index('Name')]) == name) ]
        print(f"Reservation for {name} with Table Number {table_number} has successfully been cancel")
#                     
    with open(reservations_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(reservations)
            
def modify_reservation(reservations_file):
    #collect user input inorder to extract the row to be updated
    table_number_to_update = int(input("Enter the table number to update: "))
    name_to_update = input("Enter the name of the reservation to update: ")
    name_to_update = name_to_update.lower()
    date_to_update = input("Enter the date of the reservation to update (YYYY-MM-DD): ")
    # Collect user input for the updated row
    new_name = input("Enter the new Name: ")
    new_name = new_name.lower()
    new_contact = input("Enter the new Contact ")
    new_party_size = input("Enter the new Party Size ")
    new_start_time = input("Enter the new Start time (HH:MM): ")
    new_end_time = input("Enter the new End time (HH:MM): ")
    new_table_number = input("Enter the new Table Number ")
    new_reservation_date = input("Enter the new reservation Date (YYYY-MM-DD): ")
    try:
        # Read the content of the CSV file
        with open(reservations_file, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            header = reader.fieldnames
            
            # Debug: Print the header
            # print("Header:", header)
            # Check if the necessary columns are present in the header
            required_columns = ['Name','Contact','Party Size','Start time', 'End time','Date','Table Number']
            for col in required_columns:
                if col not in header:
                    print(f"Error: Required column '{col}' not found in the CSV header.")
                    return
            rows = []
            record_found = False  # Flag to track if a record was updated

            # Iterate through each row and update the specified one
            for res in reader:
                # Debug: Print the row being processed
                # print("Processing row:", res)
                #The res.get function is a method for dictionaries in Python, which allows you to 
                # retrieve the value associated with a given key.
                table_number_value = res.get('Table Number') 
                name_value = res.get('Name')
                date_value = res.get('Date')
                # Check if the row matches the criteria
                if (table_number_value is not None and 
                    name_value is not None and 
                    date_value is not None and
                    int(table_number_value) == table_number_to_update and 
                    name_value == name_to_update and 
                    date_value == date_to_update):
                    
                    # Create the updated row as a dictionary
                    updated_row = res
                    updated_row['Date'] = new_reservation_date
                    updated_row['Start time'] = new_start_time
                    updated_row['End time'] = new_end_time
                    updated_row['Name'] = new_name
                    updated_row['Contact'] = new_contact
                    updated_row['Party Size'] = new_party_size
                    updated_row['Table Number'] = new_table_number
                    rows.append(updated_row)
                    record_found = True  # Set the flag to True
                else:
                    rows.append(res)

        # Write the updated content back to the CSV file
        with open(reservations_file, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=header)
            writer.writeheader()
            writer.writerows(rows)

         # Provide feedback based on whether the record was found and updated
        if record_found:
            print(f"Record for Table Number {table_number_to_update}, Name {name_to_update}, Date {date_to_update} has been updated.")
        else:
            print(f"No record found for Table Number {table_number_to_update}, Name {name_to_update}, Date {date_to_update}.")

    except Exception as e:
        print(f"Error updating record: {e}")

def daily_summary(reservations_file):
    # Get the current date
    summary_option = int(input("Enter 1 for Today Summary \nEnter 2 for any other day\n"))
    if summary_option == 1:
        date = datetime.now().strftime('%Y-%m-%d')
        print("date = ", date)
    else:
        date = input("Enter Date to find it summary ")
    
    try:
        # Read the content of the CSV file
        with open(reservations_file, mode='r', newline='') as file:
            reader = csv.DictReader(file)
        # Filter reservations for the date
            reservations = [res for res in reader if res.get('Date') == date ]
            # Print summary
            if reservations:
                print(f"Summary of reservations for - {date}:")
                for each_reservation in reservations:
                    print(f" Name: {each_reservation.get('Name')} Contact:{each_reservation.get('Contact')} Party Size:{each_reservation.get('Party Size')} Reservation Start Time: {each_reservation.get('Start time')} Reservation End Time: {each_reservation.get('End time')} Reservation Date: {each_reservation.get('Date')} Reservation Table Number: {each_reservation.get('Table Number')} ")
            else:
                print(f"No reservations for {date}.")

    except Exception as e:
        print(f"Error getting daily summary: {e}")

# # Function to make the code run at the Terminal
def start():
        print("Choose from the below options 1-5")
        print("Option 1 stands for View Table: ")
        print("Option 2 stands for make reservation: ")
        print("Option 3 stands for Cancel reservation: ")
        print("Option 4 stands for View Reservations: ")
        print("Option 5 stands for Modify Reservation: ")
        print("Option 6 stands for daily summary: ")
        function_label = int(input('Enter number for the action you want to perform: '))
        if function_label == 1:
            view_tables(lists_of_table)
        elif function_label == 2:
            make_reservation(lists_of_table, reservations_file)
        elif function_label == 3:
            cancel_reservation(reservations_file)
        elif function_label == 4:
            view_reservations(reservations_file)
        elif function_label == 5:
            modify_reservation(reservations_file)
        elif function_label == 6:
            daily_summary(reservations_file)
        else:
            print("You entered invalid Number")
start()
