import json
import os
import tempfile

def save_db(file_path, data):
    dir_name = os.path.dirname(os.path.abspath(file_path))
    fd, tmp_path = tempfile.mkstemp(dir=dir_name, suffix=".tmp")
    try:
        with os.fdopen(fd, 'w') as f:
            json.dump(data, f, indent=4)
        os.replace(tmp_path, file_path)
    except Exception:
        os.remove(tmp_path)
        raise
    
def load_db(file_path):
    if not os.path.exists(file_path):
        return {"tables":{}}
    with open(file_path, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError as e:
            raise ValueError(f"Corrupted database file: {file_path}") from e
