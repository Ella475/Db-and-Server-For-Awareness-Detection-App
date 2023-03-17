import csv

import pandas as pd
from tqdm import tqdm

from db.db_connection import connect_to_db, disconnect, execute_query


def create_tables(db, cursor, tables_queries):
    for query in tables_queries:
        execute_query(db, cursor, query)

    execute_query(db, cursor, "SHOW TABLES", commit=False)
    print("Created tables:")
    for table_name in cursor:
        print(table_name[0])


def create_tables_queries():
    queries = []

    users_query = \
        """CREATE TABLE users (
              id INT(11) NOT NULL AUTO_INCREMENT,
              username VARCHAR(255) NOT NULL,
              password VARCHAR(255) NOT NULL,
              PRIMARY KEY (id)
            );"""
    queries.append(users_query)

    drives_query = \
        """CREATE TABLE drives (
              id INT(11) NOT NULL AUTO_INCREMENT,
              driver_id INT(11) NOT NULL,
              PRIMARY KEY (id),
              FOREIGN KEY (driver_id) REFERENCES users(id)
            );"""
    queries.append(drives_query)

    drive_data_query = \
        """
        CREATE TABLE drive_data (
          id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
          drive_id INT(11) NOT NULL,
          awareness_percentage INT(11) NOT NULL,
          asleep BOOLEAN NOT NULL,
          inattentive BOOLEAN NOT NULL,
          FOREIGN KEY (drive_id) REFERENCES drives(id)
        );
        """
    queries.append(drive_data_query)

    return queries


def insert_records(db, cursor, queries):
    for k, (table, query) in enumerate(queries.items()):
        print()
        print('Inserting records to table: ' + table)
        table_path = query[1]
        table_query = query[0]

        for i, chunk in tqdm(enumerate(pd.read_csv(table_path, chunksize=1000))):
            records = chunk.where(pd.notnull(chunk), None).to_records(index=False).tolist()
            execute_query(db, cursor, table_query, True, records)


def create_driver_awareness_db():
    db, cursor = connect_to_db(delete_if_exist=True)
    tables_queries = create_tables_queries()
    create_tables(db, cursor, tables_queries)
    disconnect(db, cursor)
