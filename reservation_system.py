import csv
import os
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
    contact  = input('Enter your Contact Number')
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
                    print(f"{row[header.index('Name')]},{row[header.index('Contact')]}, {row[header.index('Party Size')]},{row[header.index('Start time')]},{row[header.index('End time')]},{row[header.index('Date')]}, {row[header.index('Table Number')]}")
        except Exception as e:
            print(f"Error viewing reservation:{e}")
                
# calling the functions that was created
# The parameter table_number serves as the unique id that is been used to 
# identify the particular reservation what will be deleted

def cancel_reservation(reservations_file,table_number,name):
    with open(reservations_file, mode='r', newline='') as file:      
        reader = csv.reader(file)
        header = next(reader,None)    
        reservations = list(reader)
        print("reader is", reader)
        row_to_remove =[reservations.remove(reserved_table) for reserved_table in reservations 
                                   if(int(reserved_table[header.index('Table Number')]) == table_number) and 
                                   ((reserved_table[header.index('Name')]) == name) ]
        print(f"Reservation for {name} with Table Number {table_number} has successfully been cancel")
#                     
    with open(reservations_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(reservations)
            

def update_reservation(reservations_file, table_number_to_update, name_to_update, date_to_update):
    with open(reservations_file, mode='r', newline='') as file:
        reader = csv.reader(file)
        header = next(reader)  # Assuming the first row is the header
        rows = []

        # Iterate through each row and update the specified one
        for res in reader:
            print(type(res[header.index('Table Number')]))
            if (int(res[header.index('Table Number')]) == table_number_to_update and 
                res[header.index('Name')] == name_to_update and 
                res[header.index('Date')] == date_to_update):
                # Create the updated row as a list
                updated_row = res
                new_name = input('Enter your Name: ')
                new_contact  = input('Enter your Contact Number')
                new_party_size = int(input('Enter Number of People: '))
                new_start_time =  input('Enter Reservation Start Time (HH:MM): ')
                new_end_time =  input('Enter Reservation End time (HH:MM): ')
                new_date =  input('Enter reservation Date (YYYY-MM-DD): ')
                new_table_number = int(input("Enter the New table Number"))
                
                updated_row[header.index('Name')] = new_name
                updated_row[header.index('Contact')] = new_contact
                updated_row[header.index('Party Size')] = new_party_size
                updated_row[header.index('Start time')] = new_start_time
                updated_row[header.index('End time')] = new_end_time
                updated_row[header.index('Date')] = new_date
                updated_row[header.index('Table Number')] = new_table_number
                
                rows.append(updated_row)
            else:
                rows.append(res)

    # Write the updated content back to the CSV file
    with open(reservations_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(rows)

# Example usage
# file_path = 'reservations.csv'
# table_number_to_check = 3
# name_to_check = 'Sofiyah'
# date_to_check = '2024-07-07'


# Function to make the code run at the Terminal
def start():
        print("Choose from the below options 1-5")
        print("Option 1 stands for View Table: ")
        print("Option 2 stands for make reservation: ")
        print("Option 3 stands for Cancel reservation: ")
        print("Option 4 stands for View Reservations: ")
        print("Option 5 stands for Modify Reservation: ")
        function_label = int(input('Enter number for the action you want to perform: '))
        if function_label == 1:
            view_tables(lists_of_table)
        elif function_label == 2:
            make_reservation(lists_of_table, reservations_file)
        elif function_label == 3:
            table_number = int(input("Enter table number that needs to be deleted "))
            name = input("Enter Name of the Table ")
            cancel_reservation(reservations_file,table_number,name)
        elif function_label == 4:
            view_reservations(reservations_file)
        elif function_label == 5:
            table_number_to_update = int(input("Enter the table number to update: "))
            name_to_update = input("Enter the name of the reservation to update: ")
            date_to_update = input("Enter the date of the reservation to update (YYYY-MM-DD): ")
            update_reservation(reservations_file, table_number_to_update, name_to_update, date_to_update)
        else:
            print("You entered invalid Number")
start()
