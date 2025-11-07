from pymongo import MongoClient

client = MongoClient("mongodb+srv://maria:YJQwTuiCQzcNmOBo@cluster0.zxkwa2s.mongodb.net/")
db = client["catalogosites"]
colecao_voos = db["voos"]