import mysql.connector
from mysql.connector import Error

from utils.detailes import get_username_password


def connect_to_db(db_name='driving_db', delete_if_exist: bool = False):
    details = get_username_password()
    username, password = details['username'], details['password']
    sql_connection = mysql.connector.connect(
        host="localhost",
        user=username,
        password=password,
    )

    my_cursor = sql_connection.cursor()

    my_cursor.execute("SHOW DATABASES")
    db_names = my_cursor.fetchall()

    if delete_if_exist:
        if (db_name,) in db_names:
            execute_query(sql_connection, my_cursor, "DROP DATABASE " + db_name)
            db_names.remove((db_name,))

    if (db_name,) not in db_names:
        my_cursor.execute("CREATE DATABASE " + db_name)
        print("Created db: " + db_name)
    else:
        print("db: " + db_name + " found")

    my_cursor.close()
    sql_connection.close()

    my_db = mysql.connector.connect(
        host="localhost",
        user=username,
        password=password,
        database=db_name
    )

    my_cursor = my_db.cursor()

    return my_db, my_cursor


def disconnect(db, cursor):
    cursor.close()
    db.close()


def execute_query(db, cursor, query, commit: bool = True, val=None):
    try:
        if not val:
            cursor.execute(query)
        else:
            cursor.executemany(query, val)
        if commit:
            db.commit()

        return True
    except Error as e:
        print(f"The error '{e}' occurred")
        return False


def yield_query_result(db, cursor, query, max_rows: int = None):
    execute_query(db, cursor, query, commit=False)

    try:
        r = [dict((cursor.description[i][0], value) for i, value in enumerate(row)) for row in cursor.fetchall()]
    except Error as e:
        print(f"The error '{e}' occurred")
        return None
    print(query)

    return None if not r else r if max_rows is None else r[:max_rows]
