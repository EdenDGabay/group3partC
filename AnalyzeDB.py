import pymongo
import json
from pymongo.server_api import ServerApi
import certifi
import os

from dotenv import load_dotenv
load_dotenv()

def AnalyzeDB():
    # Extract the connection details from the configuration
    uri = os.environ.get('DB_URI'), 

    # Create the MongoDB connection
    client = pymongo.MongoClient(uri, server_api=ServerApi('1'), tlsCAFile=certifi.where())

    # Return the connection object
    db = client[os.environ.get('DB_NAME')]

    # Print all documents in the Books collection
    books_collection = db['Books']
    for document in books_collection.find():
        print(document)

    # Print all documents in the Users collection
    users_collection = db['Users']
    for document in users_collection.find():
        print(document)

    # Print all documents in the Categories collection
    categories_collection = db['Categories']
    for document in categories_collection.find():
        print(document)