import argparse
from db.create_sql_db import create_driver_awareness_db


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--delete', action='store_true', help='Delete the database if it exists')
    args = parser.parse_args()
    delete_if_exist = args.delete
    create_driver_awareness_db(delete_if_exist=delete_if_exist)
