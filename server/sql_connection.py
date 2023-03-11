from db.db_connection import connect_to_db, disconnect


class SQLConnection:

    def __init__(self):
        self.db, self.cursor = None, None

    def start(self):
        self.db, self.cursor = connect_to_db()

    def stop(self):
        disconnect(self.db, self.cursor)

    def get(self):
        return self.db, self.cursor


if __name__ == '__main__':
    connection = SQLConnection()
    connection.start()
    connection.stop()
    