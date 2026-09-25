def matches(row, criteria):
    for key, value in criteria.items():
        if key == "$and":
            if not all(matches(row, sub) for sub in value):
                return False
        elif key == "$or":
            if not any(matches(row, sub) for sub in value):
                return False
        elif isinstance(value, dict):
            for op, target in value.items():
                if not _apply_op(row.get(key), op, target):
                    return False
        else:
            if row.get(key) != value:
                return False
    return True

def _apply_op(field_value, op, target):
    ops = {
        "$gt": lambda a, b: a > b,
        "$lt": lambda a, b: a < b,
        "$gte": lambda a, b: a >= b,
        "$lte": lambda a, b: a <= b,
        "$ne": lambda a, b: a != b,
    }
    if op not in ops:
        raise ValueError(f"Unsupported operator: {op}")
    return ops[op](field_value, target)