from flask import Flask, request, render_template, jsonify

from db.db_connection import yield_query_result, execute_query
from server.queries import check_user, insert_user, check_username, get_user_id_by_username, get_drive_data_by_drive_id
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
        # if username and password are not provided, return 400
        else:
            return jsonify({"response": False, "error": "Bad request"}), 400

    if request.method == 'POST':
        request_as_dict = request.get_json(force=True)
        db, cursor = connection.get()
        if 'username' in request_as_dict and 'password' in request_as_dict and len(request_as_dict) == 2:
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
        else:
            return jsonify({"response": False, "error": "Bad request"}), 400


@app.route('/drives', methods=['GET', 'POST'])
def drives():
    if request.method == 'GET':
        request_as_dict = request.get_json(force=True)
        db, cursor = connection.get()
        return jsonify({"response": yield_query_result(db, cursor, get_drive_data_by_drive_id(**request_as_dict))})
    if request.method == 'POST':
        request_as_dict = request.get_json(force=True)
        db, cursor = connection.get()
        return jsonify({"response": execute_query(db, cursor, get_drive_data_by_drive_id(**request_as_dict))})


def start_server():
    connection.start()
    app.run(debug=True)


def stop_server():
    connection.stop()


# if __name__ == '__main__':
#     connection.start()
#     app.run(debug=True)
#     connection.stop()
