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
table_numbers = []
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
    for table in available_tables:
        print(f"Table {table['table']} - Seats {table['seats']}")
        table_numbers.append(table['table'])

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
    file_exists = os.path.isfile(reservations_file)
    if file_exists:
    #This line checks if a file specified by reservations_file exists and assigns the result (True or False) to file_exists
        try:    
            with open(reservations_file, mode='r', newline='') as file:
                #this line creates a CSV reader object that can iterate over lines in the CSV file specified by file
                reader = csv.reader(file)
                print(f"Here is the lists of reservations that has been made:")
                for row in reader:
                    print(f"{row[0]},{row[1]}, {row[3]},{row[4]},{row[5]},{row[6]}")
        except Exception as e:
            print(f"Error viewing reservation:{e}")
                
# calling the functions that was created
# The parameter table_number serves as the unique id that is been used to 
# identify the particular reservation what will be deleted

def cancel_reservation(reservations_file,table_number):

    file_exists = os.path.isfile(reservations_file)
    if file_exists:
    #This line checks if a file specified by reservations_file exists and assigns the result (True or False) to file_exists
                rows = []
                with open(reservation, mode='r', newline='') as file:
                    reader = csv.DictReader(file)
                    
                    fieldnames = reader.fieldnames
                    for row in reader:
                        print(row['Table Number'])
                        if row['Table Number'] != str(table_number):
                                rows.append(row)
                        print(f"Reservation for Table {table_number} has successfully been cancel")
                            

                # Write the updated data back to the CSV file
                with open(reservation, mode='w', newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(rows)

            # Example usage
reservation = 'reservations_file.csv'
table_number = 4  # The table ID to identify the row to delete
cancel_reservation(reservation, table_number)
                
# view_tables(lists_of_table)
make_reservation(lists_of_table,reservations_file)
# view_reservations(reservations_file)   
# cancel_reservation()
