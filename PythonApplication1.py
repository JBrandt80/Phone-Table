import sqlite3

# Connect to SQLite database (creates the file if it doesn't exist)
conn = sqlite3.connect('phones.db')
cursor = conn.cursor()

# Drop table if it exists
cursor.execute('DROP TABLE IF EXISTS phone')
conn.commit()
print("Dropped existing table (if any).")

# Create the table
cursor.execute('''CREATE TABLE IF NOT EXISTS phone (
    phone_id INTEGER PRIMARY KEY, 
    country_code TEXT NOT NULL,
    phone_number INTEGER NOT NULL,
    phone_type TEXT
)
''')
conn.commit()
print("Created new table.")

# Insert sample data
sample_data = [
    (1, 'US', 1234567890, 'CELLULAR'),
    (2, 'US', 9876543210, 'LANDLINE'),
    (3, 'XX', 5555555555, 'CELLULAR'),
    (4, 'CA', 4444444444, 'LANDLINE')
]
cursor.executemany('INSERT OR REPLACE INTO phone VALUES (?, ?, ?, ?)', sample_data)
conn.commit()
print("Inserted sample data.")

# Select phone numbers where country_code is 'US'
print("US Phone Numbers:")
cursor.execute('SELECT phone_number FROM phone WHERE country_code = ?', ('US',))
for row in cursor.fetchall():
    print(f" -{row[0]}")

# Update phone_type from 'CELLULAR' to 'MOBILE'
cursor.execute('UPDATE phone SET phone_type = ? WHERE phone_type = ?', ('MOBILE', 'CELLULAR'))
conn.commit()
print("\nUpdated phone_type from 'CELLULAR' to 'MOBILE'.")

# Delete rows where country_code is 'XX'
cursor.execute('DELETE FROM phone WHERE country_code = ?', ('XX',))
conn.commit()
print("Deleted rows with country_code = 'XX'.")

# Show remaining rows
print("\nRemaining Rows in table:")
cursor.execute('SELECT * FROM phone')
for row in cursor.fetchall():
    print(f" -{row}")

# Drop the table
cursor.execute('DROP TABLE IF EXISTS phone')
conn.commit()
print("\nDropped the table.")

# Close the connection
conn.close()
print("Connetion closed.")
