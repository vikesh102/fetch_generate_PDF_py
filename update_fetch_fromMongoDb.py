
from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

# Connect to MongoDB
client = MongoClient('mongodb://10.236.76.215:27017')  # Replace with your MongoDB connection string

# Access the database and collection
database = client['locobotDB']  # Replace with your database name
collection = database['pdfData']  # Replace with your collection name

@app.route('/update_record', methods=['POST'])
def update_record():
    data = request.json
    print(data)
    # Define the filter based on user keys
    filter = data.get('user_data')
    print("filter here " , filter)
    print(data.get('damage_report'))
    update = {'$push': {'observations': data.get('damage_report')}}
    # Check if the record exists
    existing_record = collection.find_one(filter)
    print("existing record", existing_record)
    if existing_record:
        # Update the document
        result = collection.update_one(filter, update)
        print(f'{result.modified_count} document(s) updated.')
    else:
        # Create a new document with a blank array
        new_document = filter.copy()  # Replace 'array_field' with your actual array field name
        new_document.update({'observations': []})
        # Insert the new document
        result = collection.insert_one(new_document)
        print(f'{result.inserted_id} document inserted.')

        # Update the document
        result = collection.update_one(filter, update)
        print(f'{result.modified_count} document(s) updated.')
    return 'success', 200
@app.route('/get_record', methods=['POST'])
def fetch_records():
    data = request.json
    filter = data.get('user_data')
    print("filter ",filter)
    # fetched = collection.find_one(filter)
    fetched = collection.find_one(filter)
    if fetched is not None:
        fetched['_id'] = str(fetched['_id'])
    return jsonify(fetched)


if __name__ == '__main__':
    app.run()
    # Close the MongoDB connection
    client.close()
