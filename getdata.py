import pandas as pd

# Path ke file CSV
csv_file_path = 'data.csv'

# Membaca file CSV menggunakan pandas
df = pd.read_csv(csv_file_path)

# Looping per baris dan mencetak nilai variabel
for index, row in df.iterrows():
    email = row['Email IL']
    firstName = row['First Name']
    lastName = row['Last Name']
    username = row['Username RHNID']
    password = row['Password RHNID']
    
    print(f"Row {index + 1}:")
    print(f"  Email: {email}")
    print(f"  First Name: {firstName}")
    print(f"  Last Name: {lastName}")
    print(f"  Username: {username}")
    print(f"  Password: {password}")
    print()
