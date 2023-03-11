# Description: This file contains all the queries that are used in the server


def insert_user(username, password):
    return f'INSERT INTO users (Username, Password) VALUES (' \
           f'"{username}","{password}")'


def check_user(username, password):
    return f'SELECT * FROM users WHERE users.Username ="{username}" AND users.Password ="{password}"'


def check_username(username):
    return f'SELECT * FROM users WHERE users.Username ="{username}"'


def insert_drive(driver_id):
    return f'INSERT INTO drives (driver_id) VALUES ({driver_id})'


def insert_drive_data(drive_id, timestamp, attention_level, is_eye_closed, head_pose):
    return f'INSERT INTO drive_data (Drive_ID, Timestamp, Attention_Level, Is_Eye_Closed, Head_Pose) ' \
           f'VALUES ({drive_id}, "{timestamp}", {attention_level}, {is_eye_closed}, {head_pose})'


def get_drives_by_user_id(user_id):
    return f'SELECT * FROM drives WHERE drives.driver_id = {user_id}'


def get_drive_data_by_drive_id(drive_id):
    return f'SELECT * FROM drive_data WHERE drive_data.Drive_ID = {drive_id}'


def get_user_id_by_username(username):
    return f'SELECT users.id FROM users WHERE users.Username = "{username}"'


def get_last_drive_data(user_id):
    return f'SELECT * FROM drive_data WHERE drive_data.Drive_ID = ' \
           f'(SELECT MAX(drives.id) FROM drives WHERE drives.driver_id = {user_id})'


