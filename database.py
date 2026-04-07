from pymongo import MongoClient
from config import MONGO_URL

client = MongoClient(MONGO_URL)
db = client["quizbot"]

users = db["users"]

def add_user(user_id, name):
    if not users.find_one({"user_id": user_id}):
        users.insert_one({
            "user_id": user_id,
            "name": name,
            "score": 0
        })

def update_score(user_id, correct=True, neg=0.25):
    if correct:
        users.update_one({"user_id": user_id}, {"$inc": {"score": 1}})
    else:
        users.update_one({"user_id": user_id}, {"$inc": {"score": -neg}})

def get_top():
    return users.find().sort("score", -1).limit(10)
