import pymongo
import json
from pymongo.server_api import ServerApi
import certifi
from flask import current_app
def mongo_db_instance() -> pymongo.database.Database:

    # Extract the connection details from the configuration
    uri = current_app.config['DB']['uri']  

    # Create the MongoDB connection
    client = pymongo.MongoClient(uri, server_api=ServerApi('1'), tlsCAFile=certifi.where())

    # Return the connection object
    return client[current_app.config['DB']['database']]