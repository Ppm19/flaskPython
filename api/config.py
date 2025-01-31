from pymongo import MongoClient

MONGO_URI = "mongodb+srv://ppermis:hola123@backvercel.n3fru.mongodb.net/?retryWrites=true&w=majority&appName=backVercel"
client = MongoClient(MONGO_URI)
db = client["robertExpress"]
