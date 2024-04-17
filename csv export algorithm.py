from pymongo import MongoClient
import csv

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['user_data']
collection = db['users']

# Retrieve data from MongoDB
cursor = collection.find({}, {'_id': 0, 'expenses': 0})  # Exclude _id and expenses fields
data = list(cursor)

# Define CSV file path
csv_file = 'user_data.csv'

# Write data to CSV file
with open(csv_file, 'w', newline='') as file:
    # Define fieldnames including the name column
    fieldnames = ['name', 'age', 'gender', 'total_income', 'utilities', 'entertainment', 'school_fees', 'shopping', 'healthcare']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

print(f"Data has been stored in {csv_file}")
