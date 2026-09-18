# insert, select, update, delete
from .table import validate_record

def matches_criteria(row, criteria):
    return all(row.get(k) == v for k, v in criteria.items())

def insert_record(db, table_name, record):
    table = db["tables"].get(table_name)
    if not table:
        raise ValueError(f"Table '{table_name}' does not exist.")
    validate_record(table["schema"], record)
    table["rows"].append(record)
    

def select_records(db, table_name, criteria=None):
    table = db["tables"].get(table_name)
    if not table:
        raise ValueError(f"Table '{table_name}' does not exist.")
    if criteria is None:
        return table["rows"]
    return [row for row in table["rows"] if matches_criteria(row, criteria)]

def update_records(db, table_name, criteria, updates):
    table = db["tables"].get(table_name)
    if not table:
        raise ValueError(f"Table '{table_name}' does not exist.")
    for row in table["rows"]:
        if matches_criteria(row, criteria):
            for k, v in updates.items():
                if k in table["schema"]:
                    row[k] = v
                else:
                    raise ValueError(f"Column '{k}' does not exist in table '{table_name}'.")
    

def delete_records(db, table_name, criteria):
    table = db["tables"].get(table_name)
    if not table:
        raise ValueError(f"Table '{table_name}' does not exist.")
    original_count = len(table["rows"])
    table["rows"] = [row for row in table["rows"] if not matches_criteria(row, criteria)]
    deleted_count = original_count - len(table["rows"])
    return deleted_count

