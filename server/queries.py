# Description: This file contains all the queries that are used in the server

def get_table(is_supervisor=False):
    if is_supervisor:
        return 'supervisors'
    else:
        return 'users'


def insert_user(username, password, is_supervisor=False):
    table = get_table(is_supervisor)
    return f'INSERT INTO {table} (Username, Password) VALUES (' \
           f'"{username}","{password}")'


def check_user(username, password, is_supervisor=False):
    table = get_table(is_supervisor)
    return f'SELECT id FROM {table} WHERE Username ="{username}" AND Password ="{password}"'


def check_username(username, is_supervisor=False):
    table = get_table(is_supervisor)
    return f'SELECT * FROM {table} WHERE Username ="{username}"'


def get_user_id_by_username(username, is_supervisor=False):
    table = get_table(is_supervisor)
    return f'SELECT id FROM {table} WHERE Username = "{username}"'


def insert_drive(user_id, time):
    return f'INSERT INTO drives (user_id, time) VALUES ({user_id}, "{time}")'


def insert_drive_data(drive_id, awareness_percentage, asleep, inattentive):
    return f'INSERT INTO drive_data (Drive_ID, Awareness_Percentage, Asleep, Inattentive) ' \
           f'VALUES ({drive_id}, {awareness_percentage}, {asleep}, {inattentive})'


def get_drives_by_user_id(user_id):
    return f'SELECT * FROM drives WHERE drives.user_id = {user_id}'


def get_drive_data_by_drive_id(drive_id):
    return f'SELECT * FROM drive_data WHERE drive_data.Drive_ID = {drive_id}'


def get_last_drive_id(user_id):
    return f'SELECT MAX(drives.id) FROM drives WHERE drives.user_id = {user_id}'


def insert_supervised_user(supervisor_id, user_id):
    return f'INSERT INTO supervised_users (supervisor_id, user_id) VALUES ({supervisor_id}, {user_id})'


def get_supervised_usernames(supervisor_id):
    return f'SELECT users.id, users.username FROM supervised_users ' \
           f'INNER JOIN users ON supervised_users.user_id = users.id ' \
           f'WHERE supervised_users.supervisor_id = {supervisor_id}'
