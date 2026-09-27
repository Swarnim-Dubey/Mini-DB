from mini_db.db import MiniDB


def parse_typed_value(value, col_type):
    if col_type == "int":
        return int(value)
    elif col_type == "float":
        return float(value)
    elif col_type == "bool":
        return value.lower() in ("true", "1", "yes")
    return value


def parse_criteria(criteria_input, schema):
    result = {}
    for item in criteria_input.split(","):
        col, val = item.split(":")
        col = col.strip()
        val = val.strip()
        result[col] = parse_typed_value(val, schema.get(col, "str"))
    return result


def main():
    db = MiniDB("data.json")

    while True:
        print("\n1. Create Table")
        print("2. Insert Record")
        print("3. Select Records")
        print("4. Update Records")
        print("5. Delete Records")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            table_name = input("Enter table name: ")
            schema_input = input("Enter schema (eg., id:int,name:str,age:int): ")
            schema = dict(item.split(":") for item in schema_input.split(","))
            schema = {k.strip(): v.strip() for k, v in schema.items()}
            try:
                db.create_table(table_name, schema)
                print(f"Table '{table_name}' created successfully")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "2":
            table_name = input("Enter table name: ")
            try:
                schema = db.data["tables"][table_name]["schema"]
            except KeyError:
                print(f"Error: Table '{table_name}' does not exist")
                continue

            record = {}
            for column, col_type in schema.items():
                value = input(f"{column} ({col_type}): ")
                try:
                    value = parse_typed_value(value, col_type)
                except ValueError:
                    print(f"Error: '{value}' is not a valid {col_type} for '{column}'")
                    record = None
                    break
                record[column] = value

            if record is None:
                continue

            try:
                db.insert(table_name, record)
                print("Record inserted")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "3":
            table_name = input("Enter table name: ")
            try:
                schema = db.data["tables"][table_name]["schema"]
            except KeyError:
                print(f"Error: Table '{table_name}' does not exist")
                continue

            criteria_input = input("Enter criteria (e.g., name:John) or leave blank for all records: ")
            try:
                criteria = parse_criteria(criteria_input, schema) if criteria_input else None
            except ValueError as e:
                print(f"Error: invalid criteria value ({e})")
                continue

            try:
                records = db.select(table_name, criteria)
                print(f"Records in '{table_name}': {records}")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "4":
            table_name = input("Enter table name: ")
            try:
                schema = db.data["tables"][table_name]["schema"]
            except KeyError:
                print(f"Error: Table '{table_name}' does not exist")
                continue

            criteria_input = input("Enter criteria (e.g., id:1): ")
            updates_input = input("Enter updates (e.g., age:31): ")
            try:
                criteria = parse_criteria(criteria_input, schema)
                updates = parse_criteria(updates_input, schema)
            except ValueError as e:
                print(f"Error: invalid value ({e})")
                continue

            try:
                db.update(table_name, criteria, updates)
                print(f"Records in '{table_name}' updated successfully")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "5":
            table_name = input("Enter table name: ")
            try:
                schema = db.data["tables"][table_name]["schema"]
            except KeyError:
                print(f"Error: Table '{table_name}' does not exist")
                continue

            criteria_input = input("Enter criteria (eg., id:1): ")
            try:
                criteria = parse_criteria(criteria_input, schema)
            except ValueError as e:
                print(f"Error: invalid criteria value ({e})")
                continue

            try:
                deleted_count = db.delete(table_name, criteria)
                print(f"{deleted_count} records deleted from '{table_name}'")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "6":
            print("Exiting MiniDB CLI...")
            break

        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()