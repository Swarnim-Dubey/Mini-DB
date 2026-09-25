def create_table(db, name, schema):
    if name in db:
        raise ValueError(f"Table '{name}' already exists.")
    db["tables"][name] = {
        "schema": schema,
        "rows": []
    }

def drop_table(db, name):
    if name not in db:
        raise ValueError(f"Table '{name}' does not exist.")
    del db["tables"][name]

def validate_record(schema, record):
    for col, col_type in schema.items():
        if col not in record:
            raise ValueError(f"Missing column '{col}' in record.")
        expected_type = {"int": int, "str": str, "float": float, "bool": bool}.get(col_type)

        if expected_type and not isinstance(record[col], expected_type):
            raise ValueError(f"Field '{col}' expected type '{col_type}', got '{type(record[col]).__name__}'.")
    extra_fields = set(record.keys()) - set(schema.keys())
    if extra_fields:
        raise ValueError(f"Extra fields in record: {extra_fields}.")