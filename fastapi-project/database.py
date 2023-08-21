from pymongo import MongoClient
import os


def get_mongo_client():
    MONGO_DB_URL = str(os.environ.get("MONGO_DB_URL"))
    if not MONGO_DB_URL:
        raise ValueError("MONGO_DB_URL is not set in environment variables.")
    return MongoClient(MONGO_DB_URL)


def get_drinks_db(client=None):
    if client is None:
        client = get_mongo_client()
    return client.test.drinks


# mongodb+srv://aleyadri:<password>@drink-api.zahpxpn.mongodb.net/?retryWrites=true&w=majority
