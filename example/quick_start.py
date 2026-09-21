from mini_db.db import MiniDB

db = MiniDB("example_data.json")

db.create_table("users", schema={"id": "int", "name": "str", "age": "int"})

db.insert("users", {"id": 1, "name": "Hiroshima", "age": 29})
db.insert("users", {"id": 2, "name": "Japan", "age": 34})

print(db.select("users"))
print(db.select("users", {"name": "India"}))

db.update("users", {"id": 1}, {"age": 30})
print(db.select("users", {"id": 1}))

db.delete("users", {"id": 2})
print(db.select("users"))