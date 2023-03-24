from db.db_connection import connect_to_db, disconnect, execute_query


def create_tables(db, cursor, tables_queries):
    execute_query(db, cursor, "SHOW TABLES", commit=False)
    existing_table_names = [table_name[0] for table_name in cursor]
    print("Existing tables:")
    for table_name in existing_table_names:
        print(table_name)

    print("Created tables:")
    for table_name, query in tables_queries:
        if table_name not in existing_table_names:
            execute_query(db, cursor, query)
            print(table_name)


def create_tables_queries():
    queries = []

    users_query = \
        """CREATE TABLE users (
              id INT(11) NOT NULL AUTO_INCREMENT,
              username VARCHAR(255) NOT NULL,
              password VARCHAR(255) NOT NULL,
              PRIMARY KEY (id)
            );"""
    queries.append(('users', users_query))

    drives_query = \
        """CREATE TABLE drives (
              id INT(11) NOT NULL AUTO_INCREMENT,
              user_id INT(11) NOT NULL,
              time VARCHAR(255) NOT NULL,
              PRIMARY KEY (id),
              FOREIGN KEY (user_id) REFERENCES users(id)
            );"""
    queries.append(('drives', drives_query))

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
    queries.append(('drive_data', drive_data_query))

    supervisors_query = \
        """CREATE TABLE supervisors (
              id INT(11) NOT NULL AUTO_INCREMENT,
              username VARCHAR(255) NOT NULL,
              password VARCHAR(255) NOT NULL,
              PRIMARY KEY (id)
            );"""
    queries.append(('supervisors', supervisors_query))

    supervisors_users_query = \
        """CREATE TABLE supervised_users (
              id INT(11) NOT NULL AUTO_INCREMENT,
                supervisor_id INT(11) NOT NULL,
              user_id INT(11) NOT NULL,
              PRIMARY KEY (id),
              FOREIGN KEY (user_id) REFERENCES users(id),
              FOREIGN KEY (supervisor_id) REFERENCES supervisors(id)
            );"""
    queries.append(('supervised_users', supervisors_users_query))

    return queries


def create_driver_awareness_db(delete_if_exist=True):
    db, cursor = connect_to_db(delete_if_exist=delete_if_exist)
    tables_queries = create_tables_queries()
    create_tables(db, cursor, tables_queries)
    disconnect(db, cursor)
