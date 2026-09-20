from .storage import load_db, save_db
from . import table
from . import crud

class MiniDB:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = load_db(file_path)

    def create_table(self, name, schema):
        table.create_table(self.data, name, schema)
        save_db(self.file_path, self.data)

    def drop_table(self, name):
        table.drop_table(self.data, name)
        save_db(self.file_path, self.data)

    def insert(self, table_name, record):
        crud.insert_record(self.data, table_name, record)
        save_db(self.file_path, self.data)

    def update(self, table_name, criteria, update):
        crud.update_records(self.data, table_name, criteria, update)
        save_db(self.file_path, self.data)

    def select(self, table_name, criteria=None):
        return crud.select_records(self.data, table_name, criteria)
    
    def delete(self, table_name, criteria):
        crud.delete_records(self.data, table_name, criteria)
        save_db(self.file_path, self.data)
        
