# Mini-DB

A simple database engine built from scratch in Python, as a learning project. Mini-DB stores data in JSON files and supports creating tables, inserting records, querying with filters, updating, and deleting — all through a simple command-line interface.

## Why

This project is an attempt to understand how a database actually works underneath, by building one from scratch — in-memory data modeling, saving data to disk, filtering records, and basic query logic.

## Features

- Create tables with a defined schema
- Insert, select, update, and delete records
- Filter records using equality, comparison operators (`$gt`, `$lt`, `$gte`, `$lte`, `$ne`), and logical combinators (`$and`, `$or`)
- Data persisted to a JSON file with atomic writes (no corrupted files on a crash mid-save)
- Simple command-line interface to interact with the database

## Getting started

### 1. Clone the repository

```bash
git clone https://github.com/Swarnim-Dubey/Mini-DB.git
cd Mini-DB
```

### 2. Install dependencies

This project uses [uv](https://docs.astral.sh/uv/) for environment and dependency management.

```bash
uv sync
```

### 3. Run the CLI

```bash
uv run main.py
```

You'll see a menu like this:

```
1. Create Table
2. Insert Record
3. Select Records
4. Update Records
5. Delete Records
6. Exit
Enter your choice:
```

## Usage examples

#### Create a table

```
Enter your choice: 1
Enter table name: users
Enter schema (e.g., id:int,name:str,age:int): id:int,name:str,age:int
Table 'users' created successfully.
```

#### Insert a record

```
Enter your choice: 2
Enter table name: users
id (int): 1
name (str): Ava
age (int): 29
Record inserted.
```

#### Select records

Leave the criteria blank to fetch every record:

```
Enter your choice: 3
Enter table name: users
Enter criteria (e.g., name:John) or leave blank for all records:
Records in 'users': [{'id': 1, 'name': 'Ava', 'age': 29}]
```

Or filter by a field:

```
Enter your choice: 3
Enter table name: users
Enter criteria (e.g., name:John) or leave blank for all records: name:Ava
Records in 'users': [{'id': 1, 'name': 'Ava', 'age': 29}]
```

#### Update records

```
Enter your choice: 4
Enter table name: users
Enter criteria (e.g., id:1): id:1
Enter updates (e.g., age:31): age:30
Records in 'users' updated successfully.
```

#### Delete records

```
Enter your choice: 5
Enter table name: users
Enter criteria (e.g., id:1): id:1
1 records deleted from 'users'.
```

#### Exit

```
Enter your choice: 6
Exiting MiniDB CLI.
```