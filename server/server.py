from datetime import datetime

from flask import Flask, request, jsonify

from db.db_connection import yield_query_result, execute_query
from server.queries import *
from server.sql_connection import SQLConnection

app = Flask(__name__)
connection = SQLConnection()


@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        # get username from request
        username = request.args.get('username')
        # get password from request
        password = request.args.get('password')
        # check if only username is provided
        if not username:
            return jsonify({"response": False, "error": "Bad request"}), 400

        if username and not password:
            db, cursor = connection.get()
            response = yield_query_result(db, cursor, check_username(username))
            # if user exists, return True
            if response:
                return jsonify({"response": True})
            # if user does not exist, return False
            else:
                return jsonify({"response": False})
        # check if username and password are provided
        elif username and password:
            db, cursor = connection.get()
            response = yield_query_result(db, cursor, check_user(username, password))
            # if user password is correct, return user id
            if response:
                response_str = str(response[0]['id'])
                return jsonify({"response": response_str})
            # if user password is incorrect, return False
            else:
                return jsonify({"response": False})

    if request.method == 'POST':
        request_as_dict = request.get_json(force=True)
        db, cursor = connection.get()

        if 'username' not in request_as_dict or 'password' not in request_as_dict:
            return jsonify({"response": False, "error": "Bad request"}), 400

        if 'username' in request_as_dict and 'password' in request_as_dict:
            response = execute_query(db, cursor, insert_user(**request_as_dict))
            if response:
                response = yield_query_result(db, cursor, get_user_id_by_username(request_as_dict.get("username")))
                if response:
                    response_str = str(response[0]['id'])
                    return jsonify({"response": response_str})
                else:
                    return jsonify({"response": False})
            else:
                return jsonify({"response": False})


@app.route('/drives', methods=['GET', 'POST'])
def drives():
    if request.method == 'POST':
        # get userId from request
        request_as_dict = request.get_json(force=True)
        if 'user_id' not in request_as_dict:
            return jsonify({"response": False, "error": "Bad request"}), 400

        db, cursor = connection.get()
        time = datetime.now().strftime("%d.%m.%Y %H:%M")
        response = execute_query(db, cursor, insert_drive(**request_as_dict, time=time))
        if response:
            response = yield_query_result(db, cursor, get_last_drive_id(**request_as_dict))
            if response:
                # get value of first

                response_str = str(response[0].popitem()[1])
                return jsonify({"response": response_str})
            else:
                return jsonify({"response": False})
        else:
            return jsonify({"response": False})

    if request.method == 'GET':
        # get userId from request
        userid = request.args.get('user_id')
        db, cursor = connection.get()
        response = yield_query_result(db, cursor, get_drives_by_user_id(userid))
        # if user exists, return drive id
        if response:
            # return all drive ids
            response_str = str(response)
            return jsonify({"response": response_str})
        # if user does not exist, return False
        else:
            return jsonify({"response": False})


@app.route('/drives_data', methods=['GET', 'POST'])
def drives_data():
    if request.method == 'GET':
        if 'drive_id' in request.args:
            arg = request.args.get('drive_id')
            func = get_drive_data_by_drive_id
        else:
            return jsonify({"response": False, "error": "Bad request"}), 400

        db, cursor = connection.get()
        response = yield_query_result(db, cursor, func(arg))
        if response:
            response = str(response)
            return jsonify({"success": True, "response": response})
        # if user does not exist, return False
        else:
            return jsonify({"success": False})

    if request.method == 'POST':
        # get driveId, awareness_percentage, asleep, head_pose from request
        request_as_dict = request.get_json(force=True)
        if 'drive_id' not in request_as_dict:
            return jsonify({"response": False, "error": "Bad request"}), 400

        db, cursor = connection.get()
        response = execute_query(db, cursor, insert_drive_data(**request_as_dict))
        print(response)
        if response:
            # return all drive data
            response_str = str(response)
            return jsonify({"response": response_str})
        # if user does not exist, return False
        else:
            return jsonify({"response": False})


def start_server():
    connection.start()
    app.run(host='0.0.0.0', debug=True)


def stop_server():
    connection.stop()

