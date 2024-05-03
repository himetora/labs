import psycopg2
import csv

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="himetora"
)

cur = conn.cursor()

def upload_data_from_csv(filename, table_name):
    try:
        with open(filename, 'r') as f:
            reader = csv.reader(f, delimiter=";")
            next(reader)
            for row in reader:
                first_name, last_name, phone, email = row
                cur.execute(
                    f"INSERT INTO {table_name} (first_name, last_name, phone, email) VALUES (%s, %s, %s, %s)",
                    (first_name, last_name, phone, email,)
                )
            conn.commit()
            print("Data uploaded successfully from", filename)
    except Exception as e:
        print("Error uploading data:", e)

def update_data(id, column, value, table_name):
    try:
        cur.execute(
            f"UPDATE {table_name} SET {column} = %s WHERE id = %s",
            (value, id)
        )
        conn.commit()
        print("Data updated successfully")
    except Exception as e:
        print("Error updating data:", e)

def insert_data_from_console(table_name):
    try:
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email address: ")
        cur.execute(
            f"INSERT INTO {table_name} (first_name, last_name, phone, email) VALUES (%s, %s, %s, %s)",
            (first_name, last_name, phone, email)
        )
        conn.commit()
        print("Data inserted successfully")
    except Exception as e:
        print("Error inserting data:", e)

def query_data(column, value, table_name):
    try:
        cur.execute(
            f"SELECT * FROM {table_name} WHERE {column} = %s",
            (value,)
        )
        rows = cur.fetchall()
        if len(rows) == 0:
            print("No records found")
        else:
            for row in rows:
                print(row)
    except Exception as e:
        print("Error querying data:", e)

def delete_data(column, value, table_name):
    try:
        cur.execute(
            f"DELETE FROM {table_name} WHERE {column} = %s",
            (value,)
        )
        conn.commit()
        print("Data deleted successfully")
    except Exception as e:
        print("Error deleting data:", e)

upload_data_from_csv('PhoneBook_data.csv', 'PhoneBook')
insert_data_from_console('PhoneBook')
update_data(1, 'first_name', 'Jane', 'PhoneBook')
query_data('last_name', 'Jones', 'PhoneBook')
delete_data('last_name', 'Harris', 'PhoneBook')

cur.close()
conn.close()
